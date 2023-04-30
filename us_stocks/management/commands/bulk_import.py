from django.core.management.base import BaseCommand
from us_stocks.yahoo_stocks_scrapping import get_stocks_data
from us_stocks.models import StockPrice, Company


class Command(BaseCommand):

    help='Display hello'

    def add_arguments(self, parser):
        parser.add_argument('company', type=str, help='end date')
        parser.add_argument('start_date', type=str, help='start date')
        parser.add_argument('end_date', type=str, help='end date')

    def handle(self, *args, **kwargs):
        """
        bulk import data
        """
        start_date = kwargs['start_date']
        end_date = kwargs['end_date']
        company = kwargs['company']

        data=get_stocks_data(start_date, end_date)
        company= Company.objects.get(company=company)
        stocks = [
            StockPrice(
                company = company,
                date= row['Date'],
                open = row['Open'],
                close = row['Close'],
                volume = row['Volume']
            )
            for i, row in data.iterrows()]
        StockPrice.objects.bulk_create(stocks)



        self.stdout.write('Succeeded')
