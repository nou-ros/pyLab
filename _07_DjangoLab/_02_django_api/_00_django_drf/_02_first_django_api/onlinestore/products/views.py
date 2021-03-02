
from .models import Product, Manufacturer

from django.http import JsonResponse

def product_list(request):
    products = Product.objects.all() #[:30] slice of products
    context = {
        # "products": list(products.values("pk", "name"))
        "products": list(products.values())
    }
    response = JsonResponse(context)
    return response

def product_detail(request, pk):
    try: 
        product = Product.objects.get(pk=pk)
        context = {
            "product": {
                "name": product.name,
                "manufacturer": product.manufacturer.name,
                "description": product.description,
                "photo": product.photo.url,
                "price": product.price,
                "shipping_cost": product.shipping_cost,
                "quantity": product.quantity,
            }
        }
        response = JsonResponse(context)
    except Product.DoesNotExist:
        response = JsonResponse({
            "error": {
                "code": 404,
                "message": "product not found"
            }
        }, status=404)

    return response

# the real logic behind the restapi with JsonResponse in the above. But all this can be avoided with django serializers.

# from django.views.generic.detail import DetailView
# from django.views.generic.list import ListView

# # class ProductListView(ListView):
# #     model = Product
# #     template_name = "products/product_list.html"

# # # Create your views here.
# # class ProductDetailView(DetailView):
# #     model = Product
# #     template_name = "products/product_detail.html"