from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.create_invoice, name='create_invoice'),
    path('list/', views.invoice_list, name='invoice_list'),
    path('pdf/<int:invoice_id>/', views.generate_pdf, name='generate_pdf'),
    path('register/', views.register, name='register'),
]