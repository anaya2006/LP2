from flask import Flask, render_template, request, redirect
import random

app = Flask(__name__)

# -------------------- Stock Class --------------------

class Stock:
    def __init__(self, symbol, price, quantity):
        self.symbol = symbol
        self.price = price
        self.quantity = quantity

    def update_price(self):
        change = random.uniform(-0.05, 0.05)
        self.price = round(self.price * (1 + change), 2)


# -------------------- Expert System --------------------

class ExpertSystem:
    def evaluate(self, stock):
        """Inference Engine applying rules"""

        # RULES (Knowledge Base)
        if stock.price < 150:
            return "BUY", "Price is low (<150)"
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
        self.stocks[stock.symbol] = stock

    def get_recommendations(self):
        recommendations = {}
        for symbol, stock in self.stocks.items():
            decision, reason = self.expert.evaluate(stock)
            recommendations[symbol] = (decision, reason)
        return recommendations

    def buy_stock(self, symbol, quantity):
        stock = self.stocks.get(symbol)
        if not stock:
            return

        cost = stock.price * quantity
        if self.balance >= cost and stock.quantity >= quantity:
            stock.quantity -= quantity
            self.balance -= cost

    def sell_stock(self, symbol, quantity):
        stock = self.stocks.get(symbol)
        if not stock:
            return

        stock.quantity += quantity
        self.balance += stock.price * quantity

    def update_stocks(self):
        for stock in self.stocks.values():
            stock.update_price()


# -------------------- Initialize --------------------

portfolio = Portfolio()

portfolio.add_stock(Stock("AAPL", 130, 100))
portfolio.add_stock(Stock("GOOG", 1900, 50))
portfolio.add_stock(Stock("MSFT", 240, 75))


# -------------------- Routes --------------------

@app.route("/")
def index():
    recommendations = portfolio.get_recommendations()
    return render_template("index1.html",
                           portfolio=portfolio,
                           recommendations=recommendations)


@app.route("/buy", methods=["POST"])
def buy():
    portfolio.buy_stock(request.form["symbol"], int(request.form["quantity"]))
    return redirect("/")


@app.route("/sell", methods=["POST"])
def sell():
    portfolio.sell_stock(request.form["symbol"], int(request.form["quantity"]))
    return redirect("/")


@app.route("/update")
def update():
    portfolio.update_stocks()
    return redirect("/")


# -------------------- Run --------------------

if __name__ == "__main__":
    app.run(debug=True)
