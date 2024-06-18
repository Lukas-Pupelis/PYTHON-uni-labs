from django.db import models
from django.contrib.auth.models import User

class VATInvoice(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    invoice_number = models.CharField(max_length=255)
    date = models.DateField()
    customer_name = models.CharField(max_length=255)
    quantity = models.IntegerField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.invoice_number

class Aktas(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    item_name = models.CharField(max_length=255, default="Default Item")
    unit = models.CharField(max_length=50, default="vnt")
    quantity = models.IntegerField(default=1)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    usage = models.CharField(max_length=255, default="Default Usage")
    invoice = models.ForeignKey(VATInvoice, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.item_name
