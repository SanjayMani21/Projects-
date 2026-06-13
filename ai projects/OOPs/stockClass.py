class Stock:
    def __init__(self,name, open_price, close_price):
        self.name = name
        self.open_price = open_price
        self.close_price = close_price

    def price_change(self):
        change = self.close_price - self.open_price
        return change
    
    def is_flat(self):
        return abs(self.price_change()) < 5 
            
    def __str__(self):
        return f"{self.name} opened at {self.open_price} and closed at {self.close_price} and the price changed is {self.price_change()} hence the market is {'flat' if self.is_flat() else 'not flat'}"
    
    @staticmethod
    def create_stock(stock):
        return Stock(stock['name'], stock['open'], stock['close'])

# reliance = Stock("Reliance", 2000, 3200)
# print(reliance)

# tata = Stock("Tata",100,200)
# print(tata)

# Using objects, list , for loop 

stocks = [{"name": 'reliance',"open":  100,"close" :200}, {"name": 'tata',"open" : 300,"close": 1000}, {"name": 'Cognizant',"open" : 1000,"close": 1000}]

for stock in stocks:
    
    response = Stock.create_stock(stock)
    print(response)
    