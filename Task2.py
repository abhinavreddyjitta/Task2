```python
import csv

# Predefined stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 420,
    "AMZN": 190
}

portfolio = []
total_investment = 0

print("=" * 45)
print("       STOCK PORTFOLIO TRACKER")
print("=" * 45)

print("\nAvailable Stocks and Prices:")
for stock, price in stock_prices.items():
    print(f"{stock}: ${price}")

print("\nEnter your stock details.")
print("Type 'done' when you finish.\n")

while True:
    stock_name = input("Enter stock symbol: ").strip().upper()

    if stock_name == "DONE":
        break

    if stock_name not in stock_prices:
        print("Invalid stock symbol! Please choose from the list.")
        continue

    try:
        quantity = int(input("Enter quantity: "))

        if quantity <= 0:
            print("Quantity must be greater than zero.")
            continue

    except ValueError:
        print("Please enter a valid whole number.")
        continue

    price = stock_prices[stock_name]
    investment = price * quantity

    portfolio.append({
        "Stock": stock_name,
        "Quantity": quantity,
        "Price": price,
        "Investment": investment
    })

    total_investment += investment

    print(f"Added {quantity} shares of {stock_name}.\n")

# Display portfolio summary
print("\n" + "=" * 55)
print("                 PORTFOLIO SUMMARY")
print("=" * 55)

if portfolio:
    print(f"{'Stock':<12}{'Quantity':<12}{'Price':<12}{'Investment':<15}")
    print("-" * 51)

    for item in portfolio:
        print(
            f"{item['Stock']:<12}"
            f"{item['Quantity']:<12}"
            f"${item['Price']:<11}"
            f"${item['Investment']:<14}"
        )

    print("-" * 51)
    print(f"Total Investment: ${total_investment}")

    # Save portfolio to CSV file
    with open("portfolio.csv", "w", newline="") as file:
        fieldnames = ["Stock", "Quantity", "Price", "Investment"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        writer.writeheader()
        writer.writerows(portfolio)

        writer.writerow({
            "Stock": "TOTAL",
            "Quantity": "",
            "Price": "",
            "Investment": total_investment
        })

    print("\nPortfolio saved successfully to portfolio.csv")

else:
    print("No stocks were added to your portfolio.")

print("\nThank you for using Stock Portfolio Tracker!")
```
