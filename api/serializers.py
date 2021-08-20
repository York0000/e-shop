from rest_framework import serializers

from products.models import ProductModel, CategoryModel, ColorModel


class CategoryModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryModel
        fields = '__all__'


class ColorModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = ColorModel
        fields = '__all__'


class ProductModelSerializer(serializers.ModelSerializer):
    category = CategoryModelSerializer()
    colors = ColorModelSerializer(many=True)

    class Meta:
        model = ProductModel
        exclude = [
            'long_description',
            'wishlist',
        ]
