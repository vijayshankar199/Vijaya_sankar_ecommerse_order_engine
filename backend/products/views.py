from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Product
from .serializers import ProductSerializer
from rest_framework.status import HTTP_200_OK
# Create your views here.

class addproduct(APIView):
    def get(self,request):
        p_obj=Product.objects.all()
        s_obj=ProductSerializer(p_obj,many=True)
        return Response(s_obj.data)
    def post(self,request):
        s_obj=ProductSerializer(data=request.data)
        if s_obj.is_valid():
            s_obj.save()
            return Response(status=HTTP_200_OK)
        else:
            return Response(s_obj.errors)