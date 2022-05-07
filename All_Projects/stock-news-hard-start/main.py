
import requests
from twilio.rest import Client

import datetime

time = datetime.datetime.now()
today = time.day
day_before_yesterday = today - 2
two_day_before_yesterday = today - 3

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
stock_price_key = " H63ANG3ENTCF5L6P"
stock_news_key = "ba4e35c847b542579989fd92ba55901e"

account_sid = "ACd400fd8415d4644bb07e343403fb1636"
auth_token = "2f9bca9a32431b4ed47a34cdb4e4fb3e"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

stock_price_parameter = {
    "function": "TIME_SERIES_INTRADAY",
    "symbol": STOCK,
    "interval": "60min",
    "apikey": stock_price_key,
}

stock_news_parameter = {
    "q": "tesla",
    "from": f"2022-02-{two_day_before_yesterday}",
    "apikey": stock_news_key,

}


response = requests.get(STOCK_ENDPOINT, params=stock_price_parameter)
data = response.json()
day_before_yesterday_price = float(data["Time Series (60min)"][f"2022-02-{day_before_yesterday} 20:00:00"]["4. close"])
two_day_before_yesterday_price = float(data["Time Series (60min)"][f"2022-02-{two_day_before_yesterday} 20:00:00"]
                                       ["4. close"])
percent_difference = (day_before_yesterday_price - two_day_before_yesterday_price) / day_before_yesterday_price * 100
if percent_difference > 5 or percent_difference < -5:
    response1 = requests.get(NEWS_ENDPOINT, params=stock_news_parameter)
    data = (response1.json())

    num = 0
    for title in data["articles"]:
        headline = (data["articles"][num]["title"])
        description = (data["articles"][num]["description"])
        url = (data["articles"][num]["url"])

        client = Client(account_sid, auth_token)

        if percent_difference > 5:
            message = client.messages \
                .create(body=f"TSLA: ▲ {int(percent_difference)}%\nHeadline: {headline}\nBrief: {description}\n {url}",
                        from_="+19032823075",
                        to="+918076431825")

        else:
            message = client.messages \
                .create(body=f"TSLA: ▼ {int(percent_difference)}%\nHeadline: {headline}\nBrief: {description}\n {url}",
                        from_="+19032823075",
                        to="+918076431825")
        print(message.status)
        num += 1
        if num > 2:
            break
