from extract import extract_data


def transform_data(file_path):
    df = extract_data(file_path)

    print("Shape:", df.shape)
    print("Duplicate rows:", df.duplicated().sum())

    df = df.drop_duplicates()

    df["director"] = df["director"].fillna("Unknown")
    df["country"] = df["country"].fillna("Unknown")
    df["rating"] = df["rating"].fillna("Unknown")
     
    df = df[
    [
        "show_id",
        "type",
        "title",
        "director",
        "country",
        "release_year",
        "rating",
        "duration",
        "listed_in",
    ]
]
    
    print("\nMissing values:")
    print(df.isnull().sum())

    print("\nMissing values after cleaning:")
    print(df[["director", "country", "rating"]].isnull().sum())

    print("\nColumns after selection:")
    print(df.columns)

    print("Final shape:", df.shape)



    return df


if __name__ == "__main__":
    file_path = "data/netflix_titles.csv"

    df = transform_data(file_path)