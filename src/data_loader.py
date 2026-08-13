from pathlib import Path
import pandas as pd


PROJECT_ROOT = Path(__file__).resolve().parent.parent

RAW_DATA_PATH = (
    PROJECT_ROOT
    / "data"
    / "raw"
    / "accidents_raw.csv"
)

PROCESSED_DATA_DIR = (
    PROJECT_ROOT
    / "data"
    / "processed"
)


def check_file_exists(file_path: Path) -> bool:
    """
    Check whether a file exists.
    """

    return file_path.exists()


def load_dataset(
    file_path: Path,
    nrows: int | None = 10000
) -> pd.DataFrame:
    """
    Load accident dataset from CSV.

    By default, 10,000 rows are loaded for the
    development version of RoadShield.
    """

    if not check_file_exists(file_path):
        raise FileNotFoundError(
            f"Dataset not found: {file_path}"
        )

    print("Loading dataset...")

    df = pd.read_csv(
        file_path,
        nrows=nrows
    )

    print(
        f"Loaded {len(df):,} rows successfully!"
    )

    return df