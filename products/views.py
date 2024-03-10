from django.views.generic import ListView, DetailView
from products.models import Product


class ProductListView(ListView):
    template_name = 'products/product_list.html'
    context_object_name = 'products'
    queryset = Product.objects.filter(active=True).order_by('-datetime_created')


class ProductDetailView(DetailView):
    model = Product
    template_name = 'products/product_detail.html'
    context_object_name = 'product'
