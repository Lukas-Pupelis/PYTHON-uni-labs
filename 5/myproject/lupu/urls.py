from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.create_invoice, name='create_invoice'),
    path('list/', views.invoice_list, name='invoice_list'),
    path('pdf/<int:invoice_id>/', views.generate_pdf, name='generate_pdf'),
    path('register/', views.register, name='register'),
    path('create_aktas/', views.create_aktas, name='create_aktas'),
    path('aktas_list/', views.aktas_list, name='aktas_list'),
    path('aktas_pdf/<int:aktas_id>/', views.generate_aktas_pdf, name='generate_aktas_pdf'),
]