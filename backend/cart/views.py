from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from products.models import Product
from .models import Cart,Cartitem
from .serializers import CartSerializer
# Create your views here.

class addcart(APIView):
    def post(self,request):
        user = request.data['user']
        pid = request.data['product_id']
        qty = request.data['qty']
        product = Product.objects.get(id=pid)
        if product.stock < qty:
            return Response({"error": "Out of stock"})
        product.stock -= qty
        product.save()
        cart, _ = Cart.objects.get_or_create(user_id=user)
        Cartitem.objects.create(cart=cart, product=product, quantity=qty)
        return Response({"msg": "Added"})
class viewcart(APIView):
    def get(self,request):
        cart=Cartitem.objects.all()
        s_obj=CartSerializer(cart,many=True)
        return Response(s_obj.data)