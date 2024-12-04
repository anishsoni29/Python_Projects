import yfinance as yf

def fetch_stock_data(ticker, start_date, end_date):
    """
    Fetch historical stock data for the given ticker symbol.
    """
    # Append `.NS` to ticker for NSE stocks
    if not ticker.endswith(".NS") and not ticker.endswith(".BO"):
        ticker += ".NS"
    
    try:
        stock = yf.Ticker(ticker)
        data = stock.history(start=start_date, end=end_date)

        if data.empty:
            raise ValueError(f"No data found for ticker: {ticker}")
        
        return data
    except Exception as e:
        print(f"Error fetching data for {ticker}: {e}")
        return None
