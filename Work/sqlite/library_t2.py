import sqlite3

def create_film_db(db_file_name):
    my_db = sqlite3.connect(db_file_name)
    my_db.close
def main():
    db_file_name = 'film.db'
    create_film_db(db_file_name)
    print("Created Database File:", db_file_name)
    
#This runs if the program is run from a console
if __name__ == '__main__':
    main()

#procedure to create film and user tables
def create_film_tables(db_file_name):
    my_db = sqlite3.connect(db_file_name)
    my_db.execute('PRAGMA foreign_keys = ON')

    sql_code = \
    " CREATE TABLE film(film_id INTEGER, title TEXT, studio TEXT, "\
    "year INTEGER, prod_cost REAL, box_office REAL, seen TEXT, " \
    "classification TEXT, PRIMARY KEY(film_id))"

    my_db.execute(sql_code)

    sql_code = \
    "CREATE TABLE user(first_name TEXT, last_name TEXT, email TEXT, password TEXT, PRIMARY KEY(email))"

    my_db.execute(sql_code)

db_file_name = 'film.db'
create_film_tables(db_file_name)
#database size = 16KB
