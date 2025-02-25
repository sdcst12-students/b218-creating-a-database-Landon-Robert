import sqlite3

file = 'dbase.db'
connection = sqlite3.connect(file)
print(connection)

cursor = connection.cursor()
query = ("""
create table if not exists customers (
    id integer primary key autoincrement,
    fname tinytext,
    lname tinytext,
    phone bigint,
    email tinytext,
    address tinytext,
    city tinytext, 
    postalcode tinytext);
""")
cursor.execute(query)
query = """
create table if not exists pets (
    id integer primary key autoincrement,
    name tinytext,
    type tinytext,
    breed tinytext,
    birthdate tinytext,
    ownerID int);
"""
cursor.execute(query)
query = """
create table if not exists visits (
    id integer primary key autoincrement,
    ownerid int,
    petid int,
    details text,
    cost float(16,2),
    paid float(16,2));
);
"""
cursor.execute(query)

"""
end = False
print(cursor.fetchall())
while end == False:
    option = input("What would you like to do?\nExit: 0\nAdd new customer: 1\nSearch for a customer: 2")
    if option == 0:
        end = True
    elif option == 1:
        print("Please enter relevant customer information:")
        for i in cursor.fetchall():

    elif option == 2:
        print()
    else:
        print("That is not a valid input.")
"""