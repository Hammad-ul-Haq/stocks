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