import csv
import psycopg2
import os
def main():
    conn = psycopg2.connect(dbname='vk_test_home', user='postgres', password='1111', host='localhost', port='5433')

    # how get path to dir without file\
    current_dir = os.path.dirname(os.path.abspath(__file__))
    current_dir = current_dir + '\\data\\ips.csv'

    # how change permissions for file    
    query = 'SELECT * FROM ip_address;'

    cur = conn.cursor()

    cur.execute(query)
    results = cur.fetchall()

    with open(current_dir, 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile, delimiter=';')
        for row in results:
            csvwriter.writerow(row)

    cur.close()
    conn.close()

main()
    