from django import forms
from .models import VATInvoice

class VATInvoiceForm(forms.ModelForm):
    class Meta:
        model = VATInvoice
        fields = ['invoice_number', 'date', 'customer_name', 'amount', 'quantity']