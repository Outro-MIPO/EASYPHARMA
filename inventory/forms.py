from django import forms
from .models import Pharmacy

class PharmacyForm(forms.ModelForm):
    class Meta:
        model = Pharmacy
        fields = ['name', 'address', 'contact']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nom de la pharmacie'}),
            'address': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Adresse complète'}),
            'contact': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Téléphone ou email'}),
        }


from django import forms
from .models import Medicine

class MedicineForm(forms.ModelForm):
    class Meta:
        model = Medicine
        fields = ['name', 'code', 'expiry_date']
        widgets = {
            'expiry_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'code': forms.TextInput(attrs={'class': 'form-control'}),
        }


from django import forms
from .models import Stock

class StockForm(forms.ModelForm):
    class Meta:
        model = Stock
        fields = ['pharmacy', 'medicine', 'quantity']
        widgets = {
            'pharmacy': forms.Select(attrs={'class': 'form-control'}),
            'medicine': forms.Select(attrs={'class': 'form-control'}),
            'quantity': forms.NumberInput(attrs={'class': 'form-control'}),
        }
