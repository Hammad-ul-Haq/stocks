from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from .models import Company, StockPrice
from .serializers import StockPriceSerializer
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import AccessToken


class AddStockTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        # creating new user
        user_name = "test_user"
        user_email = "test@stocks.com"
        user_password = "asdfqwer"
        user = User.objects.create_user(username=user_name, email=user_email)
        user.set_password(user_password)
        user.save()

        # Generate a JWT token for the user
        token = AccessToken.for_user(user)

        # Store the token in the user's model
        user.auth_token = str(token)
        user.save()

        # Authenticate the user using the token
        self.client.credentials(HTTP_AUTHORIZATION="Bearer " + str(token))
        # create test payload
        #
        self.valid_add_company_payload = {
            "ticker": "1234",
            "company": "test_company",
            "industry": "mobile",
            "sector": "H",
            "address": "china",
        }

        self.invalid_add_company_payload = {
            "ticker": "1234",
            "company": "test_company",
            "industry": "mobile",
            "sector": "H",
            "address": "china",
        }

        self.valid_add_stock_payload = {
            "date": "2022-08-11",
            "company": "test_company",
            "open": 160.0,
            "close": 180.0,
            "volume": 10052,
        }
        self.invalid_add_stock_payload = {
            "company": "Microsoft",
            "price": -12.34,
            "date": "2022-01-01",
        }

        self.valid_update_company_payload = {
            "company": "Microsoft",
            "price": -12.34,
            "date": "2022-01-01",
        }

    def test_add_valid_company(self):
        response = self.client.post(
            reverse("us_stocks:company"),
            data=self.valid_add_company_payload,
            format="json",
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Company.objects.count(), 1)
        self.assertEqual(Company.objects.get().ticker, "1234")

    def test_add_invalid_company(self):
        response = self.client.post(
            reverse("us_stocks:company"),
            data=self.invalid_add_stock_payload,
            format="json",
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(Company.objects.count(), 0)

    def test_add_valid_stock(self):
        self.company = Company.objects.create(company="test_company")
        response = self.client.post(
            reverse("us_stocks:add-stock"),
            data=self.valid_add_stock_payload,
            format="json",
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(StockPrice.objects.count(), 1)
        self.assertEqual(StockPrice.objects.get().volume, 10052)

    def test_add_invalid_stock(self):
        response = self.client.post(
            reverse("us_stocks:add-stock"),
            data=self.invalid_add_stock_payload,
            format="json",
        )
        self.assertEqual(
            response.status_code,
            status.HTTP_404_NOT_FOUND or status.HTTP_400_BAD_REQUEST,
        )
        self.assertEqual(StockPrice.objects.count(), 0)
