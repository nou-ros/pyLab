from django.shortcuts import get_object_or_404, redirect, render

from .models import Product, ProductGallery, ReviewRating
from category.models import Category
from carts.models import CartItem
from carts.views import _cart_id

from django.core.paginator import Paginator
# Create your views here.

from orders.models import OrderProduct

from .forms import ReviewForm

from django.contrib import messages
from django.db.models import Q


def store(request, category_slug=None):
    categories = None
    products = None

    # serve products by category
    if category_slug != None:
        categories = get_object_or_404(Category, slug=category_slug)
        products = Product.objects.all().filter(category=categories, is_available=True)
        product_count = products.count()
    # serve products without category
    else:
        products = Product.objects.all().filter(is_available=True).order_by('-created_date')
        product_count = products.count()

    paginator = Paginator(products, 2) # number of products we want in each page
    #store/?page=2
    page = request.GET.get('page')
    paged_products = paginator.get_page(page) # this will contain 5 products now


    context = {
        'products': paged_products, 
        'product_count': product_count
        
        }

    return render(request, 'store/store.html', context)

def product_detail(request, category_slug, product_slug):
    try:
        # fetch the product by matching category slug and product slug
        single_product = Product.objects.get(category__slug=category_slug, slug=product_slug)
        # checking if the product resides inside cart(to perform added to cart)
        in_cart = CartItem.objects.filter(cart__cart_id=_cart_id(request), product=single_product).exists()
    except Exception as e:
        raise e

    # user is authenticated then perform
    if request.user.is_authenticated:
        # let a user review on the product if he/she has bought the product.
        try:
            ordered_product = OrderProduct.objects.filter(user=request.user, product_id=single_product.id).exists()
            
        except OrderProduct.DoesNotExist:
            ordered_product = None
    else:
        ordered_product = None 
        
    # get the rating with the product id and true status(false will not let the reviews to show) reviews 
    reviews = ReviewRating.objects.filter(product_id=single_product.id, status=True)

    
    # product gallery
    product_gallery = ProductGallery.objects.filter(product_id=single_product.id)

    context = {
            'single_product': single_product,
            'in_cart': in_cart,
            'ordered_product': ordered_product, 
            'reviews': reviews, 
            'product_gallery': product_gallery
        }    
    return render(request, 'store/product_detail.html', context) 


def search(request):
    products = 0 
    product_count = 0 
    if 'keyword' in request.GET:
        #taking the keyword's value
        keyword = request.GET['keyword']
        if keyword:
            # Q for or opeartions in django filter follow doc
            products = Product.objects.order_by('-created_date').filter(Q(description__icontains=keyword) | Q(product_name__icontains = keyword))

        products = products
        product_count = products.count()
    
    context = {
        'products': products,
        'product_count': product_count
    }
    return render(request, 'store/store.html', context)  



def review(request, product_id):

    # to store prev url
    url = request.META.get('HTTP_REFERER')

    if request.method == 'POST':
        
        try: 
            reviews = ReviewRating.objects.get(user__id=request.user.id, product__id=product_id)
            # to update already presented review
            form = ReviewForm(request.POST, instance=reviews)
            form.save()
            messages.success(request, 'Thank you! Your review has been updated.')
            return redirect(url)

        except ReviewRating.DoesNotExist:
            form = ReviewForm(request.POST)

            if form.is_valid():
                data = ReviewRating()
                data.subject = form.cleaned_data['subject']
                data.rating = form.cleaned_data['rating']
                data.review = form.cleaned_data['review']
                data.ip = request.META.get('REMOTE_ADDR')
                data.product_id = product_id
                data.user_id = request.user.id
                data.save()
                messages.success(request, 'Thank you! Your review has been submitted.')
                return redirect(url)


                