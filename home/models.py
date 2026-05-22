from django.db import models

# Create your models here.


class Reservation(models.Model):
    identifiant = models.CharField(max_length=255)
    lieux = models.CharField(max_length=255)
    contact = models.CharField(max_length=20)
    date_evenement = models.DateField()
    forfait = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.identifiant} - {self.lieux} | Contact: {self.contact} | Date: {self.date_evenement} | Forfait: {self.forfait}"
