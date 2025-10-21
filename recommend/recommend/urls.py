
from django.contrib import admin
from django.urls import path
from home.views import *

urlpatterns = [
    path('',index),
    path('product_detail/<id>/', product_detail),
    path('admin/', admin.site.urls),
    path('products/',ProductsAPI.as_view()),
    path('product/<id>/',ProductDetailAPI.as_view()),
]