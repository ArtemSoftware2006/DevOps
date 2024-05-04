import pandas as pd
import psycopg2

# Подключение к базе данных PostgreSQL
conn = psycopg2.connect(
    dbname="ip_tables",
    user="postgres",
    password="1111",
    host="localhost",
    port="5433"
)
cur = conn.cursor()

# Чтение CSV файла
df = pd.read_csv('.\\data\\dump (3).csv',delimiter=';', usecols=[0,1,2], header=None, encoding='cp1251')
print(df.head(n=15))
# Обработка каждой строки CSV файла
for index, row in df.iterrows():
    # Разделение IP адресов в строке

    ips = row[0]
    if type(ips) is float:
        continue

    ips = row[0].split('|')

    for ip in ips:
        with open('./ip_parse.csv', 'a') as domain_file:
            if pd.isnull(ip) or pd.isna(ip):
                domain_file.writelines('\n')
            elif pd.isnull(row[1]) or pd.isna(row[1]):
                domain_file.writelines(ip + ';' + ';' + '\n')
            elif pd.isnull(row[2]) or pd.isna(row[2]):
                domain_file.writelines(ip + ';' + row[1] + ';' + '\n')
            else:
                domain_file.writelines(ip + ';' + row[1] + ';' + row[2] + '\n')

    print(index)

    if index == 10000:
        break

print('You are winner!')

# Закрытие соединения с базой данных
cur.close()
conn.close()