from . import views
from django.urls import path


urlpatterns = [
    path('', views.EquipmentList.as_view(), name='equipment'),
    path('<slug:slug>/', views.EquipmentDetail.as_view(), name='equipment_detail')
]