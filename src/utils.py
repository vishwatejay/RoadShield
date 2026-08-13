from pathlib import Path
import pandas as pd


def ensure_directory(
    directory: Path
) -> None:
    """
    Create directory if it does not exist.
    """

    directory.mkdir(
        parents=True,
        exist_ok=True
    )


def save_dataframe(
    df: pd.DataFrame,
    file_path: Path
) -> None:
    """
    Save a DataFrame as a CSV file.
    """

    ensure_directory(
        file_path.parent
    )

    df.to_csv(
        file_path,
        index=False
    )