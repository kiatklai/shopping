from django.shortcuts import render
from productsApp.models import Product
# Create your views here.
def index(request):
  products = Product.objects.filter(isTrending=True)
  return render(request,"index.html",{"products":products})

def productDetail(request,id):
  product=Product.objects.get(pk=id)
  return render(request,"detail.html",{"product":product})

def products(request):
  all_products = Product.objects.all()
  return render(request,"products.html",{"all_products":all_products})