# Yahoo financial Ticket Data Scraper API

This is an API that allows you to scrape ticket data from Yahoo Finance based on a company and a date range. 
The API returns the Date, Open, Close, and Volume data for the specified company during the specified date range.

## How it works
The API uses BeautifulSoup in the backend to scrape data from the Yahoo Finance website. When a request is made to the 
API with a specific company and date range, the API sends a request to the Yahoo Finance website and scrapes the 
necessary data using BeautifulSoup. The scraped data is then returned to the client in the form of a JSON response.

## Requirements
- Python 3.11
- Django 4.2
- BeautifulSoup4
- 
## Installation
To install the required packages, you can run the following command:

    # create virtual enviorment
    python -m venv venv
    # activate virtual enviorment (Linux/Macox)
    source venv/bin/activate
    pip install -r requirement.txt

## Migrations
Before running the API, you need to apply the migrations to create the database tables. 
You can do this by running the following commands:

    python manage.py makemigrations
    python manage.py migrate

## To Bulk load data

To load data in bulk, you can use the bulk_import command provided by the API. The command takes three arguments: 
the company ticker symbol, the start date of the date range, and the end date of the date range. For example, 
to load data for Apple Inc. (AAPL) between 1-12-2022 and 1-31 2022, you can run the following command:

      python manage.py bulk_import [company] [start_date] [end_date]

Note that this command will take some time to execute

## Run the app

To start the API server locally, you can run the following command:

    python manage.py runserver

## Run the tests

To run the tests, you can use the following command:

    ./manage.py test --pattern="*_test.py"

This will run all the tests that match the pattern *_test.py.

## API Reference

#### Generate token
Pass `username` and `password` to generate token


```http
  POST /us_stocks/token/
```

<img width="1355" alt="Screen Shot 2023-05-02 at 1 03 25 PM" src="https://user-images.githubusercontent.com/52544737/235612353-e18a0340-a98a-4af5-9c29-84fa0ee40e8c.png">

#### Get all companies

<img width="1347" alt="Screen Shot 2023-05-01 at 2 49 04 PM" src="https://user-images.githubusercontent.com/52544737/235437074-96463e13-652e-4ad9-a684-d6c7db81f1f1.png">

```http
  GET /us_stocks/company/
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `token` | `string` | **Required**. Your JWT |

#### Create new object of company
header should contains: `ticker`, `company`, `industry`, `sector`, `address`

<img width="1360" alt="Screen Shot 2023-05-01 at 2 49 47 PM" src="https://user-images.githubusercontent.com/52544737/235437145-1b3a5fd7-6e62-453b-b4e5-c01353b39d2b.png">


```http
  POST /us_stocks/company/
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `token`   | `string` | **Required**. Your JWT            |

#### Update object of company
header contains: `ticker`, `company`, `industry`, `sector`, `address`

<img width="1360" alt="Screen Shot 2023-05-01 at 2 50 24 PM" src="https://user-images.githubusercontent.com/52544737/235437224-2dd340a9-d768-47cc-9480-32caeaa93f86.png">


```http
  PUT /us_stocks/company/<str:company_name>
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `token`   | `string` | **Required**. Your JWT            |



#### Delete object of company

<img width="1366" alt="Screen Shot 2023-05-01 at 2 52 45 PM" src="https://user-images.githubusercontent.com/52544737/235437460-2ee9e789-7a84-489d-87ce-d4b1d02c48fc.png">


```http
  DELETE /us_stocks/company/<str:company_name>
```

| Parameter   | Type     | Description                       |
| :--------   | :------- | :-------------------------------- |
| `token`     | `string` | **Required**. Your JWT            |
| `company` | `string` | **Required**. Name of compamy you want to delete   |

#### Get company object details

<img width="1355" alt="Screen Shot 2023-05-01 at 2 53 18 PM" src="https://user-images.githubusercontent.com/52544737/235437493-9b9231f5-7479-4f46-8b47-ef326b99339a.png">

```http
  GET /us_stocks/company-details/<str:company_name>
```

| Parameter   | Type     | Description                       |
| :--------   | :------- | :-------------------------------- |
| `token`     | `string` | **Required**. Your JWT            |
| `company` | `string` | **Required**. Name of compamy   |


#### Create new object of stocks
header contains: `company`, `date`, `open`, `close`, `volume`

<img width="1352" alt="Screen Shot 2023-05-01 at 2 54 32 PM" src="https://user-images.githubusercontent.com/52544737/235437601-a61d6843-b9a9-4216-8f4d-d6053086595b.png">

```http
  POST /us_stocks/add-stock/
```

| Parameter   | Type     | Description                       |
| :--------   | :------- | :-------------------------------- |
| `token`     | `string` | **Required**. Your JWT            |


#### Get objects of stocks 

<img width="1369" alt="Screen Shot 2023-05-01 at 2 55 04 PM" src="https://user-images.githubusercontent.com/52544737/235437651-0368cdd1-b3c4-48c6-b15c-f8cc0a1821e9.png">


```http
  POST /list-stocks/<str:company>/<str:start_date>/<str:end_date>
```

| Parameter   | Type     | Description                       |
| :--------   | :------- | :-------------------------------- |
| `token`     | `string` | **Required**. Your JWT            |
| `company`   | `string` | **Required**. Name of company        |
| `start_date`| `string` | **Required**. Start date of stocks         |
| `end_date`  | `string` | **Required**. End date of stocks           |
