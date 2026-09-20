# Stock Portfolio Tracker 📈

A simple Python console application that allows users to build a stock portfolio by selecting available stocks and entering the number of shares they want.

## Features

* Displays available stocks and their prices.
* Allows users to select stocks from the available list.
* Accepts the quantity of shares for each stock.
* Validates the entered quantity.
* Handles invalid non-numeric input.
* Allows adding more shares of the same stock.
* Calculates the value of each stock in the portfolio.
* Calculates the total investment value.
* Formats large numbers for easier reading.

## Available Stocks

The application currently includes:

* AAPL
* TSLA
* GOOGL
* MSFT
* AMZN

> The stock prices used in this project are sample values for learning purposes and are not live market prices.

## How to Run

Make sure Python is installed, then run:

```bash
python main.py
```

Enter a stock symbol when prompted.
Enter `done` when you have finished adding stocks.

## Example

```text
Enter stock symbol (or 'done' to finish): AAPL
Enter quantity: 8

Enter stock symbol (or 'done' to finish): TSLA
Enter quantity: 2

Enter stock symbol (or 'done' to finish): done

AAPL: 8 × $180 = $1,440
TSLA: 2 × $250 = $500
Total Investment Value: $1,940
```

## Technologies

* Python
* Dictionaries
* Loops
* Functions
* Input validation
* Exception handling
* String formatting
