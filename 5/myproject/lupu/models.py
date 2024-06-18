# lupu/models.py
from django.db import models
from django.contrib.auth.models import User

class VATInvoice(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    invoice_number = models.CharField(max_length=50)
    date = models.DateField()
    customer_name = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField()

    @property
    def price(self):
        return self.amount / self.quantity

class Aktas(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    item_name = models.CharField(max_length=100)
    unit = models.CharField(max_length=20)
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    usage = models.TextField()
    invoice = models.ForeignKey(VATInvoice, on_delete=models.CASCADE)

    def __str__(self):
        return self.item_name
