from django.urls import path
from productsApp import views

urlpatterns=[
  path("",views.index)
]