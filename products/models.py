from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


UserModel = get_user_model()


class CategoryModel(models.Model):
    title = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'


class ColorModel(models.Model):
    code = models.CharField(max_length=10)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.code

    class Meta:
        verbose_name = 'color'
        verbose_name_plural = 'colors'


class ProductModel(models.Model):
    title = models.CharField(max_length=255, db_index=True)
    image = models.ImageField(upload_to='products')
    price = models.FloatField()
    discount = models.PositiveSmallIntegerField(
        default=0,
        validators=[
            MinValueValidator(0),
            MaxValueValidator(100)
        ]
    )
    short_description = models.TextField()
    long_description = RichTextUploadingField()
    category = models.ForeignKey(
        CategoryModel,
        on_delete=models.PROTECT,
        related_name='products'
    )
    real_price = models.FloatField(default=0)
    colors = models.ManyToManyField(ColorModel, related_name='products')
    wishlist = models.ManyToManyField(UserModel, related_name='wishlist')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    @staticmethod
    def get_from_cart(request):
        cart = request.session.get('cart', [])
        return ProductModel.objects.filter(
            pk__in=cart
        )

    def is_discount(self):
        return self.discount != 0

    class Meta:
        verbose_name = 'product'
        verbose_name_plural = 'products'


class ProductImageModel(models.Model):
    product = models.ForeignKey(ProductModel, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='products')

    def __str__(self):
        return self.product.title

    class Meta:
        verbose_name = 'product image'
        verbose_name_plural = 'product images'
