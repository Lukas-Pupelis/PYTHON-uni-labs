from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login as auth_login
from .forms import VATInvoiceForm, AktasForm
from .models import VATInvoice, Aktas
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('invoice_list')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

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
    return render(request, 'create_invoice.html', {'form': form})

@login_required
def update_invoice(request, pk):
    invoice = get_object_or_404(VATInvoice, pk=pk)
    if request.method == 'POST':
        form = VATInvoiceForm(request.POST, instance=invoice)
        if form.is_valid():
            form.save()
            return redirect('invoice_list')
    else:
        form = VATInvoiceForm(instance=invoice)
    return render(request, 'update_invoice.html', {'form': form})

@login_required
def invoice_list(request):
    invoices = VATInvoice.objects.filter(user=request.user)
    return render(request, 'invoice_list.html', {'invoices': invoices})

@login_required
def create_aktas(request):
    aktas = Aktas.objects.create(
        user=request.user,
        item_name="Default Item",  # Set a default item name
        unit="vnt",  # Set a default unit
        quantity=1,  # Set a default quantity
        price=0,  # Set a default price
        total_price=0,  # Set a default total price
        usage="Default Usage",  # Set a default usage
        invoice=VATInvoice.objects.filter(user=request.user).first()  # Link to the first VAT invoice
    )
    return redirect('aktas_list')

@login_required
def update_aktas(request, pk):
    aktas = get_object_or_404(Aktas, pk=pk)
    if request.method == 'POST':
        form = AktasForm(request.POST, instance=aktas)
        if form.is_valid():
            form.save()
            return redirect('aktas_list')
    else:
        form = AktasForm(instance=aktas)
    return render(request, 'update_aktas.html', {'form': form})

@login_required
def aktas_list(request):
    aktai = Aktas.objects.filter(user=request.user)
    return render(request, 'aktas_list.html', {'aktai': aktai})

@login_required
def invoice_pdf(request, pk):
    invoice = get_object_or_404(VATInvoice, pk=pk)
    template_path = 'invoice_pdf.html'
    context = {'invoice': invoice}
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="invoice_{invoice.pk}.pdf"'
    template = get_template(template_path)
    html = template.render(context)
    pisa_status = pisa.CreatePDF(html, dest=response)
    if pisa_status.err:
        return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response

@login_required
def invoice_details(request, pk):
    invoice = get_object_or_404(VATInvoice, pk=pk)
    return render(request, 'invoice_details.html', {'invoice': invoice})

@login_required
def aktas_details(request, pk):
    aktas = get_object_or_404(Aktas, pk=pk)
    return render(request, 'aktas_details.html', {'aktas': aktas})

from decimal import Decimal

@login_required
def aktas_pdf(request, pk):
    aktas = get_object_or_404(Aktas, pk=pk)
    vat_invoices = VATInvoice.objects.filter(user=request.user)
    
    vat_rate = Decimal('1.21')
    
    for invoice in vat_invoices:
        invoice.suma_su_pvm = invoice.quantity * invoice.price * vat_rate

    template_path = 'aktas_pdf.html'
    context = {'aktas': aktas, 'vat_invoices': vat_invoices}
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="aktas_{aktas.pk}.pdf"'
    template = get_template(template_path)
    html = template.render(context)
    pisa_status = pisa.CreatePDF(html, dest=response)
    if pisa_status.err:
        return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response
