import csv

file_path = 'data/ШтатИмпорт.csv'

with open(file_path, 'r') as file:
    reader = csv.reader(file, delimiter='/')
    for line in reader:
        print(line)

import pandas as pd


df = pd.read_csv(file_path, delimiter='/' ,encoding='windows-1251')
print(df.head(4))
print(df.describe())