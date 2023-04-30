from django.db import models

# Create your models here.


class Company(models.Model):
    ticker = models.CharField(max_length=100, primary_key=True, blank=False, null=False)
    company = models.CharField(max_length=100, blank=False, null=False)
    industry = models.CharField(max_length=100, blank=False, null=False)
    sector = models.CharField(max_length=100)
    address = models.CharField(max_length=250)

    def __str__(self):
        return self.company


class StockPrice(models.Model):
    company = models.ForeignKey(
        Company, on_delete=models.CASCADE, verbose_name="ticker"
    )
    date = models.DateField(blank=False, null=False)
    open = models.FloatField(default=None)
    close = models.FloatField(default=None)
    volume = models.IntegerField(default=None)

    def __str__(self):
        return str(self.company) + "_stocks"
