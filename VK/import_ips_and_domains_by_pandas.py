from pandas import pd
from sqlalchemy import create_engine

engine = create_engine('postgresql://postgres:1111@localhost:5433/vk_test_home')


ips_path = '.\\data\\non_duplecate_table_ip.csv'
domains_path = '.\\data\\non_duplecate_table_domain.csv'

df = pd.read_csv(ips_path, delimiter=';', encoding='cp1251') 
df.to_sql('ip_addresses', engine, if_exists='append', index=False)  

df = pd.read_csv(domains_path, delimiter=';', encoding='cp1251') 
df.to_sql('domains', engine, if_exists='append', index=False)  