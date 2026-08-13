# RoadShield - Road Accident Black Spot Analyzer

RoadShield is a Python-based road accident analysis project that explores accident patterns, severity, location, time, weather conditions, and road infrastructure to identify potential accident black spots and generate safety-oriented recommendations.

---

## 🎯 Objective

The main objective of RoadShield is to analyze road accident data and identify patterns that can help understand high-risk locations and conditions.

The project focuses on:

- Accident severity analysis
- Accident-prone locations
- Time-based accident patterns
- Weather-related factors
- Road infrastructure factors
- Potential accident black spots
- Safety recommendations

---

## 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Git
- GitHub

---

## 📊 Dataset

The project currently analyzes **10,000 accident records** containing **46 features**.

The dataset includes information about:

- Accident severity
- Date and time
- Latitude and longitude
- Location
- Weather conditions
- Temperature
- Humidity
- Visibility
- Wind speed
- Precipitation
- Road infrastructure
- Traffic signals
- Junctions
- Railway crossings
- Sunrise and twilight conditions

---

## 📁 Project Structure

```text
RoadShield/
│
├── data/
│   ├── raw/
│   │   └── accidents_raw.csv
│   │
│   └── processed/
│
├── output/
│   ├── plots/
│   └── reports/
│
├── src/
│   ├── __init__.py
│   ├── data_loader.py
│   ├── cleaning.py
│   ├── analysis.py
│   ├── visualization.py
│   ├── recommendation.py
│   └── utils.py
│
├── main.py
├── requirements.txt
├── .gitignore
└── README.md
