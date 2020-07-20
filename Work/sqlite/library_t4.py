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
user_data = (
('Fred', 'Bloggs', 'fred.bloggs@gmail.com', '1234'),
('Joe', 'Bloggs','joe.bloggs@outlook.co.uk','password'),
('Bob', 'Brown', 'bob123@talktalk.com', 'bob123'),
('John', 'Fish', 'thefish@yahoo.com', 'F1$hM4n'))

def insert_user_data(db_file_name):
    my_db =sqlite3.connect(db_file_name)
    my_db.execute('PRAGMA foreign_keys = ON')
    my_db.executemany('INSERT INTO user VALUES (?,?,?,?)', user_data) #executemany replaces the ?s with the data in the 'user_data'
    my_db.commit() #required to ensure that the data is saved to the disk
    my_db.close()

studio_data = (
('Fox','20th Century Fox','Fox Studio Lot Building 88', 'Los Angeles'),
('Sony','Sony Pictures', '10202 West Washington Boulevard', 'Culver City'),
('WB','Warner Bros. Entertainment Inc.','4000 Warner Blvd', 'Burbank'),
('BV','Buena Vista Film Distribution Company','500 South Buena Vista Street', 'Burbank'),
('DW','DreamWorks Animation LLC','1000 Flower Street', 'Glendale'))
    
def insert_studio_data(db_file_name):
    my_db =sqlite3.connect(db_file_name)
    my_db.execute('PRAGMA foreign_keys = ON')
    my_db.executemany('INSERT INTO studio VALUES (?,?,?,?)', studio_data) #executemany replaces the ?s with the data in the 'user_data'
    my_db.commit() #required to ensure that the data is saved to the disk
    my_db.close()
    
film_data = (
(1,'Avatar','Fox',2009,254.00,2787.97,'Y','12'),
(2,'Spider-Man 3','Sony',2007,286.00,890.87,'N','12'),
(3,'The Dark Knight Rises','WB',2012,230.00,1084.43,'N','12'),
(4,'The Hobbit: The desolation of Smaug','WB',2013,225.00,960.37,'Y','12'),
(5,'Harry Potter and the half-blood Prince','WB',2009,268.00,934.42,'N','U'),
(6,'Pirates of the Caribbean:Dead Man''s Chest','BV',2006,256.00,1066.18,'N','U'),
(7,'Shrek 2','DW',2004,100.00,919.83,'Y','U'),
(8,'Pirates of the Caribbean: At world''s end','BV',2007,300.00,963.42,'N','12'),
(9,'Skyfall','WB',2012,205.00,1108.56,'N','12'),
(10,'Titanic','Fox',1997,260.00,2186.77,'Y','12'))

def insert_film_data(db_file_name):
    my_db =sqlite3.connect(db_file_name)
    my_db.execute('PRAGMA foreign_keys = ON')
    my_db.executemany('INSERT INTO studio VALUE (?,?,?,?,?,?,?,?)', film_data) #executemany replaces the ?s with the data in the 'user_data'
    my_db.commit() #required to ensure that the data is saved to the disk
    my_db.close()



db_file_name = 'film.db'
create_film_tables(db_file_name)
insert_user_data(db_file_name)
insert_studio_data(db_file_name)
#db file size = 24KB the size didnt change
