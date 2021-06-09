
from django.shortcuts import redirect, render
from carts.models import CartItem, Cart
from .forms import OrderForm
from .models import Order, OrderProduct, Payment
import datetime
from product.models import Product

from django.core.mail import EmailMessage
from django.template.loader import render_to_string

import uuid

# Create your views here.



def payments(request):
    # Store transaction details inside payment model(static approach)
    if request.method == 'POST':
        # customer_fullname = request.POST.get('full_name')
        # customer_email = request.POST.get('email')
        customer_order_number = request.POST.get('order_number')
        
        # persion transaction id generator
        user = str(request.user)
        transaction_list = [user, customer_order_number]
        service_provider = "deshicraft".join(transaction_list)
        transaction_id = uuid.uuid5(uuid.NAMESPACE_DNS, service_provider)
        customer_payment_method = 'personal_method'

        order = Order.objects.get(user=request.user, is_ordered=False, order_number=customer_order_number)

        # print(customer_fullname, customer_email, customer_order_number)
        payment = Payment(
            user = request.user,
            payment_id = transaction_id, # transaction id from third party will be here. 
            payment_method = customer_payment_method,
            amount_paid = order.order_total,
            status = "In Progress"
        )
        #saving the payment both for payment and order model
        payment.save()
        order.payment = payment
        order.is_ordered = True
        order.save()

        # move the cart items to order product table
        cart_items = CartItem.objects.filter(user=request.user)
        
        for item in cart_items:
            order_product = OrderProduct()
            order_product.order_id = order.id
            order_product.payment = payment
            order_product.user_id = request.user.id 
            order_product.product_id = item.product_id
            order_product.quantity = item.quantity
            order_product.product_price = item.product.price
            order_product.ordered = True
            order_product.save()

            # setting product variations(many to many field) for orderproduct table 
            cart_item = CartItem.objects.get(id=item.id)
            product_variation = cart_item.variations.all()
            order_product = OrderProduct.objects.get(id=order_product.id)
            order_product.variations.set(product_variation)
            order_product.save()

            # reduce the sold products quantity
            product = Product.objects.get(id=item.product_id)
            product.stock -= item.quantity
            product.save()

        # clearing the cart 
        CartItem.objects.filter(user=request.user).delete()

        # send order received email to customer 
        mail_subject = 'Thank you for your purchase!!!'
        mail_body = render_to_string('orders/order_received_email.html', {
            'user': request.user,
            'order': order
        })
        to_email = request.user.email
        send_email = EmailMessage(mail_subject, mail_body, to=[to_email])
        send_email.send()


        # send order number and transaction id back to transaction handler party
        # print(payment.payment_id)

        # from here should be in complete order if used a third party
        order = Order.objects.get(order_number=customer_order_number, is_ordered=True)
        ordered_products = OrderProduct.objects.filter(order_id=order.id)
        payment = Payment.objects.get(payment_id=transaction_id)

        subtotal = 0

        for item in ordered_products:
            subtotal += item.product_price * item.quantity
            
        context = {
            'order': order, 
            'ordered_products': ordered_products,
            'order_number' : order.order_number,
            'transID': payment.payment_id,
            'payment': payment,
            'subtotal': subtotal
        }
        return render(request, 'orders/order_complete.html', context)



# will be performed after login
def place_order(request):
    current_user = request.user

    # if the cart_count is less than or equal to 0, then redirect to shop
    cart_items = CartItem.objects.filter(user=current_user)
    cart_count = cart_items.count()
    if cart_count <= 0:
        return redirect('store')
    
    # calculate total monetary opeartion from cart item
    grand_total = 0
    tax = 0
    quantity = 0
    total = 0
    for cart_item in cart_items:
        total += (cart_item.product.price * cart_item.quantity)
        quantity += cart_item.quantity  
    # static tax
    tax = (2*total)/100
    grand_total = total+tax

    

    # handle the billing form data
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            # store all the billing data in order table
            data = Order()
            data.user = current_user
            data.first_name = form.cleaned_data['first_name']
            data.last_name = form.cleaned_data['last_name']
            data.phone = form.cleaned_data['phone']
            data.email = form.cleaned_data['email']
            data.address_lane_1 = form.cleaned_data['address_lane_1']
            data.address_lane_2 = form.cleaned_data['address_lane_2']
            data.country = form.cleaned_data['country']
            data.state = form.cleaned_data['state']
            data.city = form.cleaned_data['city']
            data.order_note = form.cleaned_data['order_note']
            data.order_total = grand_total
            data.tax = tax
            data.ip = request.META.get('REMOTE_ADDR') # for user ip
            data.save() # to generate order id for ordernumber 

            # generating uniqe order number based on current (year and datetime) and order primary key
            year = int(datetime.date.today().strftime('%Y'))
            date = int(datetime.date.today().strftime('%d'))
            month = int(datetime.date.today().strftime('%m'))

            time = datetime.date(year,month,date)
            current_date = time.strftime("%Y%m%d") # 20210522

            order_number = current_date + str(data.id)
            data.order_number = order_number

            data.save()

            order = Order.objects.get(user=current_user, is_ordered=False, order_number=order_number)
            context = {
                'order':order,
                'cart_items' : cart_items,
                'total': total,
                'tax': tax,
                'grand_total': grand_total
            }
            return render(request, 'orders/payments.html', context)

    else:
        return redirect('checkout')


def order_complete(request):
    return render(request, 'orders/order_complete.html')

