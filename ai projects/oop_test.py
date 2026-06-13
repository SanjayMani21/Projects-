class Trade:

    def __init__(self, qty, buy, sell):

        self.qty = qty
        self.buy = buy
        self.sell = sell


    def __str__(self):
          return f"QTY:{self.qty} BUY:{self.buy} SELL:{self.sell}"
    
    def calculate_pl(self):

        return (self.sell - self.buy) * self.qty




trade1 = Trade(10, 100, 120)
trade2 = Trade(5, 200, 250)
trade3 = Trade(3, 50, 40)

trades = []

trades.append(trade1)
trades.append(trade2)
trades.append(trade3)

print(trade1)