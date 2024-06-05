from django.shortcuts import render

# Create your views here.

from django.shortcuts import render, redirect
from .forms import VATInvoiceForm
from .models import VATInvoice
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login as auth_login

@login_required
def create_invoice(request):
    if request.method == 'POST':
        form = VATInvoiceForm(request.POST)
        if form.is_valid():
            invoice = form.save(commit=False)
            invoice.user = request.user
            invoice.save()
            return redirect('invoice_list')
    else:
        form = VATInvoiceForm()
    return render(request, 'lupu/create_invoice.html', {'form': form})

@login_required
def invoice_list(request):
    invoices = VATInvoice.objects.filter(user=request.user)
    return render(request, 'lupu/invoice_list.html', {'invoices': invoices})

@login_required
def generate_pdf(request, invoice_id):
    invoice = VATInvoice.objects.get(id=invoice_id)
    template_path = 'lupu/invoice_pdf.html'
    context = {'invoice': invoice}
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="invoice_{invoice_id}.pdf"'
    template = get_template(template_path)
    html = template.render(context)
    pisa_status = pisa.CreatePDF(html, dest=response)
    if pisa_status.err:
        return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('create_invoice')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})