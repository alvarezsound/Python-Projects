import sqlite3

# opens the connection to sqlite3
conn = sqlite3.connect('Database_Assignment.db')

# creates table called "tbl_files" with ID column and filename column
with conn:
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_files( \
        ID INTEGER PRIMARY KEY AUTOINCREMENT, col_filename STRING)")
    conn.commit()

# fileList tuple
fileList = ('information.docx', 'Hello.txt', 'myImage.png', \
            'myMovie.mpg', 'World.txt', 'data.pdf', 'myPhoto.jpg')

# loop through tuple to find and add filenames that end with .txt to the
# database and print  them to the console
for x in fileList:
    if x.endswith('.txt'):
        with conn:
            cur = conn.cursor()
            cur.execute("INSERT INTO tbl_files (col_filename) VALUES (?)", (x,))
            print(x)

# closes the connection to sqlite3
conn.close()
