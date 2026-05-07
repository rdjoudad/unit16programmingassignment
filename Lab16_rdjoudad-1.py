"""
Ohio Unemployment Data Mapping
Ryma Djoudad
Create a graph that visualizes data read from a file
CSV file used to create line plot
05/06/2026
"""

from pathlib import Path
import csv
import matplotlib.pyplot as plt
from datetime import datetime

path = Path('OHUR.csv')
lines = path.read_text(encoding='utf-8').splitlines()

reader = csv.reader(lines)
header = next(reader)

dates = []
percentages = []

for index, row in enumerate(reader):
    try:
        date = datetime.strptime(row [0], '%Y-%m-%d')
        percentage = float(row[1])
        dates.append(date)
        percentages.append(percentage)
    except ValueError:
        print(f"Row {row}: Missing data")

plt.style.use('seaborn-v0_8-whitegrid')
my_fig, my_ax = plt.subplots()
graph_title = "Ohio Unemployment (by Month): 1976-2022"
my_ax.set_title(graph_title, fontsize=20)
my_ax.set_xlabel('Date', fontsize=17)
my_ax.set_ylabel('Unemp Rate', fontsize=17)
my_ax.plot(dates, percentages)

plt.savefig('ohio_unemployment.png')


