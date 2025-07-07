stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 135,
    "MSFT": 310,
    "AMZN": 125
}
portfolio = {}
print("Enter your stock portfolio (type 'done' to finish):")
while True:
    stock = input("Stock symbol (e.g., AAPL): ").upper()
    if stock == "DONE":
        break
    if stock not in stock_prices:
        print("Stock not found in database.")
        continue
    try:
        quantity = int(input(f"Quantity of {stock}: "))
        portfolio[stock] = portfolio.get(stock, 0) + quantity
    except ValueError:
        print("Invalid quantity. Please enter an integer.")
total_investment = 0
print("\nYour Portfolio:")
for stock, quantity in portfolio.items():
    price = stock_prices[stock]
    value = quantity * price
    total_investment += value
    print(f"{stock}: {quantity} shares @ ${price} = ${value}")
print(f"\nTotal Investment Value: ${total_investment}")
save_option = input("\nDo you want to save this to a file? (yes/no): ").lower()
if save_option == "yes":
    with open("portfolio_summary.csv", "w") as file:
        file.write("Stock,Quantity,Price per Share,Total Value\n")
        for stock, quantity in portfolio.items():
            price = stock_prices[stock]
            value = quantity * price
            file.write(f"{stock},{quantity},{price},{value}\n")
        file.write(f"\nTotal Investment,,,{total_investment}")
    print("Portfolio saved to 'portfolio_summary.csv'")
