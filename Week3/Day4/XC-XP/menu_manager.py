import psycopg2

from menu_item import MenuItem



class MenuManager:
    @classmethod
    def get_by_name(cls, name):
        conn = psycopg2.connect(
            dbname = 'qmcjdcgq',
            user = 'qmcjdcgq',
            password = '4nY4MXBPAtEpeLb7qo78BZno7hfF74kG',
            host = 'flora.db.elephantsql.com',
            port = '5432' 
        )
        
        cur = conn.cursor()
        cur.execute("SELECT item_name, item_price FROM Menu_Items WHERE item_name = %s", (name,))
        result = cur.fetchone()
        
        # print(result)
        cur.close()
        conn.close()
        if result:
            return MenuItem(*result)
        return None

    @classmethod
    def all_items(cls):
        conn = psycopg2.connect(
            dbname = 'qmcjdcgq',
            user = 'qmcjdcgq',
            password = '4nY4MXBPAtEpeLb7qo78BZno7hfF74kG',
            host = 'flora.db.elephantsql.com',
            port = '5432' 
        )


        cur = conn.cursor()
        cur.execute("SELECT item_name, item_price FROM Menu_Items")
        
        current_s = cur.fetchall()
        items = [MenuItem(*x) for x in current_s]


        cur.close()
        conn.close()
        return items
    


# item = MenuItem('Burger', 35)
# item.save()
# item.delete()
# item.update('Veggie Burger', 37)

# item3 = MenuItem('Beef Stew', 40)
# item3.save()

item2 = MenuManager.get_by_name('Beef Stew')


items = MenuManager.all_items()
for x in items:
    print(f"{x.name},{x.price}")

