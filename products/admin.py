from django.contrib import admin

from products.forms import ColorModelForm
from products.models import CategoryModel, ProductModel, ColorModel, ProductImageModel


@admin.register(CategoryModel)
class CategoryModelAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_at']
    list_filter = ['created_at']
    search_fields = ['title']


@admin.register(ColorModel)
class ColorModelAdmin(admin.ModelAdmin):
    list_display = ['code', 'created_at']
    list_filter = ['created_at']
    search_fields = ['code']
    form = ColorModelForm


class ProductImageStackedInline(admin.StackedInline):
    model = ProductImageModel


@admin.register(ProductModel)
class ProductModelAdmin(admin.ModelAdmin):
    list_display = ['title', 'price', 'discount', 'short_description', 'created_at']
    list_filter = ['category', 'created_at']
    search_fields = ['title', 'short_description']
    autocomplete_fields = ['category', 'colors']
    readonly_fields = ['real_price']
    inlines = [ProductImageStackedInline]
