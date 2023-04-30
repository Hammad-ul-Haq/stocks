from django.contrib import admin
from .models import Company, StockPrice
# Register your models here.

class CompanyAdmin(admin.ModelAdmin):
    list_display = ("ticker", "company", "industry", "sector", "address")

class StockPriceAdmin(admin.ModelAdmin):
    list_display = ("company", "date","open","close","volume")


admin.site.register(Company, CompanyAdmin)
admin.site.register(StockPrice, StockPriceAdmin)
