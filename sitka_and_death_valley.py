from datetime import datetime
import csv
import matplotlib.pyplot as plt

Death_Valley_File = open("death_valley_2018_simple.csv", "r")
Death_Valley_csv_file = csv.reader(Death_Valley_File, delimiter=",")

indices = {}

header_row = next(Death_Valley_csv_file)
for index, column_header in enumerate(header_row):
    print("Index:", index, "Column Name:", column_header)
    indices[column_header] = index

dates = []

DeathValleyLows = []
DeathValleyHighs = []

for i in Death_Valley_csv_file:
    try:
        high = int(i[indices["TMAX"]])
        low = int(i[indices["TMIN"]])
        converted_date = datetime.strptime(i[indices["DATE"]], "%Y-%m-%d")
        DeathValleyName = i[indices["NAME"]]
    except ValueError:
        print(f"Missing data for {converted_date}")
    else:
        DeathValleyHighs.append(int(i[indices["TMAX"]]))
        DeathValleyLows.append(int(i[indices["TMIN"]]))
        dates.append(converted_date)

Death_Valley_File.close()

Sitka_File = open("sitka_weather_2018_simple.csv", "r")
Sitka_csv_file = csv.reader(Sitka_File, delimiter=",")
header_row2 = next(Sitka_csv_file)

indices = {}
for index, column_header in enumerate(header_row2):
    print("Index:", index, "Column Name:", column_header)
    indices[column_header] = index

SitkaLows = []
SitkaHighs = []

for i in Sitka_csv_file:
    SitkaHighs.append(int(i[indices["TMAX"]]))
    SitkaLows.append(int(i[indices["TMIN"]]))
    SitkaName = i[indices["NAME"]]

Sitka_File.close()

fig, a = plt.subplots(2)
fig.set_size_inches(12, 6)
fig.suptitle("Temperature Comparison Between" + " " + SitkaName + " " + "and" + " " + DeathValleyName)

a[0].plot(dates, SitkaHighs, c="red")
a[0].plot(dates, SitkaLows, c="blue")
a[0].fill_between(dates, SitkaHighs, SitkaLows, facecolor="blue", alpha=0.1)
a[0].set_title(SitkaName)

a[1].plot(dates, DeathValleyHighs, c="red")
a[1].plot(dates, DeathValleyLows, c="blue")
a[1].fill_between(dates, DeathValleyHighs, DeathValleyLows, facecolor="blue", alpha=0.1)
a[1].set_title(DeathValleyName)

fig.autofmt_xdate()

plt.show()
