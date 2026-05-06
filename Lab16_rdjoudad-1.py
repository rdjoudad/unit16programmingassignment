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
import datetime

path = Path('OHUR.csv')
lines = path.read_text(encoding='utf-8').splitlines()

reader = csv.reader(lines)
header = next(reader)

print(header)

dates = []
percentages = []

