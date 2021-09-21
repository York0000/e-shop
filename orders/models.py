from django.contrib.auth import get_user_model
from django.db import models

from products.models import ProductModel

UserModel = get_user_model()


class OrderModel(models.Model):
    user = models.ForeignKey(UserModel, related_name='orders', on_delete=models.CASCADE)
    products = models.ManyToManyField(ProductModel, related_name='order')
    price = models.FloatField(null=True)

    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    company_name = models.CharField(max_length=50, null=True, blank=True)
    country = models.CharField(max_length=50)
    street_address1 = models.CharField(max_length=100)
    street_address2 = models.CharField(max_length=100, null=True, blank=True)
    city = models.CharField(max_length=30)
    state = models.CharField(max_length=30)
    phone = models.CharField(max_length=20)
    email = models.EmailField()

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.user)

    class Meta:
        verbose_name = 'order'
        verbose_name_plural = 'orders'
