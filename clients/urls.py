from . import views
from django.urls import path


urlpatterns = [
    path('', views.ClientsList.as_view(), name='clients'),
    path('<slug:slug>/', views.ClientsDetail.as_view(), name='clients_detail')
]