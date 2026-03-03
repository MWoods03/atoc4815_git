"""
Boulder January 2025 Temperature Analysis
ATOC 4815/5815 - Git Practice Exercise 1

Instructions:
    1. Add your name below
    2. Complete the TODO sections
    3. Run the script to check your work
    4. Use git to save your changes!
"""

# TODO: Add your name here
STUDENT_NAME = "Matthew Woods"  # Example: "Alice Johnson"


def load_temperatures(filepath):
    """Load temperature data from CSV file.

    Returns list of dictionaries with date, high_f, low_f, precip_in.
    """
    data = []
    with open(filepath, "r") as f:
        header = f.readline().strip().split(",")
        for line in f:
            values = line.strip().split(",")
            row = {
                "date": values[0],
                "high_f": float(values[1]),
                "low_f": float(values[2]),
                "precip_in": float(values[3]),
            }
            data.append(row)
    return data


def average_high(data):
    """Calculate the average high temperature.

    Args:
        data: list of dictionaries from load_temperatures()

    Returns:
        Average high temperature in Fahrenheit, or None if not implemented.
    """
    # TODO: Calculate the average high temperature
    # Hint: sum up all the high_f values and divide by the number of days
    # Hint: use data[i]["high_f"] to get the high temp for day i
    result = None
    return result


def max_temperature(data):
    """Find the highest temperature recorded in January.

    Args:
        data: list of dictionaries from load_temperatures()

    Returns:
        The maximum high temperature in Fahrenheit, or None if not implemented.
    """
    # TODO: Find the maximum high temperature
    # Hint: loop through data and track the highest high_f value
    result = None
    return result


def min_temperature(data):
    """Find the lowest temperature recorded in January.

    Args:
        data: list of dictionaries from load_temperatures()

    Returns:
        The minimum low temperature in Fahrenheit, or None if not implemented.
    """
    # TODO: Find the minimum low temperature
    # Hint: loop through data and track the lowest low_f value
    result = None
    return result


# ---- Run the analysis ----
if __name__ == "__main__":
    print("=" * 50)
    print("Boulder January 2025 Temperature Analysis")
    print("=" * 50)

    if STUDENT_NAME:
        print(f"Analyst: {STUDENT_NAME}")
    else:
        print("NOTE: Add your name to STUDENT_NAME at the top!")

    print()

    data = load_temperatures("data/boulder_jan2025.csv")
    print(f"Loaded {len(data)} days of data")
    print()

    avg = average_high(data)
    if avg is not None:
        print(f"Average high temperature: {avg:.1f} F")
    else:
        print("Average high: not yet implemented (complete the TODO!)")

    mx = max_temperature(data)
    if mx is not None:
        print(f"Highest temperature:      {mx:.1f} F")
    else:
        print("Max temperature:  not yet implemented (complete the TODO!)")

    mn = min_temperature(data)
    if mn is not None:
        print(f"Lowest temperature:       {mn:.1f} F")
    else:
        print("Min temperature:  not yet implemented (complete the TODO!)")

    print()
    print("Done! Now use git to save your work:")
    print("  git status")
    print("  git add boulder_temperatures.py")
    print('  git commit -m "Complete boulder temperature analysis"')
    print("  git push")
