from rest_framework import serializers
from .models import Category, LinkMapper, Product, LinkStats

class CategorySerializer(serializers.ModelSerializer):  # create class to serializer model
    class Meta:
        model = Category
        fields = '__all__'

class LinkMapperSerializer(serializers.ModelSerializer):  # create class to serializer model
    class Meta:
        model = LinkMapper
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):  # create class to serializer model
    class Meta:
        model = Product
        fields = '__all__'

class LinkStatsSerializer(serializers.ModelSerializer):  # create class to serializer model
    class Meta:
        model = LinkStats
        fields = '__all__'
