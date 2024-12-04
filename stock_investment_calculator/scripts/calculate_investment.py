
import pandas as pd
import pandas_ta as ta

def calculate_investment(data, total_investment, weightage, ticker, end_date):
    """
    Calculates investment, adjusted weightage, and RSI for stock data.
    """
    # Calculate RSI
    data['RSI'] = ta.rsi(data['Close'], length=14)
    last_row = data.iloc[-1]

    # Retrieve last open, close, and RSI values
    last_close = last_row['Close']
    last_open = last_row['Open']
    last_rsi = last_row['RSI']

    # Allocate investment
    allocated_investment = total_investment * weightage

    # Adjust weightage based on RSI
    adjusted_weightage = weightage
    if last_rsi < 30:  # Oversold
        adjusted_weightage *= 1.1
    elif last_rsi > 70:  # Overbought
        adjusted_weightage *= 0.9

    return {
        "Ticker": ticker,
        "Date": end_date,
        "Weightage": weightage,
        "Adjusted Weightage": adjusted_weightage,
        "Open": last_open,
        "Close": last_close,
        "RSI": last_rsi
    }
