from django.db import models

class Pharmacy(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    contact = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Medicine(models.Model):
    name = models.CharField(max_length=255)
    code = models.CharField(max_length=50, unique=True)
    expiry_date = models.DateField()

    def __str__(self):
        return f"{self.name} ({self.code})"


class Stock(models.Model):
    pharmacy = models.ForeignKey(Pharmacy, on_delete=models.CASCADE)
    medicine = models.ForeignKey(Medicine, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.pharmacy.name} - {self.medicine.name}"