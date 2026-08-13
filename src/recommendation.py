import pandas as pd


def generate_recommendations(
    df: pd.DataFrame,
    black_spots: pd.DataFrame
) -> list[str]:
    """
    Generate data-driven road safety recommendations.
    """

    recommendations = []

    # --------------------------------------------------
    # TIME
    # --------------------------------------------------

    busiest_hour = (
        df["Hour"]
        .value_counts()
        .idxmax()
    )

    recommendations.append(
        f"Prioritize traffic monitoring and safety "
        f"measures around {busiest_hour}:00, "
        f"the hour with the highest number of "
        f"recorded accidents."
    )

    # --------------------------------------------------
    # DAY
    # --------------------------------------------------

    busiest_day = (
        df["Day_of_Week"]
        .value_counts()
        .idxmax()
    )

    recommendations.append(
        f"Increase traffic safety monitoring on "
        f"{busiest_day}, which has the highest "
        f"accident frequency in the analyzed data."
    )

    # --------------------------------------------------
    # NIGHT
    # --------------------------------------------------

    if "Sunrise_Sunset" in df.columns:

        night_count = (
            df["Sunrise_Sunset"]
            .eq("Night")
            .sum()
        )

        if night_count > 0:

            recommendations.append(
                "Improve road lighting, visibility "
                "and night-time warning systems in "
                "locations with frequent night accidents."
            )

    # --------------------------------------------------
    # TRAFFIC SIGNAL
    # --------------------------------------------------

    if "Traffic_Signal" in df.columns:

        signal_count = (
            df["Traffic_Signal"]
            .eq(True)
            .sum()
        )

        if signal_count > 0:

            recommendations.append(
                "Review traffic-signal intersections "
                "with high accident frequency and "
                "evaluate signal timing and road design."
            )

    # --------------------------------------------------
    # WEATHER
    # --------------------------------------------------

    if "Weather_Condition" in df.columns:

        weather = (
            df["Weather_Condition"]
            .value_counts()
        )

        if len(weather) > 0:

            condition = weather.index[0]

            recommendations.append(
                f"Monitor road safety conditions "
                f"during {condition}, the most frequently "
                f"recorded weather condition in the dataset."
            )

    # --------------------------------------------------
    # BLACK SPOTS
    # --------------------------------------------------

    if len(black_spots) > 0:

        recommendations.append(
            "Prioritize engineering inspections and "
            "safety improvements at the highest-ranked "
            "accident black spots identified by RoadShield."
        )

    return recommendations


def save_recommendations(
    recommendations: list[str],
    file_path
) -> None:
    """
    Save recommendations to a text file.
    """

    with open(
        file_path,
        "w",
        encoding="utf-8"
    ) as file:

        file.write(
            "ROADSHIELD SAFETY RECOMMENDATIONS\n"
        )

        file.write(
            "=" * 50 + "\n\n"
        )

        for number, recommendation in enumerate(
            recommendations,
            start=1
        ):

            file.write(
                f"{number}. {recommendation}\n\n"
            )