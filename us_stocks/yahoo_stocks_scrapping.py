import pandas as pd
import requests
from bs4 import BeautifulSoup


def unix_date(date):
    """
        Converts a date in the format "DD-MM-YYYY" to a Unix timestamp (number of seconds since January 1, 1970).

        Args:
            date (str): A date string in the format "DD-MM-YYYY".

        Returns:
            float: A Unix timestamp representing the given date.

        Raises:
            ValueError: If the date string is not in the expected format or contains invalid values for day, month or year.

        Example:
            >>> unix_date("01-05-2023")
            1_772_377_600.0
    """

    date = date.split("-")
    # Define the date as day, month, and year
    day, month, year = int(date[0]), int(date[1]), int(date[2])

    import datetime
    from datetime import timezone

    dt = datetime.datetime(year, month, day)
    timestamp = dt.replace(tzinfo=timezone.utc).timestamp()

    return timestamp


def get_profile():
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/112.0.0.0 Safari/537.36"
    }
    url_profile = "https://finance.yahoo.com/quote/AAPL/profile?p=AAPL"

    r = requests.get(url_profile, headers=headers)

    soup = BeautifulSoup(r.text, "html.parser")

    # getting name
    name = soup.find("h1", {"class": "D(ib) Fz(18px)"}).text

    # getting address
    address_object = soup.find("p", {"class": "D(ib) W(47.727%) Pend(40px)"})
    words = address_object.get_text(separator="<br>", strip=True).split("<br>")
    address = " ".join(words[0:-2])

    return (name, address)


def get_stocks_data(start_date, end_date):
    """
    Scrapes historical data for the AAPL stock ticker from Yahoo Finance for the specified time range and returns a
    Pandas DataFrame.

    Args:
        start_date (str): A date string in the format "DD-MM-YYYY" representing the start of the time range to scrape.
        end_date (str): A date string in the format "DD-MM-YYYY" representing the end of the time range to scrape.

    Returns:
        pd.DataFrame: A Pandas DataFrame containing the historical data for the AAPL stock ticker within the specified
        time range.

    Raises:
        ValueError: If either start_date or end_date is not in the expected format or contains invalid values for day,
        month, or year.
        Exception: If the request to Yahoo Finance fails, or the HTML content cannot be parsed correctly.

    Example:
        >>> get_stocks_data("01-01-2022", "31-12-2022")
                      Date        Open       Close    Volume
        0      2022-01-03  177.330002  181.110001  14006400
        1      2022-01-04  181.929993  182.500000  16548300
        2      2022-01-05  182.070007  179.509995  18226000
        3      2022-01-06  178.809998  181.070007  14668500
    """

    unix_start_date = int(unix_date(start_date))
    unix_end_date = int(unix_date(end_date))

    url_history = f"https://finance.yahoo.com/quote/AAPL/history?period1={unix_start_date}&period2={unix_end_date}&interval=1d&filter=history&frequency=1d&includeAdjustedClose=true"
    # url = "https://finance.yahoo.com/quote/AAPL/history?period1=1640995200&period2=1672444800&interval=1d&filter=history&frequency=1d&includeAdjustedClose=true"

    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/112.0.0.0 Safari/537.36"
    }

    response = requests.get(url_history, headers=headers)

    soup = BeautifulSoup(response.content, "html.parser")

    table = soup.find("table", {"class": "W(100%) M(0)"})

    table.find_all("th")
    header = []

    for th in table.find_all("th"):
        header.append(th.text.strip())

    data = []

    for tr in table.find_all("tr")[1:]:
        row = []
        for td in tr.find_all("td"):
            row.append(td.text.strip())
        data.append(row)

    df = pd.DataFrame(data=data, columns=header)
    df = df.rename({"Close*": "Close"}, axis=1)
    df = df[["Date", "Open", "Close", "Volume"]]
    df.drop(df.tail(1).index, inplace=True)
    df["Date"] = pd.to_datetime(df["Date"], dayfirst=True)
    df.drop(df.loc[df["Open"] == "0.23 Dividend"].index, inplace=True)
    df["Open"] = df["Open"].astype(float)
    df["Close"] = df["Close"].astype(float)
    df["Volume"] = df["Volume"].str.replace(",", "").astype(int)
    return df
