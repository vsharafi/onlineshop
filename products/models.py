from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _


class Product(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.PositiveIntegerField(default=0)
    active = models.BooleanField(default=True)
    datetime_created = models.DateTimeField(auto_now_add=True)
    datetime_modified = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        return reverse('product_detail', args=[self.pk])

    def __str__(self):
        return self.title


class ActiveCommentManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(active=True)


class Comment(models.Model):
    CHOICES = [(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')]
    text = models.TextField(verbose_name=_('Comment Text'))
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='comments')
    datetime_created = models.DateTimeField(auto_now_add=True)
    datetime_modified = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='comments')
    stars = models.PositiveIntegerField(default=0, choices=CHOICES, verbose_name=_('Stars'))
    active = models.BooleanField(default=True)

    objects = models.Manager()
    active_comments = ActiveCommentManager()

    def __str__(self):
        return self.text
