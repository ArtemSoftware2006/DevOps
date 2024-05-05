import VK.final_script.init_db_schema as init_db_schema
import VK.final_script.domain_parse as domain_parse
import VK.final_script.ip_parse as ip_parse
import VK.final_script.ips_doamins_parse as ips_doamins_parse
import psycopg2

conn = psycopg2.connect(dbname='vk_test2', user='postgres', password='1111', host='localhost', port='5433')

cur = conn.cursor()

query = ''' ALTER TABLE ip_domains
            ADD COLUMN ip_id BIGINT,
            ADD COLUMN domain_id BIGINT;
        '''

cur.execute(query)
conn.commit()

query = ''' CREATE INDEX domain_index ON domains (domain);
            CREATE INDEX ip_index ON ip_addresses (ip);
        '''

cur.execute(query)

query = ''' UPDATE ip_domains 
            SET ip_id = (SELECT ip_addresses.id FROM ip_addresses WHERE ip_addresses.ip = ip_domains.ip) ;
        '''

cur.execute(query)
conn.commit()

query = ''' UPDATE public.ip_domains tip
            SET domain_id = (SELECT ia.id FROM public.domains ia WHERE tip.domain = ia.domain )  ;
        '''

cur.execute(query)
conn.commit()

query = ''' ALTER TABLE ip_domains
            DROP COlUMN ip,
            DROP COlUMN domain;
        '''
cur.execute(query)
conn.commit()

query = ''' ALTER TABLE ip_domains
            ADD CONSTRAINT fk_domain_id
            FOREIGN KEY (domain_id)
            REFERENCES domains(id);

            ALTER TABLE ip_domains
            ADD CONSTRAINT fk_ip_id
            FOREIGN KEY (ip_id)
            REFERENCES ip_addresses(id);
        '''

cur.execute(query)
conn.commit()

cur.close()
conn.close()
