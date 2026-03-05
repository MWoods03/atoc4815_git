"""
Collaborative Weather Analysis
ATOC 4815/5815 - Git Collaboration Exercise

Instructions:
  - Partner A: Complete the functions in SECTION A (temperature analysis)
  - Partner B: Complete the functions in SECTION B (wind chill & heat index)
  - Each partner works on their OWN branch, then merge via pull requests.

When both sections are complete, run:
    python collaborative_analysis.py

The main() function calls everything and prints a full weather report.
"""

# ============================================================
# SECTION A  --  Partner A: Temperature Analysis
# ============================================================

def fahrenheit_to_celsius(temp_f):
    """Convert a temperature from Fahrenheit to Celsius.

    Formula: C = (F - 32) * 5/9

    Parameters
    ----------
    temp_f : float
        Temperature in Fahrenheit.

    Returns
    -------
    float
        Temperature in Celsius.
    """
    # TODO (Partner A): implement the conversion

    celsius = (temp_f - 32) * 5/9

    return celsius


def celsius_to_fahrenheit(temp_c):
    """Convert a temperature from Celsius to Fahrenheit.

    Formula: F = C * 9/5 + 32

    Parameters
    ----------
    temp_c : float
        Temperature in Celsius.

    Returns
    -------
    float
        Temperature in Fahrenheit.
    """
    # TODO (Partner A): implement the conversion
    fahrenheit = temp_c * 9/5 + 32

    return fahrenheit


def daily_temp_range(high_f, low_f):
    """Calculate the daily temperature range in both F and C.

    Parameters
    ----------
    high_f : float
        Daily high temperature in Fahrenheit.
    low_f : float
        Daily low temperature in Fahrenheit.

    Returns
    -------
    dict
        {"range_f": float, "range_c": float}
    """
    # TODO (Partner A): compute range in F and convert to C
    range_f = high_f - low_f

    range_c = fahrenheit_to_celsius(high_f) - fahrenheit_to_celsius(low_f)

    return {f"range_f: {range_f}", f"range_c: {range_c}"}


# ============================================================
# SECTION B  --  Partner B: Wind Chill & Heat Index
# ============================================================

def wind_chill(temp_f, wind_mph):
    """Calculate the wind chill index (valid for temp <= 50 F and wind >= 3 mph).

    NWS formula:
        WC = 35.74 + 0.6215*T - 35.75*(V^0.16) + 0.4275*T*(V^0.16)

    Parameters
    ----------
    temp_f : float
        Air temperature in Fahrenheit.
    wind_mph : float
        Wind speed in miles per hour.

    Returns
    -------
    float or None
        Wind chill in Fahrenheit, or None if inputs are out of range.
    """
    # TODO (Partner B): implement the NWS wind chill formula
    # Return None if temp_f > 50 or wind_mph < 3
    pass


def heat_index(temp_f, rh):
    """Calculate a simplified heat index (valid for temp >= 80 F).

    Simplified Rothfusz regression:
        HI = -42.379 + 2.04901523*T + 10.14333127*RH
             - 0.22475541*T*RH - 0.00683783*T^2 - 0.05481717*RH^2
             + 0.00122874*T^2*RH + 0.00085282*T*RH^2
             - 0.00000199*T^2*RH^2

    Parameters
    ----------
    temp_f : float
        Air temperature in Fahrenheit.
    rh : float
        Relative humidity in percent (0-100).

    Returns
    -------
    float or None
        Heat index in Fahrenheit, or None if temp_f < 80.
    """
    # TODO (Partner B): implement the simplified heat index
    # Return None if temp_f < 80
    pass


# ============================================================
# MAIN  --  Runs both sections to produce a weather report
# ============================================================

def main():
    print("=" * 50)
    print("  Collaborative Weather Analysis Report")
    print("  ATOC 4815/5815")
    print("=" * 50)

    # ---- Section A results ----
    print("\n--- Temperature Conversions (Partner A) ---")

    boiling_c = fahrenheit_to_celsius(212.0)
    freezing_c = fahrenheit_to_celsius(32.0)
    body_f = celsius_to_fahrenheit(37.0)
    print(f"  Boiling point:  212 F = {boiling_c} C")
    print(f"  Freezing point:  32 F = {freezing_c} C")
    print(f"  Body temp:       37 C = {body_f} F")

    high, low = 45.0, 18.0
    tr = daily_temp_range(high, low)
    print(f"\n  Boulder daily high/low: {high} F / {low} F")
    print(f"  Daily range: {tr}")

    # ---- Section B results ----
    print("\n--- Wind Chill & Heat Index (Partner B) ---")

    wc = wind_chill(20.0, 15.0)
    print(f"  Wind chill at 20 F, 15 mph wind: {wc}")

    wc_none = wind_chill(55.0, 10.0)
    print(f"  Wind chill at 55 F (out of range): {wc_none}")

    hi = heat_index(95.0, 60.0)
    print(f"  Heat index at 95 F, 60% RH: {hi}")

    hi_none = heat_index(75.0, 50.0)
    print(f"  Heat index at 75 F (out of range): {hi_none}")

    print("\n" + "=" * 50)
    print("  Report complete!")
    print("=" * 50)


if __name__ == "__main__":
    main()
