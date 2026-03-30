from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from cart.models import Cart, Cartitem
from .models import Order
import random
# Create your views here.

class place_order(APIView):
    def post(self,request):
        user = request.data['user']
        coupon = request.data.get('coupon')

        cart = Cart.objects.get(user_id=user)
        items = Cartitem.objects.filter(cart=cart)

        total = sum(i.product.price * i.quantity for i in items)

        # Coupon logic
        if coupon == "SAVE10":
            total *= 0.9
        elif coupon == "FLAT200":
            total -= 200

        order = Order.objects.create(user_id=user, total=total, status='PENDING')

        if random.choice([True, False]):
            order.status = 'PAID'
            items.delete()
        else:
            order.status = 'FAILED'

            # rollback
            for i in items:
                p = i.product
                p.stock += i.quantity
                p.save()

        order.save()

        return Response({"status": order.status})