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

```http
  GET /us_stocks/company/
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `token` | `string` | **Required**. Your JWT |

#### Create new object of company
header should contains: `ticker`, `company`, `industry`, `sector`, `address`


```http
  POST /us_stocks/company/
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `token`   | `string` | **Required**. Your JWT            |

#### Update object of company
header contains: `ticker`, `company`, `industry`, `sector`, `address`

```http
  PUT /us_stocks/company/
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `token`   | `string` | **Required**. Your JWT            |



#### Delete object of company

```http
  DELETE /us_stocks/company/<str:company_name>
```

| Parameter   | Type     | Description                       |
| :--------   | :------- | :-------------------------------- |
| `token`     | `string` | **Required**. Your JWT            |
| `company` | `string` | **Required**. Name of compamy you want to delete   |

#### Get company object details


```http
  GET /us_stocks/company-details/<str:company_name>
```

| Parameter   | Type     | Description                       |
| :--------   | :------- | :-------------------------------- |
| `token`     | `string` | **Required**. Your JWT            |
| `company` | `string` | **Required**. Name of compamy   |


#### Create new object of stocks
header contains: `company`, `date`, `open`, `close`, `volume`


```http
  POST /us_stocks/add-stock/
```

| Parameter   | Type     | Description                       |
| :--------   | :------- | :-------------------------------- |
| `token`     | `string` | **Required**. Your JWT            |


#### Get objects of stocks 



```http
  POST /list-stocks/<str:company>/<str:start_date>/<str:end_date>
```

| Parameter   | Type     | Description                       |
| :--------   | :------- | :-------------------------------- |
| `token`     | `string` | **Required**. Your JWT            |
| `company`   | `string` | **Required**. Name of company        |
| `start_date`| `string` | **Required**. Start date of stocks         |
| `end_date`  | `string` | **Required**. End date of stocks           |