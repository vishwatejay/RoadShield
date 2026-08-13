import pandas as pd


def analyze_severity(
    df: pd.DataFrame
) -> pd.Series:
    """
    Count accidents by severity.
    """

    return (
        df["Severity"]
        .value_counts()
        .sort_index()
    )


def analyze_time_patterns(
    df: pd.DataFrame,
    column: str
) -> pd.Series:
    """
    Count accidents according to a time feature.
    """

    return (
        df[column]
        .value_counts()
        .sort_index()
    )


def analyze_weather(
    df: pd.DataFrame
) -> pd.Series:
    """
    Count accidents by weather condition.
    """

    return (
        df["Weather_Condition"]
        .value_counts()
    )


def analyze_locations(
    df: pd.DataFrame,
    column: str
) -> pd.Series:
    """
    Count accidents by a geographic field.
    """

    return (
        df[column]
        .value_counts()
    )


def identify_black_spots(
    df: pd.DataFrame
) -> pd.DataFrame:
    """
    Identify accident black spots using
    rounded latitude and longitude.

    A location with more accidents receives
    a higher accident count.

    Severity is also included in the score so
    locations with more severe accidents receive
    greater priority.
    """

    location_df = df[
        [
            "Start_Lat",
            "Start_Lng",
            "Severity",
        ]
    ].copy()

    location_df["Latitude"] = (
        location_df["Start_Lat"]
        .round(3)
    )

    location_df["Longitude"] = (
        location_df["Start_Lng"]
        .round(3)
    )

    grouped = (
        location_df
        .groupby(
            [
                "Latitude",
                "Longitude",
            ]
        )
        .agg(
            Accident_Count=(
                "Severity",
                "count"
            ),
            Average_Severity=(
                "Severity",
                "mean"
            ),
            Severity_Score=(
                "Severity",
                "sum"
            ),
        )
        .reset_index()
    )

    grouped["Risk_Score"] = (
        grouped["Accident_Count"]
        * grouped["Average_Severity"]
    )

    grouped = grouped.sort_values(
        "Risk_Score",
        ascending=False
    )

    return grouped.head(20)


def generate_project_summary(
    df: pd.DataFrame,
    black_spots: pd.DataFrame
) -> str:
    """
    Generate a text summary for the project report.
    """

    total_accidents = len(df)

    severity_counts = (
        df["Severity"]
        .value_counts()
        .sort_index()
    )

    most_common_severity = (
        severity_counts.idxmax()
    )

    most_common_hour = (
        df["Hour"]
        .value_counts()
        .idxmax()
    )

    most_common_day = (
        df["Day_of_Week"]
        .value_counts()
        .idxmax()
    )

    most_common_month = (
        df["Month"]
        .value_counts()
        .idxmax()
    )

    most_common_weather = (
        df["Weather_Condition"]
        .value_counts()
        .idxmax()
    )

    most_common_state = (
        df["State"]
        .value_counts()
        .idxmax()
    )

    summary = f"""
ROADSHIELD
Road Accident Black Spot Analyzer
========================================

Dataset
----------------------------------------
Total accident records analyzed: {total_accidents:,}
Number of columns: {df.shape[1]}

Key Findings
----------------------------------------
Most common accident severity: {most_common_severity}
Most common accident hour: {most_common_hour}:00
Most common accident day: {most_common_day}
Most common accident month: {most_common_month}
Most common weather condition: {most_common_weather}
State with most recorded accidents: {most_common_state}

Black Spot Detection
----------------------------------------
Top black spots were identified using
accident coordinates rounded to three decimal
places.

The ranking considers both:
1. Accident frequency
2. Average accident severity

This produces a Risk Score that helps
prioritize locations requiring attention.

Purpose
----------------------------------------
RoadShield analyzes historical accident data
to identify accident patterns, high-risk
locations, environmental conditions and
time periods.

The results can support:
- Road safety planning
- Traffic management
- Infrastructure improvement
- Accident prevention
- Emergency response planning
"""

    return summary