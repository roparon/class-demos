import psycopg2

#establish_connection
conn = psycopg2.connect("dbname=my_pgdb")
cur = conn.cursor()

#create_table
cur.execute("""
CREATE TABLE table1(
            id INTEGER PRIMARY KEY,
            completed BOOLEAN NOT NULL DEFAULT false
            );

""")
#insert record
cur.execute("""INSERT INTO table1 (id, completed) VALUES (1, true);
            
            """)
#commit the transaction
conn.commit()
#close the cursor and the connection
cur.close()
conn.close()