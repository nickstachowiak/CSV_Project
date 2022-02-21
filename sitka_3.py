# changing the file to include all the data for the year of 2018
# change the title to - Daily high and low temperatures - 2018
# extract low temps from the file and add to chart
# shade in the area between high and low

from datetime import datetime
import csv

open_file = open("sitka_weather_2018_simple.csv", "r")

csv_file = csv.reader(open_file, delimiter=",")

header_row = next(csv_file)

print(type(header_row))

for index, column_header in enumerate(header_row):
    print("Index:", index, "Column Name:", column_header)


#test_date = datetime.strptime('2018-07-01', "%Y-%m-%d")
#print(test_date)


highs = []
dates = []
lows = []

for i in csv_file:
    highs.append(int(i[5]))
    current_date = datetime.strptime(i[2], "%Y-%m-%d")
    dates.append(current_date)
    lows.append(int(i[6]))

print(highs)
print(dates)

import matplotlib.pyplot as plt

fig = plt.figure()

plt.plot(dates, highs, c="red")
plt.plot(dates, lows, c="blue")

plt.fill_between(dates, highs, lows, facecolor="blue", alpha=0.1)

plt.title("Daily high and low temperatures - 2018", fontsize=16)
plt.xlabel("Month of July 2018")
plt.ylabel("Temperatures (F)", fontsize=16)
plt.tick_params(axis="both", labelsize=16)

fig.autofmt_xdate()

#plt.show()

plt.subplot(2, 1, 1)
plt.plot(dates, highs, c="red")
plt.title("Highs")

plt.subplot(2, 1, 2)
plt.plot(dates, lows, c="blue")
plt.title("Lows")

plt.suptitle("Highs and Lows of Sitka, Alaska 2018")

plt.show()
