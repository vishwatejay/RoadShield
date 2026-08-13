import pandas as pd
import matplotlib.pyplot as plt


def save_plot(
    file_path
) -> None:
    """
    Save and close the current plot.
    """

    plt.tight_layout()
    plt.savefig(
        file_path,
        dpi=300,
        bbox_inches="tight"
    )
    plt.close()


def plot_severity_distribution(
    df: pd.DataFrame,
    file_path
) -> None:

    counts = (
        df["Severity"]
        .value_counts()
        .sort_index()
    )

    plt.figure(figsize=(8, 5))

    counts.plot(
        kind="bar"
    )

    plt.title(
        "Road Accident Severity Distribution"
    )

    plt.xlabel(
        "Severity Level"
    )

    plt.ylabel(
        "Number of Accidents"
    )

    save_plot(file_path)


def plot_accidents_by_hour(
    df: pd.DataFrame,
    file_path
) -> None:

    counts = (
        df["Hour"]
        .value_counts()
        .sort_index()
    )

    plt.figure(figsize=(10, 5))

    counts.plot(
        kind="line",
        marker="o"
    )

    plt.title(
        "Accidents by Hour of Day"
    )

    plt.xlabel(
        "Hour of Day"
    )

    plt.ylabel(
        "Number of Accidents"
    )

    plt.xticks(
        range(24)
    )

    save_plot(file_path)


def plot_accidents_by_day(
    df: pd.DataFrame,
    file_path
) -> None:

    day_order = [
        "Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday",
        "Saturday",
        "Sunday",
    ]

    counts = (
        df["Day_of_Week"]
        .value_counts()
        .reindex(day_order)
    )

    plt.figure(figsize=(10, 5))

    counts.plot(
        kind="bar"
    )

    plt.title(
        "Accidents by Day of Week"
    )

    plt.xlabel(
        "Day"
    )

    plt.ylabel(
        "Number of Accidents"
    )

    save_plot(file_path)


def plot_accidents_by_month(
    df: pd.DataFrame,
    file_path
) -> None:

    counts = (
        df["Month"]
        .value_counts()
        .sort_index()
    )

    plt.figure(figsize=(10, 5))

    counts.plot(
        kind="bar"
    )

    plt.title(
        "Accidents by Month"
    )

    plt.xlabel(
        "Month"
    )

    plt.ylabel(
        "Number of Accidents"
    )

    save_plot(file_path)


def plot_severity_by_time(
    df: pd.DataFrame,
    file_path
) -> None:

    severity_hour = pd.crosstab(
        df["Hour"],
        df["Severity"]
    )

    plt.figure(figsize=(10, 6))

    severity_hour.plot(
        kind="line",
        marker="o",
        ax=plt.gca()
    )

    plt.title(
        "Accident Severity by Hour"
    )

    plt.xlabel(
        "Hour of Day"
    )

    plt.ylabel(
        "Number of Accidents"
    )

    plt.legend(
        title="Severity"
    )

    save_plot(file_path)


def plot_top_states(
    df: pd.DataFrame,
    file_path
) -> None:

    counts = (
        df["State"]
        .value_counts()
        .head(10)
    )

    plt.figure(figsize=(10, 6))

    counts.sort_values().plot(
        kind="barh"
    )

    plt.title(
        "Top 10 States by Accident Count"
    )

    plt.xlabel(
        "Number of Accidents"
    )

    plt.ylabel(
        "State"
    )

    save_plot(file_path)


def plot_top_cities(
    df: pd.DataFrame,
    file_path
) -> None:

    counts = (
        df["City"]
        .value_counts()
        .head(10)
    )

    plt.figure(figsize=(10, 6))

    counts.sort_values().plot(
        kind="barh"
    )

    plt.title(
        "Top 10 Cities by Accident Count"
    )

    plt.xlabel(
        "Number of Accidents"
    )

    plt.ylabel(
        "City"
    )

    save_plot(file_path)


def plot_weather_conditions(
    df: pd.DataFrame,
    file_path
) -> None:

    counts = (
        df["Weather_Condition"]
        .value_counts()
        .head(10)
    )

    plt.figure(figsize=(10, 6))

    counts.sort_values().plot(
        kind="barh"
    )

    plt.title(
        "Top 10 Weather Conditions During Accidents"
    )

    plt.xlabel(
        "Number of Accidents"
    )

    plt.ylabel(
        "Weather Condition"
    )

    save_plot(file_path)


def plot_black_spots(
    black_spots: pd.DataFrame,
    file_path
) -> None:

    top = (
        black_spots
        .head(10)
        .copy()
    )

    labels = [
        f"{lat:.3f}, {lng:.3f}"
        for lat, lng
        in zip(
            top["Latitude"],
            top["Longitude"]
        )
    ]

    plt.figure(figsize=(10, 6))

    plt.barh(
        labels[::-1],
        top["Risk_Score"].values[::-1]
    )

    plt.title(
        "Top 10 Accident Black Spots"
    )

    plt.xlabel(
        "Risk Score"
    )

    plt.ylabel(
        "Approximate Location"
    )

    save_plot(file_path)