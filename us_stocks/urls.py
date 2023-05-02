from django.urls import path
from rest_framework_simplejwt.views import (TokenObtainPairView,
                                            TokenRefreshView)

from . import views

app_name = "us_stocks"

urlpatterns = [
    path('', views.api_overview, name = 'api-overview'),
    path("company/", views.company, name="company"),
    path("company/<str:company_name>/", views.company, name="company_update_delete"),
    path(
        "company-details/<str:company_name>",
        views.company_details,
        name="company-details",
    ),
    path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("add-stock/", views.add_stock, name="add-stock"),
    path(
        "list-stocks/<str:company>/<str:start_date>/<str:end_date>",
        views.list_stocks,
        name="list-stocks",
    ),
]
