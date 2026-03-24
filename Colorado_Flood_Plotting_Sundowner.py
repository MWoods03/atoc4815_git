# Import modules
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


# This script takes data from the CU Boulder Sundowner, imports data from September of 3 different years surrounding (including) the data from 2013, which was the year of large record breaking
# rainfalls and flooding. These floods led to billions in damages and affected many Boulder and Colorado residents.

# My final plot visualizes the rainfall by day throughout the month of September in each of the years 2012, 2013, and 2014. It also includes an overplot of the cumulative rainfall within
# the month of September for each year



# Import Data from the Sundowner

days = ['01','02','03','04','05','06','07','08','09','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30'] # Each day of the month of September as a string for use in the url to import the data
years = ['2012','2013','2014'] # Each year that I am interested in importing data from

# Make dictionaries to store data in. The keys will be the date for the data that I am acessing
dataframes_2012 = {} # Year before the flood for comparison
dataframes_2013 = {} # Year of the flood
dataframes_2014 = {} # Year after the flood for comparison

for year in years: # Loop each year 2012, 2013, 2014
    for day in days: # Loop each day 01 - 30 for the month of September
    
        url = f"https://sundowner.colorado.edu/weather/atoc1/wxobs{year}09{day}.txt"
        df = pd.read_fwf(url, header=[0, 1], skiprows=[2])


        date_col = [c for c in df.columns if c[1] == "Date"][0]
        time_col = [c for c in df.columns if c[1] == "Time"][0]
    
        t = (
            df[time_col]
            .astype(str)
            .str.strip()
            .str.replace(r"a$", "AM", regex=True)
            .str.replace(r"p$", "PM", regex=True)
        )

        dt = pd.to_datetime(
            df[date_col].astype(str).str.strip() + " " + t,
            format="%m/%d/%y %I:%M%p",
            errors="coerce",
        )

        df = df.set_index(dt).drop(columns=[date_col, time_col])
        df.index.name = "datetime"

        df.columns = [
            "_".join([str(a).strip(), str(b).strip()]).replace(" ", "_").strip("_")
            for a, b in df.columns
        ]

    # Set the day's data equal to the day in the correct year dictionary
        if year == '2012':
            dataframes_2012[day] = df

        elif year == '2013':
            dataframes_2013[day] = df

        else:
            dataframes_2014[day] = df




#  Create Plot and Overplot

dataframes_2013['13']['Unnamed:_17_level_0_Rain'] = 0.00118055555556
# I've set this to this value because it will result in np.sum() in the loop giving a final value of 0.34 inches which is what is displayed on the Sundowner Weather network page as total rainfall for 09/13/2013
# There was some issue with reading in this data for some reason due to the keys being split apart differently


# Arrays to store total daily rainfall values
rf_2012 = np.zeros(30) # Rainfall for September 2012
rf_2013 = np.zeros(30) # 2013
rf_2014 = np.zeros(30) # 2014


plt.figure(figsize=(10,5)) # Set the figure size so it is easier to read my x axis

for day in days:

    # Plot individual Rainfal Days as Bar Plots
    plt.bar(day, np.sum(dataframes_2013[day]['Unnamed:_17_level_0_Rain']), color = 'navy', label = '2013' if day == days[0] else None) # Plot flood year. I set the legend only if this is the first loop otherwise is doesn't do anything
    plt.bar(day, np.sum(dataframes_2012[day]['Unnamed:_17_level_0_Rain']), color = 'darkcyan', label = '2012' if day == days[0] else None) # Plot previous year
    plt.bar(day, np.sum(dataframes_2014[day]['Unnamed:_17_level_0_Rain']), color= 'maroon', label = '2014' if day == days[0] else None) # Plot year after


    # Add each day's rainfall as a value in the total rainfall lists to use later in overplotting
    rf_2012[int(day)-1] = ( np.sum(dataframes_2012[day]['Unnamed:_17_level_0_Rain']) ) # Convert to int and set index by subtracting 1 because the first day will be int('01') and I want it to be index 0
    rf_2013[int(day)-1] = ( np.sum(dataframes_2013[day]['Unnamed:_17_level_0_Rain']) )
    rf_2014[int(day)-1] = ( np.sum(dataframes_2014[day]['Unnamed:_17_level_0_Rain']) )


    plt.title('September Rainfall by Year Surrounding 2013 Colorado Front Range Flood')
    plt.xlabel('Date in September')
    plt.ylabel('Daily Total Rainfall (inches)')


# Overplot Cumulative Line for the Month
plt.plot(days, np.cumsum(rf_2013), label = 'Sept. Cumulative 2013', color='navy')
plt.plot(days, np.cumsum(rf_2012), label = 'Sept. Cumulative 2012', color='darkcyan')
plt.plot(days, np.cumsum(rf_2014), label = 'Sept. Cumulative 2014', color='maroon')

plt.legend()
plt.show()