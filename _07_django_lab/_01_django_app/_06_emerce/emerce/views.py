from django.shortcuts import render
from product.models import Product, ReviewRating


# Create your views here.
def home(request):
    products = Product.objects.all().filter(is_available=True).order_by('-created_date')

    # show product rating
    # for product in products:
    #     review = ReviewRating.objects.filter(product_id=product.id, status=True)

    context = {
        'products': products,
        }

    return render(request, 'home.html', context)