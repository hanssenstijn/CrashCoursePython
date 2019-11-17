import csv

from matplotlib import pyplot as plt

from datetime import datetime
first_date = datetime.strptime('2018-2-1', '%Y-%m-%d')
print(first_date)

filename = "C:/Users/stijn/Documents/GitHub/CrashCoursePython/Project2/data/sitka_weather_07-2018_simple.csv"
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    print(header_row)

# print temp max column
    dates, highs, lows = [], [], []
    for row in reader:

        current_date = datetime.strptime(row[2], "%Y-%m-%d")
        dates.append(current_date)

        highs.append(row[5])
        lows.append(row[6])

# Plot data.
fig = plt.figure(dpi=128, figsize=(10, 6))
plt.plot(dates, highs, c='red')
plt.plot(dates, lows, c='blue')
# shading inbetween
plt.fill_between(dates, highs, lows, facecolor='gray', alpha=0.1)
plt.title("Daily high temperatures", fontsize=24)
plt.xlabel('Day', fontsize=16)
# automatically makes x-axis readable
fig.autofmt_xdate()
plt.ylabel("Temperature (F)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()

# print with enumerate also the index of each column
for index, column_header in enumerate(header_row):
    print(index, column_header)

