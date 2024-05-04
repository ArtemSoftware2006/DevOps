import pandas
import psycopg2
import csv 
from threading import Thread


csv_source_path = 'C:\\Users\\Artem\\Downloads\\dump (3).csv' 
csv.field_size_limit(int(1e6))

def count_urls_more_two_in_row():
    df = pandas.read_csv(csv_source_path, 
                        delimiter=';', 
                        usecols=[2], 
                        header=None, 
                        encoding='cp1251'
                        )
    count_urls_more_two_in_row = 0

    for index, row in df.iterrows():
        if pandas.isnull(row[2]) or pandas.isna(row[2]):
            continue
        urls = row[2].split('|')
        if len(urls) > 1:
            count_urls_more_two_in_row += 1

    print(count_urls_more_two_in_row)

def count_domains():
    df = pandas.read_csv(csv_source_path, 
                        delimiter=';', 
                        usecols=[2], 
                        header=None, 
                        encoding='cp1251'
                        )
    
    count_urls_more_two_in_row = 0

    for index, row in df.iterrows():
        if pandas.isnull(row[2]) or pandas.isna(row[2]):
            continue
        count_urls_more_two_in_row += 1

    print(count_urls_more_two_in_row)

def main():

    conn = psycopg2.connect(
        dbname="ip_tables",
        user='postgres',
        password='1111',
        host='localhost',
        port='5433'
    )
    
    th1 = Thread(target=count_domains,args=())
    th1.start()

    th2 = Thread(target=count_urls_more_two_in_row,args=())
    th2.start()

    print('Rows with column \"description\"')
    with open(csv_source_path, 'r') as csv_file:
        reader = csv.reader(csv_file, delimiter=';',)
        for i, row in enumerate(reader):
            if len(row) > 3:
                print(i, row[3])

    th2.join()
    th1.join()

main()