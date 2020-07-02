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
