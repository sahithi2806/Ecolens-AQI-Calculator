#file name aqi.py

def calculate_individual_aqi(c_low, c_high, aqi_low, aqi_high, concentration):
    """Calculate AQI for a pollutant using linear interpolation."""
    return round(((aqi_high - aqi_low) / (c_high - c_low)) * (concentration - c_low) + aqi_low)


def calculate_aqi_for_all(pollutant_conc):
    """
    pollutant_conc: dict of pollutant concentrations, e.g.
    {"PM2.5": 45, "PM10": 120, "CO": 2.5, "SO2": 60, "NO2": 90, "O3": 170}
    """
    breakpoints = {
        "PM2.5": [(0, 30, 0, 50),(31, 60, 51, 100),(61, 90, 101, 200),
                  (91, 120, 201, 300),(121, 250, 301, 400),(251, 350, 401, 500)],
        "PM10": [(0, 50, 0, 50),(51, 100, 51, 100),(101, 250, 101, 200),
                 (251, 350, 201, 300),(351, 430, 301, 400),(431, 500, 401, 500)],
        "CO":   [(0, 1, 0, 50),(1.1, 2, 51, 100),(2.1, 10, 101, 200),
                 (10.1, 17, 201, 300),(17.1, 34, 301, 400),(34.1, 50, 401, 500)],
        "SO2":  [(0, 40, 0, 50),(41, 80, 51, 100),(81, 380, 101, 200),
                 (381, 800, 201, 300),(801, 1600, 301, 400),(1601, 2000, 401, 500)],
        "NO2":  [(0, 40, 0, 50),(41, 80, 51, 100),(81, 180, 101, 200),
                 (181, 280, 201, 300),(281, 400, 301, 400),(401, 500, 401, 500)],
        "O3":   [(0, 50, 0, 50),(51, 100, 51, 100),(101, 168, 101, 200),
                 (169, 208, 201, 300),(209, 748, 301, 400),(749, 1000, 401, 500)]
    }

    aqi_values = {}
    for pollutant, val in pollutant_conc.items():
        if val is None:
            aqi_values[pollutant] = "No Data"
            continue
        for c_low, c_high, aqi_low, aqi_high in breakpoints.get(pollutant, []):
            if c_low <= val <= c_high:
                aqi = calculate_individual_aqi(c_low, c_high, aqi_low, aqi_high, val)
                aqi_values[pollutant] = aqi
                break
        else:
            aqi_values[pollutant] = "Out of Range"
    
    return aqi_values


def calculate_overall_aqi(aqi_values):
    """Get the overall AQI = max of all valid AQIs."""
    valid_aqis = [v for v in aqi_values.values() if isinstance(v, int)]
    return max(valid_aqis) if valid_aqis else "No Data"


def categorize_aqi(aqi):
    """Return AQI category based on CPCB ranges."""
    if aqi == "No Data":
        return "No Data"
    if aqi <= 50: return "Good"
    elif aqi <= 100: return "Satisfactory"
    elif aqi <= 200: return "Moderate"
    elif aqi <= 300: return "Poor"
    elif aqi <= 400: return "Very Poor"
    else: return "Severe"


# ---------------- Example Usage ----------------
if __name__ == "__main__":
    pollutant_conc = {
        "PM2.5": 45,
        "PM10": 120,
        "CO": 2.5,
        "SO2": 60,
        "NO2": 90,
        "O3": 170
    }

    aqi_values = calculate_aqi_for_all(pollutant_conc)
    overall_aqi = calculate_overall_aqi(aqi_values)
    category = categorize_aqi(overall_aqi)

    print("Individual AQIs:", aqi_values)
    print("Overall AQI:", overall_aqi, "-", category)