# Data Analysis for LAS: Day 10

# ---- PART 1 ----

#Preamble: Import necessary libraries
import json

# Load in Station Codes
with open('stations.csv', 'r') as file:
    stations_data = file.readlines()
    for row in stations_data:
        if 'Seattle' in row:
            seattle = row.strip().split(',')
            seattle_code = seattle[2]
            seattle_state = seattle[1]
        if 'Cincinnati' in row:
            cincinnati = row.strip().split(',')
            cincinnati_code = cincinnati[2]
            cincinnati_state = cincinnati[1]
        if 'Maui' in row:
            maui = row.strip().split(',')
            maui_code = maui[2]
            maui_state = maui[1]
        if 'San Diego' in row:
            san_diego = row.strip().split(',')
            san_diego_code = san_diego[2]
            san_diego_state = san_diego[1]

# Load in Measurements from JSON
with open('precipitation.json','r') as file:
    precipitation_data = json.load(file)
    seattle_data = []
    cincinnati_data = []
    san_diego_data =[]
    maui_data = []
    for item in precipitation_data:
        if item['station'] == seattle_code:
            seattle_data.append(item)
        elif item['station'] == cincinnati_code:
            cincinnati_data.append(item)
        elif item['station'] == san_diego_code:
            san_diego_data.append(item)
        else:
            maui_data.append(item)

# Creates Lists with Total Precipitation per Month
months = ['01','02','03','04','05','06','07','08','09','10','11','12']

seattle_list = [0 for i in range(12)]
cincinnati_list = [0 for i in range(12)]
san_diego_list = [0 for i in range(12)]
maui_list = [0 for i in range(12)]

for measure in seattle_data:
    for month in months:
        if f'2010-{month}' in measure['date']:
            seattle_list[int(month)-1] += (measure['value'])

for measure in cincinnati_data:
    for month in months:
        if f'2010-{month}' in measure['date']:
            cincinnati_list[int(month)-1] += (measure['value'])

for measure in san_diego_data:
    for month in months:
        if f'2010-{month}' in measure['date']:
            san_diego_list[int(month)-1] += (measure['value'])

for measure in maui_data:
    for month in months:
        if f'2010-{month}' in measure['date']:
            maui_list[int(month)-1] += (measure['value'])

# Saves results to a .json file
with open('Seattle_Precipitation_2010.json', 'w') as outfile:
    json.dump(seattle_list, outfile)

# ---- PART 2 ----

# Calculates the sum of the precipitation over the whole year
seattle_totalprecipitation_2010 = sum(seattle_list)
cincinnati_totalprecipitation_2010 = sum(cincinnati_list)
san_diego_totalprecipitation_2010 = sum(san_diego_list)
maui_totalprecipitation_2010 = sum(maui_list)

# Calculates relative precipitation per month (Pct)
seattle_precipitation_pct = [round((x/seattle_totalprecipitation_2010), ndigits = 2) for x in seattle_list]
cincinnati_precipitation_pct = [round((x/cincinnati_totalprecipitation_2010), ndigits = 2) for x in cincinnati_list]
san_diego_precipitation_pct = [round((x/san_diego_totalprecipitation_2010), ndigits = 2) for x in san_diego_list]
maui_precipitation_pct = [round((x/maui_totalprecipitation_2010), ndigits = 2) for x in maui_list]

# ---- Part 3 ----

# Calculates relative precipitation per location in 2010
total_precipitation_2010 = cincinnati_totalprecipitation_2010 + seattle_totalprecipitation_2010 + \
                           san_diego_totalprecipitation_2010 + maui_totalprecipitation_2010

cincinnati_totalprecipitation_pct = round((cincinnati_totalprecipitation_2010/total_precipitation_2010), ndigits = 2)
seattle_totalprecipitation_pct = round((seattle_totalprecipitation_2010/total_precipitation_2010), ndigits = 2)
san_diego_totalprecipitation_pct = round((seattle_totalprecipitation_2010/total_precipitation_2010), ndigits = 2)
maui_totalprecipitation_pct = round((maui_totalprecipitation_2010/total_precipitation_2010), ndigits = 2)

# Creates Master Dictionary

cities = ['Cincinatti', 'Seattle', 'San Diego', 'Maui']
station = [cincinnati_code, seattle_code, san_diego_code, maui_code]
states = [cincinnati_state, seattle_state, san_diego_state, maui_state]
totalMonthlyPrecipitation = [cincinnati_list, seattle_list, san_diego_list, maui_list]
relativeMonthlyPrecipitation = [cincinnati_precipitation_pct, seattle_precipitation_pct, san_diego_precipitation_pct, maui_precipitation_pct]
totalYearlyPrecipitation = [cincinnati_totalprecipitation_2010, seattle_totalprecipitation_2010, san_diego_totalprecipitation_2010, maui_totalprecipitation_2010]
relativeYearlyPrecipitation = [cincinnati_totalprecipitation_pct, seattle_totalprecipitation_pct, san_diego_totalprecipitation_2010, maui_totalprecipitation_2010]

Precipitation_2010 = {}

for i in range(4):
    Precipitation_2010[cities[i]] = {\
        'station': station[i],\
        'state': states[i],\
        'totalMonthlyPrecipitation': totalMonthlyPrecipitation[i],\
        'relativeMonthlyPrecipitation': relativeMonthlyPrecipitation[i],\
        'totalYearlyPrecipitation': totalYearlyPrecipitation[i],\
        'relativeYearlyPrecipitation': relativeYearlyPrecipitation[i]}

with open('results.json', 'w') as outfile:
    json.dump(Precipitation_2010, outfile)