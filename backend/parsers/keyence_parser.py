import pandas as pd

def parse_csv(file_path, delimiter=';', encoding='ISO-8859-1', skip_rows=3):
    """
    Parses a Keyence CSV file.
    """
    df = pd.read_csv(file_path, delimiter=delimiter, encoding=encoding, skiprows=skip_rows)
    
    return df


if __name__ == '__main__':

    file_path = 'data/_examples/auto_csv_Keyence_IM-8020_VIE/examples/keyence1.csv'
    data_df = parse_csv(file_path, skip_rows=3)

    # Display the first 5 rows
    data_df.head()
