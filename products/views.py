from django.views.generic import ListView, DetailView, CreateView
from .forms import CommentForm
from .models import Product, Comment
from django.shortcuts import render, get_object_or_404, reverse, redirect


class ProductListView(ListView):
    template_name = 'products/product_list.html'
    context_object_name = 'products'
    queryset = Product.objects.filter(active=True).order_by('-datetime_created')


def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    # comments = Comment.active_comments.all()
    comments = Comment.objects.all()
    comment = CommentForm()
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.product = product
            comment.user = request.user
            comment.save()
            return redirect('product_detail', pk=product.pk)
    return render(request, 'products/product_detail.html', {'product': product, 'form': comment, 'comments': comments})


# class ProductDetailView(DetailView):
#     template_name = 'products/product_detail.html'
#     model = Product
#     context_object_name = 'product'
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['form'] = CommentForm()
#         comments = Comment.objects.filter(product_id=self.kwargs['pk'])
#         context['comments'] = comments
#         return context


# class CommentCreateView(CreateView):
#     model = Comment
#     form_class = CommentForm
#
#
#     def form_valid(self, form):
#         obj = form.save(commit=False)
#         obj.user = self.request.user
#         product_id = int(self.kwargs['pk'])
#         product = get_object_or_404(Product, pk=product_id)
#         obj.product = product
#         return super().form_valid(form)
#
#     def success_url(self):
#         return reverse('product_detail', args=[self.object.pk])




# class ProductDetailView(DetailView):
#     template_name = 'products/product_detail.html'
#     model = Product
#     context_object_name = 'product'
#     form_class = CommentForm
#
#     # def form_valid(self, form):
#     #     product_id = int(self.kwargs['pk'])
#     #     obj = form.save(commit=False)
#     #     obj.product = get_object_or_404(Product, pk=product_id)
#     #     obj.user = self.request.user
#     #     return super().form_valid(form)
#
#     def post(self, request, *args, **kwargs):
#         form = CommentForm(request.POST)
#         obj = form.save(commit=False)
#         obj.product = get_object_or_404(Product, pk=self.kwargs.get('pk'))
#         obj.user = self.request.user
#         return render(request, self.template_name, {'form':form, })
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         comments = Comment.objects.filter(product_id=self.kwargs['pk'])
#         context['form'] = CommentForm()
#         context['comments'] = comments
#         return context
#
#     def success_url(self):
#         return reverse('product_detail', args=[self.object.pk])

