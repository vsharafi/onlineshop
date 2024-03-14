from django.contrib import admin
from .models import Product, Comment


class CommentInline(admin.TabularInline):
    model = Comment
    fields = ('text', 'user', 'product', 'stars', 'active')
    extra = 0

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'price', 'datetime_created', 'datetime_modified', 'active', )
    inlines = [CommentInline, ]


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('text', 'user', 'product', 'datetime_created', 'datetime_modified', 'stars', 'active')
