from django.urls import path
from .views import ProductListView, product_detail

urlpatterns = [
    path('', ProductListView.as_view(), name='product_list'),
    path('<int:pk>/', product_detail, name='product_detail'),
]