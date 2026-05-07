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

print(header)

dates = []
percentages = []
for row in reader:
    date = datetime.strptime(row [0], '%Y-%m-%d')
    percentage = float(row[1])
    dates.append(date)
    percentages.append(percentage)

print(dates[0], percentages[0])