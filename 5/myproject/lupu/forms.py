from django import forms
from .models import VATInvoice, Aktas

class VATInvoiceForm(forms.ModelForm):
    class Meta:
        model = VATInvoice
        fields = ['invoice_number', 'date', 'customer_name', 'quantity', 'price']

class AktasForm(forms.ModelForm):
    class Meta:
        model = Aktas
        fields = ['item_name', 'unit', 'quantity', 'price', 'total_price', 'usage', 'invoice']
