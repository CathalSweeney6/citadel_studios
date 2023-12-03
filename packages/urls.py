from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_products, name='packages'),
    path('<product_id>', views.product_detail, name='product_detail'),
]