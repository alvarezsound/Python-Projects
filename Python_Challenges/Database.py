import sqlite3
from sqlite3 import Error


def create_connection():
    conn = None;
    try:
        conn = sqlite3.connect(':memory:')
        print(sqlite3.version)
    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()


def create_table():
    conn = None;
    try:
        conn = sqlite3.connect(':memory:')
        cur = conn.cursor()
        table = """ CREATE TABLE IF NOT EXISTS tbl_roster( \
                ID INTEGER PRIMARY KEY AUTOINCREMENT, \
                col_name TEXT, \
                col_species TEXT, \
                col_iq INT) """
        cur.execute(table)
        print("Table created successfully!")
        conn.commit()
        cur.execute("INSERT INTO tbl_roster(col_name, col_species, col_iq) VALUES (?,?,?)", \
                        ('Jean-Baptiste Zorg','Human', 122))
        cur.execute("INSERT INTO tbl_roster(col_name, col_species, col_iq) VALUES (?,?,?)", \
                        ('Korben Dallas','Meat Popsicle', 100))
        cur.execute("INSERT INTO tbl_roster(col_name, col_species, col_iq) VALUES (?,?,?)", \
                        ('Ak\'not','Mangalore', -5))
        print("Table data inserted successfully!")
        conn.commit()
        sql_update_query = """Update tbl_roster SET col_species = 'Human' WHERE col_species = 'Meat Popsicle'"""
        cur.execute(sql_update_query)
        conn.commit()
        print("Record Updated successfully")
        cur.execute ("SELECT col_name,col_iq FROM tbl_roster WHERE col_species = 'Human'")
        varPerson = cur.fetchall()
        for item in varPerson:
            msg = "Name: {}\nIQ: {}".format(item[0],item[1])
            print (msg)
    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()

if __name__ == '__main__':
    create_table()

