import pandas as pd
import psycopg2

csv_source_path = '.\\data\\dump (3).csv'
csv_target_path = '.\\data\\table_domain.csv'
csv_target_non_duplicate_path = '.\\data\\non_duplecate_table_domain.csv'

def calk_domains():
    print('Start calk domains...')
    df = pd.read_csv(csv_source_path,delimiter=';', usecols=[1], header=None, encoding='cp1251')
    # Обработка каждой строки CSV файла
    with open(csv_target_path, 'w') as domain_file:
        for index, row in df.iterrows():
            if pd.isnull(row[1]) or pd.isna(row[1]):
                continue
            else:
                domains = row[1].split('|')
                for domain in domains:
                    domain_file.writelines(domain + '\n')

            if index == 200000:
                break

    print('You are winner!')

def delete_duplecate_domains():
    print('Start delete duplicate...')
    domains_set = set()

    with open(csv_target_path, 'r') as source_file:
        with open(csv_target_non_duplicate_path, 'w') as target_file:
            for line in source_file:
                if line not in domains_set:
                    domains_set.add(line)
                    target_file.write(line)
    print('Finish delete duplicate!')


def save_domain_to_db():
    print('Start save domain to db...')
    conn = psycopg2.connect(dbname='vk_test2', user='postgres', password='1111', host='localhost', port='5433')
    cur = conn.cursor()
    with open(csv_target_non_duplicate_path, 'r') as source_file:
        cur.copy_from(source_file, 'domains', sep=";", columns=('domain',))
        conn.commit()
    cur.close()
    print('Finish save domain to db!')

def main():
    calk_domains()
    delete_duplecate_domains()
    save_domain_to_db()
    
main()
