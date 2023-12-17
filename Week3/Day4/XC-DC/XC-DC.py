import requests
import json
import sqlite3
import random
import psycopg2

def get_country():    
    url = 'https://restcountries.com/v3.1/all'
    data = requests.get(url)
    data = data.json()
    x = random.randint(0,len(data)-1)
    s = list()
        # print(data[x]['name']['common'])
        # print(data[x]['capital'][0])
        # print(data[x]['flags']['png'])
        # print(data[x]['subregion'])
        # print(data[x]['population'])

    s.append(data[x]['name']['common'])
    s.append(data[x]['capital'][0])
    s.append(data[x]['flags']['png'])
    s.append(data[x]['subregion'])
    q = data[x]['population']
    s.append(q)
    return s


conn = psycopg2.connect(
    dbname = 'public',
    user = 'postgres',
    password = '1234',
    host = 'localhost',
    port = '5432' 
)

for i in range(10):
    w = get_country()
    # for t in w:
    #     print(t)    
    cur = conn.cursor()
    insert_query = 'INSERT INTO countries (name, capital, url, subregion, popul) VALUES (%s,%s,%s,%s,%s)'
    data_to_insert = (w[0],w[1],w[2],w[3],w[4])
    cur.execute(insert_query, data_to_insert)
    conn.commit()


cur.execute('SELECT * FROM countries')
rows = cur.fetchall()
for row in rows:
    print(row)

cur.close
conn.close


