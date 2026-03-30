from django.db import models

class Order(models.Model):
    STATUS_CHOICES = [
        ('CREATED', 'CREATED'),
        ('PENDING_PAYMENT', 'PENDING_PAYMENT'),
        ('PAID', 'PAID'),
        ('FAILED', 'FAILED'),
        ('CANCELLED', 'CANCELLED'),
    ]

    user_id = models.CharField(max_length=50)
    total = models.FloatField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)