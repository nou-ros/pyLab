from django.http.response import HttpResponse
from django.shortcuts import get_object_or_404, render, redirect
from .models import Cart, CartItem
from product.models import Product, Variation
from django.contrib.auth.decorators import login_required

# Create your views here.

# to fetch the session id(python private function)
def _cart_id(request):
    cart = request.session.session_key
    if not cart:
        cart = request.session.create()
    return cart

def add_cart(request, product_id):
    current_user = request.user
    # get the product
    product = Product.objects.get(id=product_id)
    # if the user is authenticated
    if current_user.is_authenticated:
        product_variation = []
        # getting product variations
        if request.method == 'POST':
            # to take any variations (in future if we add more so we can dynamically get them)
            for item in request.POST:
                key = item
                value = request.POST[key]
                # print(key, value)

                try:
                    # if the variation category and value matches get the specific product
                    variation = Variation.objects.get(product=product, variation_category__iexact=key, variation_value__iexact=value)
                    # print(variation)
                    product_variation.append(variation)
                except:
                    pass
        
  
        # checking if the cart_item already exists so we can group same variations items for user
        is_cart_item_exists = CartItem.objects.filter(product=product, user=current_user).exists()

        if is_cart_item_exists:
            # grouping variations
            # when there is already cart item
            cart_item = CartItem.objects.filter(product=product, user=current_user)
            # existing variations
            ex_var_list = []
            id = []
            for item in cart_item:
                existing_variation = item.variations.all()
                ex_var_list.append(list(existing_variation))
                id.append(item.id)
            # print(ex_var_list)

            if product_variation in ex_var_list:
                # print("ache")
                # increase the cart item quantity
                index = ex_var_list.index(product_variation)
                item_id = id[index]
                item = CartItem.objects.get(product=product, id=item_id)
                item.quantity += 1
                item.save()

            else:
                # create a new cart item
                # print("nai")
                # adding the product variations in cartitem 
                item = CartItem.objects.create(product=product, user=current_user, quantity=1)
                if len(product_variation) > 0:
                    item.variations.clear()
                    item.variations.add(*product_variation)
                item.save()
                
        # when there is no cart item(initially add to cart operation)
        else:
            cart_item = CartItem.objects.create(
                product = product,
                quantity = 1,
                user=current_user
            )
            # adding the product variations in cartitem 
            if len(product_variation) > 0:
                cart_item.variations.clear()
                cart_item.variations.add(*product_variation)

            cart_item.save()
        
        # for testing purpose
        # return HttpResponse(cart_item.product)
        # exit()
        return redirect('cart')

    else:
        product_variation = []
        # getting product variations
        if request.method == 'POST':
            # to take any variations (in future if we add more so we can dynamically get them)
            for item in request.POST:
                key = item
                value = request.POST[key]
                # print(key, value)

                try:
                    # if the variation category and value matches get the specific product
                    variation = Variation.objects.get(product=product, variation_category__iexact=key, variation_value__iexact=value)
                    # print(variation)
                    product_variation.append(variation)
                except:
                    pass
        
        # getting cart
        try: 
            cart = Cart.objects.get(cart_id =_cart_id(request)) # get the cart using cart_id present in the session.
        except Cart.DoesNotExist:
            cart = Cart.objects.create(
                cart_id = _cart_id(request)
            )
        cart.save()

        # getting cart item

        # checking if the cart_item already exists so we can group same variations items 
        is_cart_item_exists = CartItem.objects.filter(product=product, cart=cart).exists()

        if is_cart_item_exists:
            # grouping variations
            # when there is already cart item
            cart_item = CartItem.objects.filter(product=product, cart=cart)
            # existing variations
            ex_var_list = []
            id = []
            for item in cart_item:
                existing_variation = item.variations.all()
                ex_var_list.append(list(existing_variation))
                id.append(item.id)
            # print(ex_var_list)

            if product_variation in ex_var_list:
                # print("ache")
                # increase the cart item quantity
                index = ex_var_list.index(product_variation)
                item_id = id[index]
                item = CartItem.objects.get(product=product, id=item_id)
                item.quantity += 1
                item.save()
            else:
                # create a new cart item
                # print("nai")
                # adding the product variations in cartitem 
                item = CartItem.objects.create(product=product, cart=cart, quantity=1)
                if len(product_variation) > 0:
                    item.variations.clear()
                    item.variations.add(*product_variation)
                item.save()
                
        # when there is no cart item(initial add to cart operation)
        else:
            cart_item = CartItem.objects.create(
                product = product,
                quantity = 1,
                cart=cart
            )
            # adding the product variations in cartitem 
            if len(product_variation) > 0:
                cart_item.variations.clear()
                cart_item.variations.add(*product_variation)

            cart_item.save()
        
        # for testing purpose
        # return HttpResponse(cart_item.product)
        # exit()
        return redirect('cart')


def remove_cart(request, product_id, cart_item_id):
    
    product = get_object_or_404(Product, id=product_id)
    try:
        if request.user.is_authenticated:
            cart_item = CartItem.objects.get(product=product, user=request.user, id=cart_item_id)
        else:
            cart = Cart.objects.get(cart_id=_cart_id(request))
            cart_item = CartItem.objects.get(product=product, cart=cart, id=cart_item_id)

        if cart_item.quantity > 1:
            cart_item.quantity -= 1
            cart_item.save()
        else:
            cart_item.delete()
    except:
        pass
    return redirect('cart')

# to delete an item at one go.
def delete_cart(request, product_id, cart_item_id):
    product = get_object_or_404(Product, id=product_id)

    if request.user.is_authenticated:
        cart_item = CartItem.objects.get(product=product, user=request.user, id=cart_item_id)
    else: 
        cart = Cart.objects.get(cart_id=_cart_id(request))
        cart_item = CartItem.objects.get(product=product, cart=cart, id=cart_item_id)
    cart_item.delete()
    
    return redirect('cart')

def cart(request, total=0, quantity=0, cart_items=None):
    tax = 0
    grand_total = 0 
    try:
        # logged in user
        if request.user.is_authenticated:
            cart_items = CartItem.objects.filter(user=request.user, is_active=True)
        # Non logged in user
        else:
            cart = Cart.objects.get(cart_id=_cart_id(request))
            cart_items = CartItem.objects.filter(cart=cart, is_active=True)

        for cart_item in cart_items:
            total += (cart_item.product.price * cart_item.quantity)
            quantity += cart_item.quantity

        tax = (2*total)/100 #considered 2% tax
        grand_total = total+tax

    except Cart.DoesNotExist:
        pass
    context = {
        'total': total, 
        'quantity': quantity,
        'cart_items': cart_items,
        'tax': tax,
        'grand_total': grand_total
        }
    return render(request, 'store/cart.html', context)


@login_required(login_url='login')
def checkout(request, total=0, quantity=0, cart_items=None):
    tax = 0
    grand_total = 0
    try:
        # logged in user
        if request.user.is_authenticated:
            cart_items = CartItem.objects.filter(user=request.user, is_active=True)
        # Non logged in user
        else:
            cart = Cart.objects.get(cart_id=_cart_id(request))
            cart_items = CartItem.objects.filter(cart=cart, is_active=True)

        for cart_item in cart_items:
            total += (cart_item.product.price * cart_item.quantity)
            quantity += cart_item.quantity

        tax = (2*total)/100 #considered 2% tax
        grand_total = total+tax

    except Cart.DoesNotExist:
        pass
    context = {
        'total': total, 
        'quantity': quantity,
        'cart_items': cart_items,
        'tax': tax,
        'grand_total': grand_total
        }
    return render(request, 'store/checkout.html', context)