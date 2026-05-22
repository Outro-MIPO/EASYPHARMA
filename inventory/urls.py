from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('pharmacies/', views.pharmacy_list, name='pharmacies'),
    path('medicines/', views.medicine_list, name='medicines'),
    path('pharmacies/add/', views.add_pharmacy, name='add_pharmacy'),
    path('medicines/add/', views.add_medicine, name='add_medicine'),
    path('stocks/add/', views.add_stock, name='add_stock'),
    # Modifier un stock
    path('stocks/edit/<int:stock_id>/', views.edit_stock, name='edit_stock'),
    
    # Supprimer un stock
    path('stocks/delete/<int:stock_id>/', views.delete_stock, name='delete_stock'),
    

]