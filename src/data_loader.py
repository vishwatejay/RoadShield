from pathlib import Path
import pandas as pd

PROJECT_ROOT = Path(__file__).resolve().parent.parent

RAW_DATA_PATH = PROJECT_ROOT / "data" / "raw" / "accidents_raw.csv"

PROCESSED_DATA_DIR = PROJECT_ROOT / "data" / "processed"

def check_file_exists(file_path: Path) -> bool:
    """
    Check whether the dataset file exists.

    Args:
        file_path (Path): Path to the dataset.

    Returns:
        bool: True if the file exists, otherwise False.
    """
    return file_path.exists()