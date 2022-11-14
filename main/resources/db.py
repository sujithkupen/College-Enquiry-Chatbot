import sqlite3
from sqlite3 import Error

def create_conn(db_file):
     try:
         conn = sqlite3.connect(db_file)
     except Error as e:
         print(e)
     finally:
         conn.close()

conn = sqlite3.connect('main\\resources\\db\\studentinfo.db')

c = conn.cursor()
c.execute("PRAGMA foreign_keys = ON")


def create_tables(c):
    try:

        c.execute('CREATE TABLE IF NOT EXISTS LOGIN'
                  '(id integer PRIMARY KEY NOT NULL, '
                  'email text, '
                  'pswd text)')

        c.execute('CREATE TABLE IF NOT EXISTS STUD_INFO'
                  '(id integer PRIMARY KEY NOT NULL, '
                  'fname text, '
                  'lname text, '
                  'sem_id integer, '
                  'FOREIGN KEY(id) REFERENCES LOGIN(id) ON DELETE CASCADE)')

        c.execute('CREATE TABLE IF NOT EXISTS GPA_DETAILS'
                  '(id integer, '
                  'sem1 real, '
                  'sem2 real, '
                  'sem3 real, '
                  'sem4 real, '
                  'sem5 real, '
                  'sem6 real, '
                  'sem7 real, '
                  'sem8 real, '
                  'FOREIGN KEY(id) REFERENCES STUD_INFO(id) ON DELETE CASCADE)')

    except Error as e:
        print(e)


create_tables(c)
conn.commit()


def populate(c):
    try:
        # id, email, pswd


        LOGIN_INFO = [(1, 'jyothi38@jntuhucej.edu', '19538'),
                       (2, 'kaveri03@jntuhucej.edu', '20503'),
                       (3, 'sujith41@jntuhucej.edu', '19541'),
                       (4, 'anusha30@jntuhucej.edu', '19530')]

        c.executemany('INSERT INTO LOGIN VALUES (?,?,?)', LOGIN_INFO)

        # id, fname, lname, sem_id


        STUD_DETAILS = [(1, 'Jyothi', 'N', 7),
                         (2, 'Kaveri', 'E', 7),
                         (3, 'Sujith Kumar', 'P', 7),
                         (4, 'Anusha', 'K', 7)]

        c.executemany('INSERT INTO STUD_INFO VALUES (?,?,?,?)', STUD_DETAILS)

        # id, sem(1 to 8)


        GPA_DETAILS = [(1, 8.4 , 7.2 , 7.4 , 7.4 , 7.9 , 7.5 , 7.0 , 0.0),
                       (2, 8.2 , 7.9 , 7.1 , 7.9 , 7.4 , 6.9 , 7.2 , 0.0),
                       (3, 8.2 , 7.5 , 7.2 , 7.9 , 7.4 , 7.3 , 6.9 , 0.0),
                       (4, 8.5, 7.6, 7.3, 7.5, 7.4, 7.2, 7.1, 0.0)]

        c.executemany('INSERT INTO GPA_DETAILS VALUES (?,?,?,?,?,?,?,?,?)', GPA_DETAILS)

    except Error as e:
        print(e)


populate(c)
conn.commit()


def bulkDataIns():
     for num in range(5, 201):
         if (num % 2) == 0:
    
              c.execute("INSERT INTO LOGIN VALUES(?,?,?)", (num, 'abc' + str(num) + '@jntuhucej.edu', 'abc' + str(num)))
              c.execute( "INSERT INTO STUD_INFO VALUES(?,?,?,?)", (num, 'ABC' , 'DEF' , 8) )
              c.execute("INSERT INTO GPA_DETAILS VALUES(?,?,?,?,?,?,?,?,?)", (num, 8.4, 8.3, 9.4, 8.9, 8.8, 9.5, 9.2, 0.0))
         else:
              c.execute("INSERT INTO LOGIN VALUES(?,?,?)", (num, 'xyz' + str(num) + '@jntuhucej.edu', 'xyz' + str(num)))
              c.execute("INSERT INTO STUD_INFO VALUES(?,?,?,?)", (num, 'PQR', 'XYZ', 7))
    
              c.execute("INSERT INTO GPA_DETAILS VALUES(?,?,?,?,?,?,?,?,?)", (num, 8.6, 8.3, 9.0, 8.5, 8.4, 8.9, 0.0, 0.0))


bulkDataIns()
conn.commit()

print("Write Successful")