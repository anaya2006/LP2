import random

class User:
    def __init__(self, name, budget, risk_level):
        self.name = name
        self.budget = budget
        self.risk_level = risk_level


class Stock:
    def __init__(self, symbol, price, quantity):
        self.symbol = symbol
        self.price = price
        self.quantity = quantity

    def update_price(self):
        # Smaller realistic fluctuation
        change = random.uniform(-0.7, 0.7)
        self.price = round(self.price * (1 + change), 2)


class ExpertSystem:
    def evaluate(self, stock, user):

        # Expert rules based on stock price + user risk level

        if user.risk_level == "LOW":
            if stock.price < 150:
                return "BUY", "Safe low-priced stock for low-risk investor"
            elif stock.price > 700:
                return "SELL", "Expensive stock for low-risk investor"
            else:
                return "HOLD", "Stable stock"

        elif user.risk_level == "MEDIUM":
            if stock.price < 200:
                return "BUY", "Good opportunity for medium-risk investor"
            elif stock.price > 900:
                return "SELL", "Very high-priced stock"
            else:
                return "HOLD", "Moderately stable stock"

        elif user.risk_level == "HIGH":
            if stock.price < 300:
                return "BUY", "Aggressive buying opportunity"
            elif stock.price > 1200:
                return "SELL", "Profit booking opportunity"
            else:
                return "HOLD", "Risk acceptable"

        return "HOLD", "No recommendation available"


class Portfolio:
    def __init__(self, user):
        self.user = user
        self.stocks = {}
        self.expert = ExpertSystem()

    def add_stock(self, stock):
        self.stocks[stock.symbol] = stock

    def display_stock(self):

        print("\nSTOCK PORTFOLIO")
        print("-" * 70)

        print(f"Investor Name : {self.user.name}")
        print(f"Risk Level    : {self.user.risk_level}")
        print(f"Balance       : {self.user.budget:.2f}")

        print("-" * 70)

        for symbol, stock in self.stocks.items():

            decision, reason = self.expert.evaluate(stock, self.user)

            print(f"Stock Symbol  : {stock.symbol}")
            print(f"Stock Price   : {stock.price}")
            print(f"Stock Quantity: {stock.quantity}")
            print(f"Recommendation: {decision}")
            print(f"Reason        : {reason}")

            print("-" * 70)

    def buy_stock(self, symbol, quantity):

        stock = self.stocks.get(symbol)

        if not stock:
            print("Stock not found")
            print()
            return

        cost = stock.price * quantity

        if cost <= self.user.budget and stock.quantity >= quantity:

            self.user.budget -= cost
            stock.quantity -= quantity

            print(f"Stocks bought {symbol} : {quantity} Successfully!")
            print(f"Remaining Balance : {self.user.budget:.2f}")
            print()

        else:
            print("Insufficient balance or stock quantity unavailable")
            print()

    def sell_stock(self, symbol, quantity):

        stock = self.stocks.get(symbol)

        if not stock:
            print("Stock not found")
            print()
            return

        revenue = stock.price * quantity

        stock.quantity += quantity
        self.user.budget += revenue

        print(f"Stock sold {symbol} : {quantity} Successfully!")
        print(f"Updated Balance : {self.user.budget:.2f}")
        print()

    def update_stock(self):

        for stock in self.stocks.values():
            stock.update_price()

        print("Stock prices updated successfully!")
        print()


# ---------------- MAIN PROGRAM ---------------- #

print("STOCK MARKET SIMULATION SYSTEM")
print("-" * 70)

name = input("Enter investor name : ")
budget = float(input("Enter investment budget : "))
risk = input("Enter risk level (LOW / MEDIUM / HIGH): ").upper()

user = User(name, budget, risk)

portfolio = Portfolio(user)

portfolio.add_stock(Stock("AAPL", 100, 50))
portfolio.add_stock(Stock("GOOG", 140, 75))
portfolio.add_stock(Stock("MSFT", 200, 15))

while True:

    print("\n1. View Portfolio")
    print("2. Buy Stocks")
    print("3. Sell Stocks")
    print("4. Update Stock Prices")
    print("5. Exit")

    ch = int(input("Enter your choice : "))
    print()

    if ch == 1:

        portfolio.display_stock()

    elif ch == 2:

        symbol = input("Enter stock symbol : ").upper()
        quantity = int(input("Enter no of stocks to buy : "))

        portfolio.buy_stock(symbol, quantity)

    elif ch == 3:

        symbol = input("Enter stock symbol : ").upper()
        quantity = int(input("Enter no of stocks to sell : "))

        portfolio.sell_stock(symbol, quantity)

    elif ch == 4:

        portfolio.update_stock()

    elif ch == 5:

        print("Exiting program...")
        break

    else:

        print("Invalid choice")