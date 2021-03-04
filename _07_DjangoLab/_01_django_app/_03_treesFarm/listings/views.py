from django.shortcuts import render, get_object_or_404
from .models import Listing
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .choices import price_choices, num_plants

# Create your views here.
def index(request):
    
    listings = Listing.objects.order_by('-created_date').filter(is_publish=True)

    # pagination with django paginator
    paginator = Paginator(listings, 6)
    #the url parameter we are seeking
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)

    context = {'listings': paged_listings}
    
    return render(request, 'listings/listings.html', context)

def details(request, listing_id):
    listing = get_object_or_404(Listing, pk=listing_id)
    context = {
        'listing':listing
    }
    return render(request, 'listings/details.html', context)

def search(request):
    queries = Listing.objects.order_by('-created_date')

    #keywords
    if 'keywords' in request.GET: 
        keywords = request.GET['keywords']
        if keywords:
            queries = queries.filter(description__icontains=keywords)
    # plants 
    if 'plants' in request.GET: 
        plants = request.GET['plants']
        if plants:
            queries = queries.filter(plants__lte=plants)
    # price 
    if 'price' in request.GET: 
        price = request.GET['price']
        if price:
            queries = queries.filter(price__lte=price)

    # with this keywords will remain in the search box
    values = request.GET

    context = {
        'price_choices': price_choices,
        'num_plants': num_plants, 
        'listings': queries,
        'values': values
    }
    return render(request, 'listings/search.html', context)