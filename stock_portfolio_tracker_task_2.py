# Stock Portfolio Tracker

# Sample stock prices
stock_prices = {
    "TCS": 3500,
    "INFY": 1600,
    "WIPRO": 280,
    "HCL": 1400,
    "RELIANCE": 2900
}

portfolio = {}
total_investment = 0

print("===== Stock Portfolio Tracker =====")

while True:
    stock_name = input("Enter Stock Name (or 'done' to finish): ").upper()

    if stock_name == "DONE":
        break

    if stock_name not in stock_prices:
        print("Stock not available in database.")
        continue

    quantity = int(input(f"Enter quantity of {stock_name}: "))

    portfolio[stock_name] = quantity

# Calculate total investment
print("\n===== Portfolio Summary =====")

for stock, quantity in portfolio.items():
    value = stock_prices[stock] * quantity
    total_investment += value

    print(
        f"{stock} | Quantity: {quantity} | "
        f"Price: ₹{stock_prices[stock]} | Value: ₹{value}"
    )

print("\nTotal Investment Value: ₹", total_investment)

# Save result to a file
with open("portfolio_summary.txt", "w") as file:
    file.write("Stock Portfolio Summary\n")
    file.write("-----------------------\n")

    for stock, quantity in portfolio.items():
        value = stock_prices[stock] * quantity
        file.write(
            f"{stock} - Quantity: {quantity}, Value: ₹{value}\n"
        )

    file.write(f"\nTotal Investment Value: ₹{total_investment}")

print("\nPortfolio saved successfully to portfolio_summary.txt")