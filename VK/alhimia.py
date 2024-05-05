import csv
from tqdm import tqdm
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy.dialects.postgresql import INET
import pandas as pd

Base = declarative_base()

class IPDomain(Base):
    __tablename__ = 'ip_domains'
    ip_id = Column(Integer, ForeignKey('ip_addresses.id'), primary_key=True)
    domain_id = Column(Integer, ForeignKey('domains.id'), primary_key=True)
    
class IP(Base):
    __tablename__ = 'ip_addresses'
    id = Column(Integer, primary_key=True, autoincrement=True)
    ip_address = Column(INET)
    domains = relationship('IPDomain', backref='ips')

class Domain(Base):
    __tablename__ = 'domains'
    id = Column(Integer, primary_key=True, autoincrement=True)  
    domain = Column(String)
    ips = relationship('IPDomain', backref='domains')

engine = create_engine('postgresql://postgres:1111@localhost:5433/vk_test_home')
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

print('Start import data')

csv_source_path = '.\\data\\table_ip_domain_non_dublicate.csv'
csv_target_path = '.\\data\\table_ip_domain_PKs.csv'

num_lines = sum(1 for line in open(csv_source_path))

with open(csv_source_path, 'r') as source_file:
    with open(csv_target_path, 'w') as target_file:
        reader = csv.reader(source_file, delimiter=';')
        i = 0
        for row in tqdm(reader, total=num_lines):
            ip_address, domain_name = row
            ip = session.query(IP).filter_by(ip_address=ip_address).first()
            domain = session.query(Domain).filter_by(domain = domain_name).first()

            target_file.writelines(str(ip.id) + ';' + str(domain.id) + '\n')
            if i == 60000:
                break
            i+=1
print('Finished import data')

session.commit()
session.close()
