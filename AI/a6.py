import random

# -------------------- Stock Class --------------------

class Stock:
    def __init__(self, symbol, price, quantity):
        self.symbol = symbol
        self.price = price
        self.quantity = quantity

    def update_price(self):
        change = random.uniform(-0.5, 0.5)
        self.price = round(self.price * (1 + change), 2)


# -------------------- Expert System --------------------

class ExpertSystem:
    def evaluate(self, stock):

        # RULES (Knowledge Base)
        if stock.price < 150:
            return "BUY", "Price is low (<150)"  # decision, reason 
        elif stock.price > 1000:
            return "SELL", "Price is very high (>1000)"
        else:
            return "HOLD", "Price is stable"


# -------------------- Portfolio --------------------

class Portfolio:
    def __init__(self):
        self.stocks = {}
        self.balance = 10000
        self.expert = ExpertSystem()

    def add_stock(self, stock):
        self.stocks[stock.symbol] = stock  #points to the stock object for value {symbol: object}

    def display_stocks(self):
        print("\n------ STOCK PORTFOLIO ------")
        print(f"Balance: ₹{self.balance:.2f}")
        print("-" * 50)

        for symbol, stock in self.stocks.items():
            decision, reason = self.expert.evaluate(stock)

            print(f"Symbol: {stock.symbol}")
            print(f"Price: ₹{stock.price}")
            print(f"Quantity: {stock.quantity}")
            print(f"Recommendation: {decision}")
            print(f"Reason: {reason}")
            print("-" * 50)

    def buy_stock(self, symbol, quantity):
        stock = self.stocks.get(symbol)   # get the value as object for the given symbol key dict.get(key_name)-> returns symbol

        if not stock:
            print("Stock not found!")
            return

        cost = stock.price * quantity

        if self.balance >= cost and stock.quantity >= quantity:
            stock.quantity -= quantity
            self.balance -= cost
            print(f"Bought {quantity} shares of {symbol}")
        else:
            print("Insufficient balance or stock unavailable!")

    def sell_stock(self, symbol, quantity):
        stock = self.stocks.get(symbol)

        if not stock:
            print("Stock not found!")
            return

        stock.quantity += quantity
        self.balance += stock.price * quantity
        print(f"Sold {quantity} shares of {symbol}")

    def update_stocks(self):
        for stock in self.stocks.values():
            stock.update_price()

        print("Stock prices updated!")


# -------------------- Initialize --------------------

portfolio = Portfolio()

portfolio.add_stock(Stock("AAPL", 130, 100))
portfolio.add_stock(Stock("GOOG", 1900, 50))
portfolio.add_stock(Stock("MSFT", 240, 75))


# -------------------- Menu Driven Program --------------------

while True:
    print("\n===== STOCK MANAGEMENT SYSTEM =====")
    print("1. View Stocks")
    print("2. Buy Stock")
    print("3. Sell Stock")
    print("4. Update Stock Prices")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        portfolio.display_stocks()

    elif choice == "2":
        symbol = input("Enter stock symbol: ").upper()
        quantity = int(input("Enter quantity: "))
        portfolio.buy_stock(symbol, quantity)

    elif choice == "3":
        symbol = input("Enter stock symbol: ").upper()
        quantity = int(input("Enter quantity: "))
        portfolio.sell_stock(symbol, quantity)

    elif choice == "4":
        portfolio.update_stocks()

    elif choice == "5":
        print("Exiting program...")
        break

    else:
        print("Invalid choice! Try again.")