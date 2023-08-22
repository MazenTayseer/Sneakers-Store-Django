from django.db import models
from django.contrib.auth.models import User


class Product(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=500, null=True)
    price = models.PositiveIntegerField(null=True)
    quantity = models.PositiveIntegerField(null=True)
    image = models.ImageField(null=True)

    def __str__(self):
        return self.name


class Cart(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    items = models.ManyToManyField(Product)

    def __str__(self):
        return self.user.username + "'s Cart"


class Order(models.Model):
    status = (
        ('Shipped', 'Shipped'),
        ('In Delivery', 'In Delivery'),
    )

    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    items = models.ManyToManyField(Product)

    name = models.CharField(max_length=500, null=True)
    email = models.EmailField(max_length=500, null=True)
    address = models.CharField(max_length=1000, null=True)
    card_number = models.CharField(max_length=16, null=True)
    cvv = models.CharField(max_length=3, null=True)

    shipped = models.CharField(max_length=50, null=True, choices=status)

    def __str__(self):
        return self.user.username + "'s Order"
