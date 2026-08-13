from pathlib import Path

from src.data_loader import (
    RAW_DATA_PATH,
    PROCESSED_DATA_DIR,
    check_file_exists,
    load_dataset,
)

from src.cleaning import (
    dataset_summary,
    column_statistics,
    convert_datetime_columns,
    extract_time_features,
    clean_dataset,
)

from src.analysis import (
    analyze_severity,
    analyze_time_patterns,
    analyze_weather,
    analyze_locations,
    identify_black_spots,
    generate_project_summary,
)

from src.visualization import (
    plot_severity_distribution,
    plot_accidents_by_hour,
    plot_accidents_by_day,
    plot_accidents_by_month,
    plot_severity_by_time,
    plot_top_states,
    plot_top_cities,
    plot_weather_conditions,
    plot_black_spots,
)

from src.recommendation import (
    generate_recommendations,
    save_recommendations,
)

from src.utils import (
    ensure_directory,
    save_dataframe,
)


print("=" * 70)
print("ROADSHIELD - ROAD ACCIDENT BLACK SPOT ANALYZER")
print("=" * 70)

# ---------------------------------------------------------
# 1. CHECK DATASET
# ---------------------------------------------------------

if not check_file_exists(RAW_DATA_PATH):
    print("❌ Dataset not found!")
    print(f"Expected location: {RAW_DATA_PATH}")
    raise SystemExit

print("\n✅ Dataset found!")

# ---------------------------------------------------------
# 2. CREATE OUTPUT DIRECTORIES
# ---------------------------------------------------------

PROJECT_ROOT = Path(__file__).resolve().parent

PLOTS_DIR = PROJECT_ROOT / "output" / "plots"
REPORTS_DIR = PROJECT_ROOT / "output" / "reports"

ensure_directory(PLOTS_DIR)
ensure_directory(REPORTS_DIR)
ensure_directory(PROCESSED_DATA_DIR)

# ---------------------------------------------------------
# 3. LOAD DATASET
# ---------------------------------------------------------

df = load_dataset(RAW_DATA_PATH)

print("\nFirst 5 rows:")
print(df.head())

print("\nDataset Shape:")
print(df.shape)

# ---------------------------------------------------------
# 4. INITIAL DATASET SUMMARY
# ---------------------------------------------------------

dataset_summary(df)

column_statistics(df)

# ---------------------------------------------------------
# 5. DATETIME PROCESSING
# ---------------------------------------------------------

df = convert_datetime_columns(df)

print("\nDatetime columns converted successfully.")

# ---------------------------------------------------------
# 6. EXTRACT TIME FEATURES
# ---------------------------------------------------------

df = extract_time_features(df)

print("\nTime features created:")
print(
    df[
        [
            "Start_Time",
            "Year",
            "Month",
            "Day",
            "Hour",
            "Day_of_Week",
        ]
    ].head()
)

# ---------------------------------------------------------
# 7. CLEAN DATASET
# ---------------------------------------------------------

df = clean_dataset(df)

print("\nDataset cleaning completed.")

# Save processed dataset
processed_path = PROCESSED_DATA_DIR / "accidents_processed.csv"
df.to_csv(processed_path, index=False)

print(f"Processed dataset saved to: {processed_path}")

# ---------------------------------------------------------
# 8. SEVERITY ANALYSIS
# ---------------------------------------------------------

print("\n" + "=" * 70)
print("SEVERITY ANALYSIS")
print("=" * 70)

severity_counts = analyze_severity(df)

print(severity_counts)

save_dataframe(
    severity_counts.reset_index(),
    REPORTS_DIR / "severity_analysis.csv"
)

# ---------------------------------------------------------
# 9. TIME ANALYSIS
# ---------------------------------------------------------

print("\n" + "=" * 70)
print("TIME ANALYSIS")
print("=" * 70)

hour_analysis = analyze_time_patterns(df, "Hour")
day_analysis = analyze_time_patterns(df, "Day_of_Week")
month_analysis = analyze_time_patterns(df, "Month")
year_analysis = analyze_time_patterns(df, "Year")

print("\nAccidents by Hour:")
print(hour_analysis)

print("\nAccidents by Day:")
print(day_analysis)

print("\nAccidents by Month:")
print(month_analysis)

print("\nAccidents by Year:")
print(year_analysis)

save_dataframe(
    hour_analysis.reset_index(),
    REPORTS_DIR / "accidents_by_hour.csv"
)

save_dataframe(
    day_analysis.reset_index(),
    REPORTS_DIR / "accidents_by_day.csv"
)

save_dataframe(
    month_analysis.reset_index(),
    REPORTS_DIR / "accidents_by_month.csv"
)

save_dataframe(
    year_analysis.reset_index(),
    REPORTS_DIR / "accidents_by_year.csv"
)

# ---------------------------------------------------------
# 10. WEATHER ANALYSIS
# ---------------------------------------------------------

print("\n" + "=" * 70)
print("WEATHER ANALYSIS")
print("=" * 70)

weather_analysis = analyze_weather(df)

print(weather_analysis.head(15))

save_dataframe(
    weather_analysis.reset_index(),
    REPORTS_DIR / "weather_analysis.csv"
)

# ---------------------------------------------------------
# 11. LOCATION ANALYSIS
# ---------------------------------------------------------

print("\n" + "=" * 70)
print("LOCATION ANALYSIS")
print("=" * 70)

state_analysis = analyze_locations(df, "State")
city_analysis = analyze_locations(df, "City")

print("\nTop States:")
print(state_analysis.head(10))

print("\nTop Cities:")
print(city_analysis.head(10))

save_dataframe(
    state_analysis.reset_index(),
    REPORTS_DIR / "state_analysis.csv"
)

save_dataframe(
    city_analysis.reset_index(),
    REPORTS_DIR / "city_analysis.csv"
)

# ---------------------------------------------------------
# 12. BLACK SPOT DETECTION
# ---------------------------------------------------------

print("\n" + "=" * 70)
print("BLACK SPOT ANALYSIS")
print("=" * 70)

black_spots = identify_black_spots(df)

print("\nTop Accident Black Spots:")
print(black_spots.head(15))

save_dataframe(
    black_spots,
    REPORTS_DIR / "black_spots.csv"
)

# ---------------------------------------------------------
# 13. GENERATE PLOTS
# ---------------------------------------------------------

print("\n" + "=" * 70)
print("GENERATING VISUALIZATIONS")
print("=" * 70)

plot_severity_distribution(
    df,
    PLOTS_DIR / "01_severity_distribution.png"
)

plot_accidents_by_hour(
    df,
    PLOTS_DIR / "02_accidents_by_hour.png"
)

plot_accidents_by_day(
    df,
    PLOTS_DIR / "03_accidents_by_day.png"
)

plot_accidents_by_month(
    df,
    PLOTS_DIR / "04_accidents_by_month.png"
)

plot_severity_by_time(
    df,
    PLOTS_DIR / "05_severity_by_hour.png"
)

plot_top_states(
    df,
    PLOTS_DIR / "06_top_states.png"
)

plot_top_cities(
    df,
    PLOTS_DIR / "07_top_cities.png"
)

plot_weather_conditions(
    df,
    PLOTS_DIR / "08_weather_conditions.png"
)

plot_black_spots(
    black_spots,
    PLOTS_DIR / "09_black_spots.png"
)

print("\n✅ All plots generated successfully.")

# ---------------------------------------------------------
# 14. RECOMMENDATIONS
# ---------------------------------------------------------

print("\n" + "=" * 70)
print("SAFETY RECOMMENDATIONS")
print("=" * 70)

recommendations = generate_recommendations(df, black_spots)

for number, recommendation in enumerate(
    recommendations,
    start=1
):
    print(f"{number}. {recommendation}")

save_recommendations(
    recommendations,
    REPORTS_DIR / "recommendations.txt"
)

# ---------------------------------------------------------
# 15. PROJECT SUMMARY
# ---------------------------------------------------------

summary = generate_project_summary(
    df,
    black_spots
)

summary_path = REPORTS_DIR / "project_summary.txt"

with open(summary_path, "w", encoding="utf-8") as file:
    file.write(summary)

print("\nProject summary saved.")

# ---------------------------------------------------------
# FINISHED
# ---------------------------------------------------------

print("\n" + "=" * 70)
print("ROADSHIELD ANALYSIS COMPLETED SUCCESSFULLY")
print("=" * 70)

print("\nGenerated:")
print("✅ Processed dataset")
print("✅ Analysis reports")
print("✅ 9 visualization plots")
print("✅ Black spot analysis")
print("✅ Safety recommendations")
print("✅ Project summary")

print("\nCheck:")
print("output/plots/")
print("output/reports/")
print("data/processed/")