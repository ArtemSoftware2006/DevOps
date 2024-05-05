import psycopg2

conn = psycopg2.connect(dbname='vk_test_home', user='postgres', password='1111', host='localhost', port='5433')

cur = conn.cursor()

source_path = '.\\data\\table_ip_domain_PKs.csv'

with open(source_path, 'r') as source_file:
    cur.copy_from(source_file, 'ip_domains', sep=";", columns=('ip_id', 'domain_id'))
    conn.commit()

cur.close()
conn.close()