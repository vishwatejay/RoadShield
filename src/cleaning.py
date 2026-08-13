import pandas as pd


def dataset_summary(df: pd.DataFrame) -> None:
    """
    Display basic information about the dataset.
    """

    print("\n" + "=" * 60)
    print("DATASET SUMMARY")
    print("=" * 60)

    print(f"\nRows    : {df.shape[0]:,}")
    print(f"Columns : {df.shape[1]}")

    print("\nData Types")
    print(df.dtypes)

    print("\nMissing Values")
    print(df.isnull().sum())

    print("\nDuplicate Rows")
    print(df.duplicated().sum())


def column_statistics(df: pd.DataFrame) -> None:
    """
    Display numerical and categorical statistics.
    """

    print("\n" + "=" * 60)
    print("NUMERICAL STATISTICS")
    print("=" * 60)

    print(df.describe())

    print("\n" + "=" * 60)
    print("CATEGORICAL STATISTICS")
    print("=" * 60)

    print(
        df.describe(
            include="object"
        )
    )


def convert_datetime_columns(
    df: pd.DataFrame
) -> pd.DataFrame:
    """
    Convert date/time columns to datetime format.
    """

    datetime_columns = [
        "Start_Time",
        "End_Time",
        "Weather_Timestamp",
    ]

    for column in datetime_columns:

        if column in df.columns:

            df[column] = pd.to_datetime(
                df[column],
                errors="coerce"
            )

    return df


def extract_time_features(
    df: pd.DataFrame
) -> pd.DataFrame:
    """
    Extract useful time features from Start_Time.
    """

    df["Year"] = df["Start_Time"].dt.year

    df["Month"] = df["Start_Time"].dt.month

    df["Day"] = df["Start_Time"].dt.day

    df["Hour"] = df["Start_Time"].dt.hour

    df["Day_of_Week"] = (
        df["Start_Time"].dt.day_name()
    )

    return df


def clean_dataset(
    df: pd.DataFrame
) -> pd.DataFrame:
    """
    Perform safe basic cleaning.

    Columns that are completely missing are removed.
    Rows are not blindly deleted because missing
    weather information does not mean an accident
    record is invalid.
    """

    # Remove columns that contain no information
    completely_missing = [
        column
        for column in df.columns
        if df[column].isna().all()
    ]

    if completely_missing:
        df = df.drop(
            columns=completely_missing
        )

    # Remove completely duplicated rows
    df = df.drop_duplicates()

    # Fill small categorical missing values
    categorical_columns = [
        "Weather_Condition",
        "Wind_Direction",
        "Timezone",
        "Airport_Code",
        "Zipcode",
    ]

    for column in categorical_columns:

        if column in df.columns:

            df[column] = df[column].fillna(
                "Unknown"
            )

    return df