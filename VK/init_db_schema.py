from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import INET

Base = declarative_base()

class IPDomain(Base):
    __tablename__ = 'ip_domains'

    id = Column(Integer, primary_key=True, autoincrement=True)
    ip = Column(INET)
    domain = Column(String)
    
class IP(Base):
    __tablename__ = 'ip_addresses'
    id = Column(Integer, primary_key=True, autoincrement=True)
    ip = Column(INET)

class Domain(Base):
    __tablename__ = 'domains'
    id = Column(Integer, primary_key=True, autoincrement=True)  
    domain = Column(String)

engine = create_engine('postgresql://postgres:1111@localhost:5433/vk_test2')
Base.metadata.create_all(engine)
