from django.shortcuts import render

from listings.models import Listing
from farmers.models import Farmer

from listings.choices import price_choices, num_plants

# Create your views here.
def index(request):
    listings = Listing.objects.order_by('-created_date').filter(is_publish=True)[:3]
    context = {
        'listings': listings,
        'price_choices': price_choices,
        'num_plants': num_plants
    }
    return render(request, 'pages/index.html', context)

def about(request):
    # get all farmers
    farmers = Farmer.objects.order_by('-hire_date')

    #get seller of the month
    top_farmer = Farmer.objects.all().filter(seller_month=True)

    context = {
        'farmers': farmers,
        'top_farmer': top_farmer
    }
    return render(request, 'pages/about.html', context)