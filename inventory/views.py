from django.shortcuts import render
from .models import Pharmacy, Medicine, Stock
import pandas as pd
import numpy as np
from django.shortcuts import render, redirect


from django.shortcuts import render
from .models import Pharmacy, Medicine, Stock  # ← Assure-toi d'importer Stock ici

from datetime import date

from datetime import date
from django.shortcuts import render
from .models import Pharmacy, Medicine, Stock
from collections import Counter

from datetime import date
from collections import Counter
import numpy as np
from sklearn.linear_model import LinearRegression
from django.shortcuts import render
from .models import Stock, Pharmacy

def dashboard(request):
    stocks = Stock.objects.select_related('pharmacy', 'medicine')

    alerts = []
    for stock in stocks:
        # 1️⃣ Vérification des ruptures de stock
        predicted_days = stock.quantity / 3
        if predicted_days <= 2:
            status_stock = 'rupture'
        elif predicted_days <= 5:
            status_stock = 'attention'
        else:
            status_stock = 'normal'

        # 2️⃣ Vérification de la date de péremption
        days_left = (stock.medicine.expiry_date - date.today()).days
        if days_left < 0:
            status_expiry = 'périmé'
        elif days_left <= 7:
            status_expiry = 'bientôt périmé'
        else:
            status_expiry = 'valide'

        # 3️⃣ Ajouter l'alerte
        alerts.append({
            'pharmacy': stock.pharmacy.name,
            'medicine': stock.medicine.name,
            'quantity': stock.quantity,
            'status_stock': status_stock,
            'status_expiry': status_expiry,
            'expiry_date': stock.medicine.expiry_date
        })

    pharmacies = Pharmacy.objects.all()

    # ⚡ Comptage des alertes pour graphique
    counter = Counter([alert['status_stock'] for alert in alerts])
    alert_counts = {
        'rupture': counter.get('rupture', 0),
        'attention': counter.get('attention', 0),
        'normal': counter.get('normal', 0),
    }

    # ⚡ Stocks par pharmacie pour graphique
    stock_counts = {p.name: stocks.filter(pharmacy=p).count() for p in pharmacies}

    # ⚡ Régression linéaire sur les produits bientôt périmés
    # Compter les produits périmant dans chaque mois
    expiry_dates = [s.medicine.expiry_date for s in stocks]
    expiry_months = [d.month for d in expiry_dates]  # 1 à 12
    month_labels = list(range(1, 13))
    month_counts = [expiry_months.count(m) for m in month_labels]

    # Calcul de la régression
    X = np.array(month_labels).reshape(-1, 1)
    y = np.array(month_counts)
    model = LinearRegression()
    model.fit(X, y)
    regression_values = model.predict(X).tolist()

    context = {
        'stocks': stocks,
        'alerts': alerts,
        'pharmacies': pharmacies,
        'alert_counts': alert_counts,
        'stock_counts': stock_counts,
        'labels': month_labels,              # pour le graphique
        'values': month_counts,              # nombre de produits périmant par mois
        'regression_values': regression_values  # ligne de tendance
    }
    return render(request, 'inventory/dashboard.html', context)






def pharmacy_list(request):
    pharmacies = Pharmacy.objects.all()
    return render(request, 'inventory/pharmacies.html', {'pharmacies': pharmacies})


def medicine_list(request):
    medicines = Medicine.objects.all()
    return render(request, 'inventory/medicines.html', {'medicines': medicines})



from .forms import PharmacyForm

def add_pharmacy(request):
    if request.method == 'POST':
        form = PharmacyForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('pharmacies')
    else:
        form = PharmacyForm()
    return render(request, 'inventory/add_pharmacy.html', {'form': form})



from .models import Medicine
from .forms import MedicineForm

def add_medicine(request):
    if request.method == 'POST':
        form = MedicineForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('medicines')  # redirige vers la liste des médicaments
    else:
        form = MedicineForm()
    return render(request, 'inventory/add_medicine.html', {'form': form})


from .forms import StockForm

def add_stock(request):
    if request.method == 'POST':
        form = StockForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')  # redirige vers ton dashboard
    else:
        form = StockForm()
    return render(request, 'inventory/add_stock.html', {'form': form})


from django.shortcuts import get_object_or_404

def edit_stock(request, stock_id):
    stock = get_object_or_404(Stock, id=stock_id)
    if request.method == 'POST':
        form = StockForm(request.POST, instance=stock)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = StockForm(instance=stock)
    return render(request, 'inventory/edit_stock.html', {'form': form})



def delete_stock(request, stock_id):
    stock = get_object_or_404(Stock, id=stock_id)
    if request.method == 'POST':
        stock.delete()
        return redirect('dashboard')
    return render(request, 'inventory/delete_stock.html', {'stock': stock})


