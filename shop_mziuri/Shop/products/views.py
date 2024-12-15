from django.shortcuts import render
from .models import Product
from django.http import Http404

def home(request):
    products = Product.objects.all()
    return render(request, 'home.html', {'products': products})
def product_detail(request, id):
    try:
        product = Product.objects.get(id=id)
    except Product.DoesNotExist:
        raise Http404("Product not found")
    return render(request, 'product_detail.html', {'product': product})
