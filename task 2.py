
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 400,
    "AMZN": 190
}

portfolio = {}
total_investment = 0

print("=================================")
print("     STOCK PORTFOLIO TRACKER")
print("=================================")

while True:
    stock_name = input("\nEnter stock name (or 'done' to finish): ").upper()

    if stock_name == "DONE":
        break

    if stock_name in stock_prices:

        quantity = int(input("Enter quantity: "))

        if quantity <= 0:
            print("Please enter valid quantity!")
            continue

        portfolio[stock_name] = portfolio.get(stock_name, 0) + quantity

        print("Stock added successfully!")

    else:
        print("Stock not found! Please try again.")



print("\n======= YOUR PORTFOLIO =======")

for stock, quantity in portfolio.items():

    price = stock_prices[stock]
    investment = price * quantity

    total_investment += investment

    print(f"{stock} | Quantity: {quantity} | Price: ${price} | Value: ${investment}")

    print("-----------------------------------")

print(f"Total investment: ${total_investment}")



with open("portfolio.txt", "w") as file:

    file.write("STOCK PORTFOLIO REPORT\n")
    file.write("==============================\n")

    for stock, quantity in portfolio.items():

        investment = stock_prices[stock] * quantity

        file.write(
            f"{stock}: Quantity = {quantity}, Value = ${investment}\n"
        )

    file.write(f"\nTotal investment = ${total_investment}")

print("\nPortfolio saved successfully in portfolio.txt")
