import matplotlib.pyplot as plt
from matplotlib.pyplot import legend, figure
import numpy as np
import json
import requests
import mpld3
import time

results = []
date = []
close = []

def apiReq(sym):
    url = "https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=%s&apikey=UWQPK2ZPSPLFDIB5" % sym
    return requests.get(url).json()

apiRequestINTC = apiReq('INTC')
apiRequestAMD = apiReq('AMD')
apiRequestNVDA = apiReq('NVDA')

apiINTC = apiRequestINTC['Time Series (Daily)']
apiAMD = apiRequestAMD['Time Series (Daily)']
apiNVDA = apiRequestNVDA['Time Series (Daily)']

closeINTC = []
closeAMD =[]
closeNVDA =[]
dates = []

def loop(x, y):
    dates = (date == [])
    for value in x:
        if dates:
            date.append(value)
        y.append(float(x[value]['4. close']))

loop(apiINTC, closeINTC)
loop(apiAMD, closeAMD)
loop(apiNVDA, closeNVDA)

# print(date)

plt.figure(figsize = [18, 6])
plt.plot(date, closeINTC, 'b--', date, closeAMD, 'r--', date, closeNVDA, 'g--')
plt.title("Stocks")
plt.xticks(rotation=90)
mpld3.show()
