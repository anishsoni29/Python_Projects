
import matplotlib.pyplot as plt

def plot_stock_data(ticker, data):
    """
    Plots the stock price trends.
    """
    plt.figure(figsize=(10, 5))
    plt.plot(data['Close'], label=f'{ticker} Closing Price', color='blue')
    plt.title(f'{ticker} Stock Price Trend')
    plt.xlabel('Date')
    plt.ylabel('Close Price')
    plt.legend()
    plt.grid(True)
    plt.show()
