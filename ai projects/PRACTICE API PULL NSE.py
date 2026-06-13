###PRACTICE API PULL FROM NSE:
import requests


headers = {
    "User-Agent": "Mozilla/5.0"
}

symbol = "RELIANCE"

response = requests.get(url=f"https://www.nseindia.com/api/NextApi/apiClient/GetQuoteApi?functionName=getSymbolData&marketType=N&series=EQ&symbol={symbol}",
                        headers= headers,
                        timeout=10)
data = response.json()

print(response.status_code)

a = data['equityResponse'][0]['metaData']

close = a['closePrice']
open = a['open']
high = a['dayHigh']
low = a['dayLow']

print(f"Close : {close}\nOpen: {open}\nHigh: {high}\nLow: {low}")

if(close - open)>5:
    print("Not Flat")
else:
    print('flat')

