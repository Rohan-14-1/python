import pandas as pd

def load_data(file_paths):
    """
    Load data from one or more file paths using Pandas.

    Args:
    - file_paths (list): A list of file paths to load.

    Returns:
    - DataFrame or list of DataFrames: The loaded data.
    """
    data = []
    for file_path in file_paths:
        try:
            # Load data from file
            df = pd.read_csv(file_path)  # Assuming CSV format, you can change it based on your file format
            data.append(df)
        except Exception as e:
            print(f"Error loading data from '{file_path}': {str(e)}")
    return data

if __name__ == "__main__":
    # Example usage:
    file_paths = ["data_file1.csv", "data_file2.csv"]  # List of file paths to load
    loaded_data = load_data(file_paths)
    for i, df in enumerate(loaded_data):
        print(f"Data loaded from file {i+1}:")
        print(df.head())  # Displaying first few rows of each loaded DataFrame

