# Data Analysis for LAS: Day 10

# ---- PART 1 ----

#Preamble: Import necessary libraries
import json

# Load in Seattle Station Code
with open('stations.csv', 'r') as file:
    stations_data = file.readlines()
    for row in stations_data:
        if 'Seattle' in row:
            seattle = row.strip().split(',')
            seattle_code = seattle[2]

# Load in Seattle Measurements from JSON
with open('precipitation.json','r') as file:
    precipitation_data = json.load(file)
    seattle_data = []
    for item in precipitation_data:
        if item['station'] == seattle_code:
            seattle_data.append(item)

# Creates a Dictionary with Measurements per Month
seattle_data_2010 = {'01': [], \
                     '02': [], \
                     '03': [], \
                     '04': [], \
                     '05': [], \
                     '06': [], \
                     '07': [], \
                     '08': [], \
                     '09': [], \
                     '10': [], \
                     '11': [], \
                     '12': []
                     }

months = ['01','02','03','04','05','06','07','08','09','10','11','12']

for measure in seattle_data:
    for month in months:
        if f'2010-{month}' in measure['date']:
            seattle_data_2010[month].append(measure['value'])

# Creates a new dictionary where values are sums of values in seattle_data_2010
seattle_totalMonthlyPrecipitation = {}

for month in months:
    seattle_totalMonthlyPrecipitation[month] = sum(seattle_data_2010[month])

seattle_list = [x for x in seattle_totalMonthlyPrecipitation.values()]

# Saves results to a .json file
with open('Seattle_Precipitation_2010.json', 'w') as outfile:
    json.dump(seattle_list, outfile)

# ---- PART 2 ----

