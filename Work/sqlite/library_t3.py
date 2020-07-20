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
    
    #SQLite3 does not have a boolean/yes/no or date/time datatype
    
    sql_code = \
    "CREATE TABLE studio(studio_id TEXT, Description TEXT, HQ_address TEXT, HQ_city TEXT,"\
    "PRIMARY KEY(studio_id))"
    my_db.execute(sql_code)
    
    sql_code = \
    "CREATE TABLE film(film_id INTEGER, title TEXT, studio TEXT, "\
    "year INTEGER, prod_cost REAL, box_office REAL, seen TEXT, " \
    "classification TEXT, studio_id TEXT NOT NULL, CONSTRAINT fk_studio PRIMARY KEY(film_id), FOREIGN KEY(studio_id) REFERENCES studio(studio_id))"    

    my_db.execute(sql_code)

    sql_code = \
    "CREATE TABLE user(first_name TEXT, last_name TEXT, email TEXT, password TEXT, PRIMARY KEY(email))"

    my_db.execute(sql_code)
    
def insert_AVATAR(db_file_name):
    my_db = sqlite3.connect(db_file_name)
    my_db.execute('PRAGMA foreign_keys = ON')
    sql_code = \
    "INSERT INTO film VALUES(1,'Avatar', 'Fox', 2009, 254.00, 2787.97,'Y','12')"
    my_db.execute(sql_code)



db_file_name = 'film.db'
create_film_tables(db_file_name)
insert_AVATAR(db_file_name)
#db file size = 24KB
