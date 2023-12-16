# Managing a Simple User Database

# Scenario:
# You're building a basic user management system that interacts with a PostgreSQL database. 
# Users should be able to:

# View all existing users.
# Add a new user.
# Update a user's information.
# Delete a user.

# Tasks:
# Database Setup:

# Create a PostgreSQL database named user_management.
# Inside the database, create a table named users with columns: 
# id (integer, primary key), username (varchar), email (varchar), and age (integer).

# Python Script:

# Write a Python script that connects to the user_management database.
# Implement functions to perform the following operations:
# View all users from the users table.
# Add a new user to the users table.
# Update a user's information based on their id.
# Delete a user from the users table based on their id.

import psycopg2

conn = psycopg2.connect(
    dbname = 'user_management',
    user = 'postgres',
    password = '1234',
    host = 'localhost',
    port = '5432' 
)

cur = conn.cursor()

s_in = 0

while s_in != 5:
    print('''User Managenment
    1. View all users
    2. Add a user
    3. Update a user       
    4. Delete a user
    5. Exit''')
    s_in = int(input('Enter you choice: '))

    if s_in == 1:
        cur.execute('SELECT * FROM users')
        rows = cur.fetchall()
        for row in rows:
            print(row)
        print()
    elif s_in == 2:
        print("Add a User:")
        name_in = input("Enter username: ")
        email_in = input("Enter e-mail: ")
        age_in = input("Enter your age: ")
        
        cur.execute('SELECT COUNT(*) FROM users')
        index_in = cur.fetchall()
        index_in = index_in[0][0]+1
        print(index_in)
        cur.execute('INSERT INTO users VALUES (%s, %s)', ('iKey', 750))





print("bye")


# cur.execute('SELECT * FROM users')
# rows = cur.fetchall()
# for row in rows:
#     print(row)

cur.close()
conn.close()

# User Interaction:

# Create a simple command-line interface (CLI) to interact with your Python functions.
# The CLI should provide options to view, add, update, or delete users, 
# and take appropriate inputs from the user to perform these actions.

# Testing:

# Test your Python script by adding users, viewing all users, 
# updating user information, and deleting users.





# Create a cursur object to execute SQL queries
# cur = conn.cursor()

# CRUD  - Create (insert) Read (select) Update (update) Delete (delete)

# Insert query
# insert_query = 'INSERT INTO products (name, price) VALUES (%s, %s)'
# data_to_insert = ('iKey', 750)
# # cur.execute(insert_query, data_to_insert)
# cur.execute('INSERT INTO products (name, price) VALUES (%s, %s)', ('iKey', 750))



# Update query
# update_query = 'UPDATE products SET name=%s, price=%s WHERE id= %s'
# new_value = ('iCar2024', 9999, 8)
# cur.execute(update_query, new_value)

# Delete query
# cur.execute('DELETE FROM products WHERE id=%s', ('5'))


# Commit the transaction
# conn.rollback()



# Execute a SELECT query
# cur.execute('SELECT * FROM products')
# rows = cur.fetchall()

# for row in rows:
#     print(row)


# Close the cursur and the connection
