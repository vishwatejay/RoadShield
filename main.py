from src.data_loader import check_file_exists, RAW_DATA_PATH

print("RoadShield - Road Accident Black Spot Analyzer")
print("-" * 50)

if check_file_exists(RAW_DATA_PATH):
    print("✅ Dataset found!")
else:
    print("❌ Dataset not found!")