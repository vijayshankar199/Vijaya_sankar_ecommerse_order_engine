from rest_framework import serializers
from .models import Cartitem

class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cartitem
        fields = '_all_'