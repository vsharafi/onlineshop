from django.urls import path
from .views import ProductListView, product_detail, test_translation

urlpatterns = [
    path('', ProductListView.as_view(), name='product_list'),
    path('<int:pk>/', product_detail, name='product_detail'),
    path('hello/', test_translation, name='hello'),

]