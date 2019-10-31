from flask import Flask
import psycopg2
# from config import config
import json

#-----------------GET-----------------
def get_creatures():
    conn = None
    try:
        conn = psycopg2.connect("dbname=mythical_creatures")
        cur = conn.cursor()
        cur.execute("SELECT * FROM creatures;") 
        rows = cur.fetchall() #.fetchmany() or .fetchone()
        return(rows)
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

app = Flask (__name__)

@app.route("/", methods=['GET', 'POST'])
def creatures():
    creatures = json.dumps(get_creatures())
    return(creatures)


#-----------------POST-----------------


def insert_creature(name, origin):
    """ insert a new creature into the creatures table """
    sql = """INSERT INTO creatures  (name, origin) VALUES (%s, %s);"""
    conn = None
    vendor_id = None
    try:
        # connect to the PostgreSQL database
        conn = psycopg2.connect("dbname=mythical_creatures")
        # create a new cursor
        cur = conn.cursor()
        # execute the INSERT statement
        cur.execute(sql, (name, origin))
        # commit the changes to the database
        conn.commit()
        # close communication with the database
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

# print('name:')
# name = input()
# print('origin:')
# origin = input()

# insert_creature(name, origin)


#-----------------UPDATE-----------------

def update_creature(id, name):
    """ update creature name based on the creature id """
    sql = """ UPDATE creatures
                SET origin = %s
                WHERE id = %s"""
    conn = None
    updated_rows = 0
    try:
        # connect to the PostgreSQL database
        conn = psycopg2.connect("dbname=mythical_creatures")
        # create a new cursor
        cur = conn.cursor()
        # execute the UPDATE  statement
        cur.execute(sql, (name, id))
        # Commit the changes to the database
        conn.commit()
        # Close communication with the PostgreSQL database
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

# print('update origin:')
# name = input()
# print('id:')
# id = input()

# update_creature(id, name)



#-----------------UPDATE-----------------


def delete_creature(id):
    """ delete creature by part id """
    conn = None
    try:
        # connect to the PostgreSQL database
        conn = psycopg2.connect("dbname=mythical_creatures")
        # create a new cursor
        cur = conn.cursor()
        # execute the UPDATE  statement
        cur.execute("DELETE FROM creatures WHERE part_id = %s", (id))
        # Commit the changes to the database
        conn.commit()
        # Close communication with the PostgreSQL database
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
 


delete_creature(14)