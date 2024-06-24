from django.db import models

# Create your models here.

class SalesData(models.Model):
    sale_date = models.DateField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.sale_date} - {self.amount}"