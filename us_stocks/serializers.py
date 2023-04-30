from rest_framework import serializers

from .models import Company, StockPrice


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = "__all__"


class StockPriceSerializer(serializers.ModelSerializer):
    company = serializers.CharField(source="company.company")

    class Meta:
        model = StockPrice
        fields = ("date", "company", "open", "close", "volume")
