from django.db import models

# Create your models here.

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
