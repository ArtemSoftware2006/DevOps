import pandas as pd
import psycopg2

csv_source_path = '.\\data\\dump (3).csv'
csv_target_path = '.\\data\\table_ip_domain.csv'
csv_target_non_duplicate_path = '.\\data\\table_ip_domain_non_dublicate.csv'

def calk_ip_domain():
    print('Start calk ip and domain...')
    df = pd.read_csv(csv_source_path, delimiter=';', usecols=[0,1], header=None, encoding='cp1251')
    with open(csv_target_path, 'w') as target_file:
        for i, row in df.iterrows():
        
            if pd.isnull(row[0]) or pd.isna(row[0]) or pd.isnull(row[1]) or pd.isna(row[1]):
                continue
            ips = row[0].split('|')
            domains = row[1].split('|')

            for ip in ips:
                for domain in domains:
                    target_file.writelines(ip + ';' + domain + '\n')

            if i == 200000:
                break
    print('Finish calk ip and domain!')

def detele_duplicate():
    print('Start delete duplicate...')
    lines_seen = set() # создаем пустой набор для хранения уникальных строк

    with open(csv_target_path, 'r') as infile:
        with open(csv_target_non_duplicate_path, 'w') as outfile:
            for line in infile:
                if line not in lines_seen: # проверяем, есть ли текущая строка в наборе
                    lines_seen.add(line) # добавляем строку в набор
                    outfile.write(line) # записываем строку в новый файл
    print('Finish delete duplicate!')


def save_csv_to_database():
    print('Start save csv to database...')

    conn = psycopg2.connect(dbname='vk_test2', user='postgres', password='1111', host='localhost', port='5433')

    cur = conn.cursor()
    with open(csv_target_non_duplicate_path, 'r') as source_file:
        cur.copy_from(source_file, 'ip_domains', sep=";", columns=('ip', 'domain'))
        conn.commit()

    cur.close()
    print('Finish save csv to database!')

def main():
    calk_ip_domain()
    detele_duplicate()
    save_csv_to_database()

main()