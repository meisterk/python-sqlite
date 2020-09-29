import sqlite3
from sqlite3 import Error


def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)

    return conn


def create_klasse(conn, klasse):
    """
    Create a new klasse into the klasse table
    :param conn:
    :param klasse:
    :return: klasse id
    """
    sql = ''' INSERT INTO klasse(name)
              VALUES(?) '''
    cur = conn.cursor()
    cur.execute(sql, klasse)
    conn.commit()
    return cur.lastrowid


def create_schueler(conn, schueler):
    """
    Create a new schueler into the schueler table
    :param conn:
    :param schueler:
    :return: schueler id
    """
    sql = ''' INSERT INTO schueler(vorname, nachname, klasse_id)
              VALUES(?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, schueler)
    conn.commit()
    return cur.lastrowid


def main():
    database = r"database.db"

    # create a database connection
    conn = create_connection(database)

    with conn:
        # create a new klasse
        klasse = (('I3A'),)
        klasse_id = create_klasse(conn, klasse)

        # schueler
        schueler_1 = ('Anna', 'Arm', klasse_id)
        schueler_2 = ('Berta', 'Bein', klasse_id)

        # create schueler
        create_schueler(conn, schueler_1)
        create_schueler(conn, schueler_2)


if __name__ == '__main__':
    main()
