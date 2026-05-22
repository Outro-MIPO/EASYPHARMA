from django.shortcuts import render
from django.shortcuts import render, redirect
from .models import Reservation  # importe ton modèle



def home(request):
    if request.method == "POST":
        identifiant = request.POST.get("identifiant")
        lieux = request.POST.get("lieux")
        contact = request.POST.get("contact")
        date_evenement = request.POST.get("date_evenement")
        forfait = request.POST.get("forfait")

        # Crée la réservation
        Reservation.objects.create(
            identifiant=identifiant,
            lieux=lieux,
            contact=contact,
            date_evenement=date_evenement,
            forfait=forfait
        )

        return redirect('confirmation')  # tu peux créer cette vue

    # Sinon, GET : afficher la page d'accueil avec le formulaire
    return render(request, 'home.html')
  # page HTML qui hérite de base.html


