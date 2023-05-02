from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

from .models import Company, StockPrice
from .serializers import CompanySerializer, StockPriceSerializer


@api_view(["GET", "POST", "PUT", "DELETE"])
@permission_classes([IsAuthenticated])
def company(request, company_name=None):
    """
    Perform CRUD operations on a Company.

    :param request: The incoming HTTP request.
    :type request: django.http.HttpRequest

    :param company_name: The name of the company to perform operations on.
    :type company_name: str

    :return: The HTTP response containing the data and status code.
    :rtype: rest_framework.response.Response
    """

    if request.method == "GET":
        companies = Company.objects.all()
        serializer = CompanySerializer(companies, many=True)
        return Response(serializer.data)

    if request.method == "POST":
        serializer = CompanySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == "PUT":
        object = get_object_or_404(Company, company=company_name)
        serializer = CompanySerializer(data=request.data, instance=object)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == "DELETE":
        try:
            del_company = Company.objects.get(company=company_name)
            del_company.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except:
            return Response(
                {"message": f"Company with name: {company_name} not found"},
                status=status.HTTP_404_NOT_FOUND,
            )


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def company_details(request, company_name=None):
    """
    Get company details of the company with given name

    Args:
        request (HttpRequest): The HTTP request object
        company_name (str): The name of the company to retrieve details for

    Returns:
        Response: HTTP response object containing serialized company details or error message
    """

    if request.method == "GET":
        try:
            company = Company.objects.get(company=company_name)
        except:
            return Response(
                {"message": f"Company with name: {company_name} not found"},
                status=status.HTTP_404_NOT_FOUND,
            )
        serializer = CompanySerializer(company)
        return Response(serializer.data, status=status.HTTP_204_NO_CONTENT)


@api_view(["POST"])
def add_stock(request):
    """
    This function adds a new stock record.

    Parameters:
    request (HttpRequest): The HTTP request object containing the data for the new stock record.

    Returns:
    Response: A Response object containing the serialized data of the new stock record if it is created successfully,
     or a Response object containing the errors and a status code of 400 if the data is invalid.
    """
    company_name = request.data.get('company')
    if request.method == "POST":
        serializer = StockPriceSerializer(data=request.data)
        company = get_object_or_404(Company, company=company_name)
        if serializer.is_valid():
            serializer.save(company=company)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET"])
def list_stocks(request, company, start_date, end_date):
    """
    Retrieve a paginated list of stock prices for the given company within the specified date range.

    :param request: Request object
    :type request: django.http.request.HttpRequest
    :param company: Name of the company to retrieve stock prices for
    :type company: str
    :param start_date: Start date of the date range (inclusive), in YYYY-MM-DD format
    :type start_date: str
    :param end_date: End date of the date range (inclusive), in YYYY-MM-DD format
    :type end_date: str
    :return: Paginated list of stock prices for the given company within the specified date range
    :rtype: django.http.response.HttpResponse
    :raises: Http404 if no company exists with the given name
    """

    paginator = PageNumberPagination()
    paginator.page_size = 10
    try:
        stocks = StockPrice.objects.filter(
            company__company=company)
    except:
        return Response(
            {"message": f"Company with name: {company} not found"},
            status=status.HTTP_404_NOT_FOUND,
        )

    result_page = paginator.paginate_queryset(stocks, request)
    serializer = StockPriceSerializer(result_page, many=True)
    return paginator.get_paginated_response(serializer.data)
