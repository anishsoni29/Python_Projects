import pandas as pd

def load_stocks(file_path):
    """
    Loads stock data from a CSV file.
    """
    try:
        return pd.read_csv(file_path)
    except Exception as e:
        print(f"Error loading file {file_path}: {e}")
        return None

def save_results_to_csv(results, file_path):
    """
    Saves the investment results to a CSV file.
    """
    try:
        df = pd.DataFrame(results)
        df.to_csv(file_path, index=False)
        print(f"Results saved to {file_path}")
    except Exception as e:
        print(f"Error saving results: {e}")

def save_results_to_excel(results, file_path):
    """
    Saves the investment results to an Excel file.
    """
    try:
        df = pd.DataFrame(results)
        df.to_excel(file_path, index=False)
        print(f"Results saved to {file_path}")
    except Exception as e:
        print(f"Error saving results: {e}")
