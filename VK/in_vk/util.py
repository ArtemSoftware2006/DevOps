# This is my VK lab
# I developed util for analize ips and domains 

import psycopg2
# import pprint
from pprint import pprint
# подключение к базе данных PostgreSQL
conn = psycopg2.connect("dbname=ip_tables user=postgres password=1111 host=localhost port=5433")
cur = conn.cursor()

# обработка ввода
while True:
    print('1. - Get IP from domain\n2. - Get domain from IP\n3. - Top 10 blocked ip \n4. - Count blocked ip\n5. - Count blocked domain\n6. - Exit')

    try:
        choice = int(input('Enter your choice: '))
        cur = conn.cursor()
        if choice == 1:
            ip_var = input("Enter IP: ")
            cur.execute("SELECT domain FROM public.ip_address WHERE ip = %s", (ip_var,))
        elif choice == 2:
            doamin_var = input("Enter domain: ")
            cur.execute("SELECT ip FROM public.ip_address WHERE domain = %s", (doamin_var,))
        elif choice == 3:
            cur.execute("SELECT ip, count(ip) FROM public.ip_address GROUP BY ip ORDER BY count(ip) DESC LIMIT 10;")
        elif choice == 4:
            cur.execute("select count(ip) from public.ip_address")
        elif choice == 5:
            cur.execute("select count(domain) from public.ip_address")
        else: 
            cur.close()
            break
        pprint(cur.fetchall())
        print()
        cur.close()
    except ValueError:
        # How create text red in print
        print("Oops!  That was no valid number.  Try again...")
        continue
cur.close()