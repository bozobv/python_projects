import requests
from twilio.rest import Client


STOCK = "TSLA"
COMPANY_NAME = "Tesla"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

STOCK_API_KEY = ""
NEWS_API_KEY = ""

class StockNews:

    def __init__(self, company, stock):
        self.change = 0
        self.company = company
        self.stock = stock

    ## STEP 1: Use https://newsapi.org/docs/endpoints/everything
    # When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

    def five_percent_change(self):
        url = f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={self.stock}&interval=5min&apikey={STOCK_API_KEY}'
        r = requests.get(url)
        data = r.json()['Time Series (Daily)']

        iterator = iter(data)

        first_last_date = next(iterator)
        first_last_close = data[first_last_date]['4. close']

        second_last_date = next(iterator)
        sec_last_close = data[second_last_date]['4. close']


        change = sec_last_close - first_last_close

        self.change = 1 - change / sec_last_close

        if abs(self.change) > 0.05:
            self.get_news(first_last_date)
        
        self.change *= 100
        self.change = round(self.change)
        


    ## STEP 2: Use https://newsapi.org/docs/endpoints/everything
    # Instead of printing ("Get News"), actually fetch the first 3 articles for the COMPANY_NAME. 

    def get_news(self, date):
        url = f'https://newsapi.org/v2/everything?q={self.company}&from={date}&sortBy=popularity&pageSize=3&apiKey={NEWS_API_KEY}'
        r = requests.get(url)
        data = r.json()["articles"]

        #print(data)

        news = []
        for article in data:
            article_dict = {}
            article_dict["headline"] = article["title"]
            article_dict["brief"] = article["description"]

            news.append(article_dict)

        self.news = news
        #return news

## STEP 3: Use twilio.com/docs/sms/quickstart/python
# Send a separate message with each article's title and description to your phone number. 

    def send_sms(self):

        
        account_sid = ""
        auth_token = ""
        client = Client(account_sid, auth_token)


        if self.change >= 0:
            change_text = f"{self.stock}: 🔺{self.change}%"
        else:
            change_text = f"{self.stock}: 🔻{self.change}%"

        for new in self.news:
            print(new)
            message = client.messages.create(
                body=f"{change_text}\nHeadline: {new['headline']}\nBrief: {new['brief']}",
                from_="+12085677795",
                to="+36206677528",
            )

            print(message.body)

        

st = StockNews(company=COMPANY_NAME, stock=STOCK)
st.get_news("2024-08-16")
st.change = 7
st.send_sms()



#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

