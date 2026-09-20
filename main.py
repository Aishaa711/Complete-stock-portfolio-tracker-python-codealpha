def get_quantity():
    while True:
      try:
        quantity = int(input("Enter quantity: "))

        if quantity <= 0:
            print("Invalid quantity.")
            continue

        return quantity
      except ValueError:
          print("Invalid quantity.")
          continue
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 420,
    "AMZN": 185
}
portfolio = {}
print("stock portfolio tracker :")
for key,value in stock_prices.items():
    print( key , " : " , value )

while True:
    stock = input("\nEnter stock symbol (or 'done' to finish): ").upper().strip()
    if stock == 'DONE':
        break
    if stock not in stock_prices:
        print("Stock not available.")
        print("Available stocks:", ", ".join(stock_prices.keys()))
        continue
    quantity = get_quantity()
    portfolio[stock] = portfolio.get(stock, 0) + quantity
total_price =0
for key,value in portfolio.items():
    mystock_price = stock_prices[key]*value
    print(f"{key}: {value} × ${stock_prices[key]} = ${mystock_price:,}")

    total_price += mystock_price
print(f"Total Investment Value: ${total_price:,}")
print("end of program")