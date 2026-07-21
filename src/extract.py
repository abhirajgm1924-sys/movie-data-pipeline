import pandas as pd

def extract_data(file_path):
    df = pd.read_csv(file_path)
    return df


if __name__ == "__main__":
    file_path = "data/netflix_titles.csv"
    df = extract_data(file_path)

    print(df.head())