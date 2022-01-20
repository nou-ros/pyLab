from django.shortcuts import render, HttpResponse, redirect
from .models import Product 
from .forms import ProductForm

# Create your views here.
def list_product(request):
    products=Product.objects.all()
    return render(request, 'product/product.html', {"products": products})

def create_product(request):
    form = ProductForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('list')

    return render(request, 'product/products-form.html', {'form': form})

def update_product(request, id):
    product = Product.objects.get(pk=id)
    form = ProductForm(request.POST or None, instance=product)

    if form.is_valid():
        form.save()
        return redirect('list')

    return render(request, 'product/update.html', {'form': form, 'product': product})

def delete_product(request, id):
    product=Product.objects.get(pk=id)
    if request.method == 'POST':
        product.delete()
        return redirect('list')

    return render(request, 'product/delete.html', {'product': product})