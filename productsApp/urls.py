from django.urls import path
from productsApp import views

urlpatterns=[
  path("",views.index),
  path("product/details/<int:id>",views.productDetail,name="productDetail"),
  path("products",views.products)
]