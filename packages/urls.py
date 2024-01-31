from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_products, name='packages'),
    path('<int:product_id>/', views.product_detail, name='product_detail'),
    path('add/', views.add_product, name='add_product'),
    path('edit/<int:product_id>/', views.edit_product, name='edit_product'),
    path('delete/<int:product_id>/', views.delete_product, name='delete_product'),
    path('delete_user_review/<int:review_id>',
         views.delete_user_review, name='delete_user_review'),
    path('edit_user_review/<int:pk>', views.EditReview.as_view(),
    name='edit_user_review')
]