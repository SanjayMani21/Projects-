from dhanhq import DhanContext, dhanhq
import pandas as pd

client_id = "1100389085"
token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJpc3MiOiJkaGFuIiwicGFydG5lcklkIjoiIiwiZXhwIjoxNzgwMzM1OTk4LCJpYXQiOjE3ODAyNDk1OTgsInRva2VuQ29uc3VtZXJUeXBlIjoiU0VMRiIsIndlYmhvb2tVcmwiOiIiLCJkaGFuQ2xpZW50SWQiOiIxMTAwMzg5MDg1In0.LESlrcwDczqTLjZb2DWA2FA-1YtMbdTvxd1D--Apnja22K6eThQcfDLoPne6uwCzN91SuWggiAYhyyoKNFYLgQ"

dhan_context = DhanContext(client_id,token)
dhan = dhanhq(dhan_context)



holdings = dhan.get_holdings()
data_holdings = holdings['data']
symbol_hold = []
for stock in data_holdings:
    profit = stock['availableQty'] * (stock['lastTradedPrice'] - stock['avgCostPrice'])
    result={
        "Name":stock['tradingSymbol'],
        "Quantity": stock['availableQty'],
        'Average Price': round(stock['avgCostPrice'], 2),
        'LTP': round(stock['lastTradedPrice'], 2),
        'Profit': round(profit, 2)
        # 'Risk_Reward': 

     }


    symbol_hold.append(result)
# print(symbol_hold)    

df = pd.DataFrame(symbol_hold)

out_path = r"D:\ai projects\api\result.csv"

df.to_csv(out_path,index=False)




# get data from dhan holding // done
# calculate profit, percentage , R:R ratio // done  
# send it to excel // done

# Why to Excel -> To see profit and Risk reward as per my strategy for each stock holdings. // 
# to notify that stock price has reached more than certain profit% , RR ratio , Stoploss //

