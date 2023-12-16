import psycopg2



class MenuItem:
    def __init__(self, name, price):
        self.name = name
        self.price = price
        conn = psycopg2.connect(
         dbname = 'qmcjdcgq',
         user = 'qmcjdcgq',
         password = '4nY4MXBPAtEpeLb7qo78BZno7hfF74kG',
         host = 'flora.db.elephantsql.com',
         port = '5432' 
        )

    def save(self):
        conn = psycopg2.connect(
         dbname = 'qmcjdcgq',
         user = 'qmcjdcgq',
         password = '4nY4MXBPAtEpeLb7qo78BZno7hfF74kG',
         host = 'flora.db.elephantsql.com',
         port = '5432' 
        )
        cur = conn.cursor()
        cur.execute("INSERT INTO Menu_Items (item_name, item_price) VALUES (%s, %s)", (self.name, self.price))
        conn.commit()
        cur.close()
        conn.close()

    def delete(self):
        conn = psycopg2.connect(
         dbname = 'qmcjdcgq',
         user = 'qmcjdcgq',
         password = '4nY4MXBPAtEpeLb7qo78BZno7hfF74kG',
         host = 'flora.db.elephantsql.com',
         port = '5432' 
        )
        cur = conn.cursor()
        cur.execute("DELETE FROM Menu_Items WHERE item_name = %s", (self.name,))
        conn.commit()
        cur.close()
        conn.close()

    def update(self, new_name, new_price):
        conn = psycopg2.connect(
         dbname = 'qmcjdcgq',
         user = 'qmcjdcgq',
         password = '4nY4MXBPAtEpeLb7qo78BZno7hfF74kG',
         host = 'flora.db.elephantsql.com',
         port = '5432' 
        )
        cur = conn.cursor()
        if new_name:
            cur.execute("UPDATE Menu_Items SET item_name = %s WHERE item_name = %s", (new_name, self.name))
            self.name = new_name
        if new_price is not None:
            cur.execute("UPDATE Menu_Items SET item_price = %s WHERE item_name = %s", (new_price, self.name))
            self.price = new_price
        conn.commit()
        cur.close()
        conn.close()







# cur = conn.cursor()