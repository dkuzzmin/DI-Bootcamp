
import psycopg2

conn = psycopg2.connect(
    dbname = 'qmcjdcgq',
    user = 'qmcjdcgq',
    password = '4nY4MXBPAtEpeLb7qo78BZno7hfF74kG',
    host = 'flora.db.elephantsql.com',
    port = '5432' 
)

# cur = conn.cursor()

def view_all(conn):
    cur = conn.cursor()
    cur.execute("SELECT * FROM posts_db")
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()


view_all(conn)


def input_db():
#input new posts (in future - parsing)
    

    pass

def update_patterns():
# adding new pro and anri words/phrase
# deleting new pro and anri words/phrase
    
    pass
 
def analyser(post):
    pass

# def visual_result()


# SQL table


# pattern word 

# class patternword (word, anitisem)
#     word = ''
#     antisem = True
#     posts_base


# def  analyse text




# sql online database

# set databases:
# - antisem sequnces
# - pro sequunses
# - main input base of publications (posts)
# - univers in watch list
# ?table of json’s files

# !find main metodology (finding hate speech)

# py-file:
# - connection to db
# - db link one-one
# - functions(features) in exter file (internal modul)
# - sql extract
# - using some external api
# - stat modul python
# - word analisys modul
# - visual module
# - ? class ??? how to use?
# - ? user manager??


# output:
# - dashboard (imafe file?)
# - html file on some server online
# - like telegram channel everyday stats






