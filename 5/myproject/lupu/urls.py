from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.create_invoice, name='create_invoice'),
    path('<int:pk>/update/', views.update_invoice, name='update_invoice'),
    path('pdf/<int:pk>/', views.invoice_pdf, name='invoice_pdf'),
    path('list/', views.invoice_list, name='invoice_list'),
    path('<int:pk>/', views.invoice_details, name='invoice_details'),
    path('<int:pk>/invoice/create/', views.create_aktas, name='create_aktas'),
    path('invoice/<int:pk>/update/', views.update_aktas, name='update_aktas'),
    path('register/', views.register, name='register'),
    path('aktas/create/', views.create_aktas, name='create_aktas'),
    path('aktas/list/', views.aktas_list, name='aktas_list'),
    path('aktas/<int:pk>/update/', views.update_aktas, name='update_aktas'),
    path('aktas/<int:pk>/', views.aktas_details, name='aktas_details'),
    path('aktas/pdf/<int:pk>/', views.aktas_pdf, name='aktas_pdf'),
]