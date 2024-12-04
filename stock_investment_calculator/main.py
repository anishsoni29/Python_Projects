import os
import pandas as pd
from scripts.utils import load_stocks, save_results_to_csv, save_results_to_excel 
from scripts.fetch_data import fetch_stock_data
from scripts.calculate_investment import calculate_investment

def main():
    # Load stock data
    stock_file = 'data/stocks.csv'
    stocks = load_stocks(stock_file)

    if stocks is None:
        return

    # Input parameters
    total_investment = float(input("Enter total investment amount: "))
    start_date = input("Enter start date (YYYY-MM-DD): ")
    end_date = input("Enter end date (YYYY-MM-DD): ")

    results = []

    for _, row in stocks.iterrows():
        ticker = row['Ticker']
        weightage = row['Weightage']

        # Fetch stock data
        data = fetch_stock_data(ticker, start_date, end_date)
        if data is None:
            continue

        # Calculate investment and adjusted weightage
        investment_data = calculate_investment(data, total_investment, weightage, ticker, end_date)
        results.append(investment_data)

    # Save results
    os.makedirs('results', exist_ok=True)
    results_df = pd.DataFrame(results)
    save_results_to_csv(results_df, 'results/investment_results.csv')
    save_results_to_excel(results_df, 'results/investment_results.xlsx')

    print("\nSample Output:")
    print(results_df)

if __name__ == '__main__':
    main()
