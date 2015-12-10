#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      pietrr
#
# Created:     05/11/2015
# Copyright:   (c) pietrr 2015
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import sqlite3

def main():
    conn = sqlite3.connect('C:\\Users\\pietrr\\Documents\\TwitterGame\\xxxx.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS Log
        (ID INTEGER PRIMARY KEY, text TEXT, output TEXT, user TEXT)''')

    try:
        newlog = (123, "inp1", "out1", "BOB")
        cursor.execute('INSERT INTO Log VALUES (?,?,?,?)', newlog)
        newlog = (124, "inp2", "out2", "BOB")
        cursor.execute('INSERT INTO Log VALUES (?,?,?,?)', newlog)
        newlog = (125, "inp3", "out3", "BOB")
        cursor.execute('INSERT INTO Log VALUES (?,?,?,?)', newlog)
    except Exception as e:
        print "sql stuff failed!"

    messagelist = []
    try:
        for row in cursor.execute('SELECT * FROM Log WHERE user=(?) ORDER BY ID ASC', ("BOB",)):
            messagelist.append(">" + str(row[1]))
            messagelist.append(row[2])
    except Exception as e:
        print "sql stuff failed! oh no!"
    messagelist = messagelist[-1 * 3:]

    print messagelist





if __name__ == '__main__':
    main()
