import requests
import os
from twilio.rest import Client

CLIENT = Client("AC116c37b1987c3093664d726b1bbd2e3a", "b97f91cfb411cb7ce51f4518ceff0e58")
STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

STOCK_API_KEY = ""
NEWS_API_KEY = ""

## STEP 1: Use https://www.alphavantage.co/documentation/#daily
# When stock price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

# Get yesterday's closing stock price. Hint: You can perform list comprehensions on Python dictionaries. e.g. [new_value for (key, value) in dictionary.items()]
stock_params = {
    "function": "TIME_SERIES_DAILY_ADJUSTED",
    "symbol": STOCK_NAME,
    "apikey": STOCK_API_KEY
}
response = requests.get(STOCK_ENDPOINT, params=stock_params)
data = response.json()["Time Series (Daily)"]
data_list = [value for (key, value) in data.items()]
print(data_list)

yesterday_data = data_list[0]
yesterday_closing_price = yesterday_data['4. close']
print(yesterday_closing_price)

# Get the day before yesterday's closing stock price
day_before_yesterday_data = data_list[1]
day_before_yesterday_closing_price = day_before_yesterday_data['4. close']
print(day_before_yesterday_closing_price)

# Find the positive difference between 1 and 2. e.g. 40 - 20 = -20, but the positive difference is 20. Hint: https://www.w3schools.com/python/ref_func_abs.asp
dif = float(yesterday_closing_price) - float(day_before_yesterday_closing_price)
up_down = None
if dif > 0:
    up_down = "🔺"
else:
    up_down = "🔻"

# Work out the percentage difference in price between closing price yesterday and closing price the day before yesterday.
diff_percent = round(dif / float(yesterday_closing_price) * 100)
print(diff_percent)

# If percentage is greater than 5 then print("Get News").
# Instead of printing ("Get News"), use the News API to get articles related to the COMPANY_NAME.

if abs(diff_percent) > 1:
    news_params = {
        "apiKey": NEWS_API_KEY,
        "qInTitle": COMPANY_NAME
    }
    news_response = requests.get(NEWS_ENDPOINT, params=news_params)
    articles = news_response.json()["articles"]
    print(articles)

    # Use Python slice operator to create a list that contains the first 3 articles. Hint: https://stackoverflow.com/questions/509211/understanding-slice-notation
    three_articles = articles[:3]
    print(three_articles)

    formatted_articles = [f"{STOCK_NAME}: {up_down} {diff_percent}% \nHeadline: {article['title']}. \n Brief: {article['description']}" for article in
                          three_articles]

    # TODO 8. - Create a new list of the first 3 article's headline and description using list comprehension.
    for article in formatted_articles:
        message = CLIENT.messages \
            .create(
            body=article,
            from_='+12708133850',
            to='+1829721'
        )
        print(message.status)
# TODO 9. - Send each article as a separate message via Twilio.

