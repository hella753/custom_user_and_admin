from django.db import models
from user.models import User


class Order(models.Model):
    AVAILABLE_STATUSES = [
        ("P", "Pending"),
        ("S", "Shipped"),
        ("D", "Delivered")
    ]

    order_date = models.DateField("შეკვეთის თარიღი", auto_now_add=True)
    order_status = models.CharField(
        "სტატუსი",
        max_length=100,
        default="Pending",
        choices=AVAILABLE_STATUSES
    )
    product = models.ForeignKey(
        "store.Product",
        on_delete=models.CASCADE,
        verbose_name="პროდუქტი"
    )
    product_quantity = models.PositiveIntegerField("რაოდენობა")
    # order_customer = models.ForeignKey(
    #     User,
    #     on_delete=models.CASCADE,
    #     verbose_name="მომხმარებელი"
    # )
    order_address = models.CharField(max_length=100, verbose_name="მისამართი")

    def __str__(self):
        return f"Order {self.id} | status {self.order_status}"


class UserCart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name="მომხმარებელი" )

    def __str__(self):
        return f"{self.id}"