# DRF API to scrap Yahoo finance data

This api scrap tickets data from Yahoo finance on the basis of Company and date range and returns `Date`, `Open`, `Close` and `Volume`.

This API use `BeautifulSoup` in backend to scrap data from web.

## Install

    # create virtual enviorment
    python -m venv venv
    # activate virtual enviorment (Linux/Macox)
    source venv/bin/activate
    pip install -r requirement.txt

## Migrations
    python manage.py makemigrations
    python manage.py migrate

## To Bulk load data
      python manage.py bulk_import [company] [start_date] [end_date]
## Run the app

    python manage.py runserver

## Run the tests

    ./manage.py test --pattern="*_test.py"

## API Reference

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
