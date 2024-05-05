import pandas as pd
import psycopg2

csv_source_path = '.\\data\\dump (3).csv'
csv_target_path = '.\\data\\table_ip.csv'
csv_target_non_duplicate_path = '.\\data\\non_duplecate_table_ip.csv'

def calk_ips():
    df = pd.read_csv(csv_source_path, delimiter=';', usecols=[0], header=None, encoding='cp1251')
    print('Start calk ips...')

    with open(csv_target_path, 'w') as ips_file:
        for index, row in df.iterrows():
            if pd.isnull(row[0]) or pd.isna(row[0]):
                continue
            ips = row[0].split('|')
            for ip in ips:
                ips_file.writelines(ip + '\n')
            if index == 200000:
                break

    print('Finish calk ips!')
def save_csv_to_database():
    print("Загрузка данных в базу данных...")
    conn = psycopg2.connect(dbname='vk_test2', user='postgres', password='1111', host='localhost', port='5433')
    cur = conn.cursor()

    with open(csv_target_non_duplicate_path, "r") as f:
        cur.copy_from(f, 'ip_addresses', sep=";", columns=('ip',))
        conn.commit()

    print("Данные успешно загружены в базу данных.")

    cur.close()

def detele_duplicate():
    print('Start delete duplicate...')
    lines_seen = set() # создаем пустой набор для хранения уникальных строк

    with open(csv_target_path, 'r') as infile:
        with open(csv_target_non_duplicate_path, 'w') as outfile:
            for line in infile:
                if line not in lines_seen: # проверяем, есть ли текущая строка в наборе
                    lines_seen.add(line) # добавляем строку в набор
                    outfile.write(line) # записываем строку в новый файл

    print("Дубликаты удалены успешно.")

def main():
    calk_ips()
    detele_duplicate()
    save_csv_to_database()

main()