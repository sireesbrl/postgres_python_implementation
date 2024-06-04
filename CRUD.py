#connecting to a postgresql database and performing various CRUD operations
#can be refined for further functionalities

import psycopg
from getpass import getpass

class Database:

    def __init__(self, db, user_name, passwd, host_add, port_no):
        self.db = db
        self.user_name = user_name
        self.passwd = passwd
        self.host_add = host_add
        self.port_no = port_no

        #with psycopg.connect(f"dbname={self.db} user={self.user_name} password={self.passwd} host={self.host_add} port={self.port_no}") as conn:
            #pass
            #with conn.cursor() as cur:
            #    cur.execute(
            #        """CREATE TABLE person(ID serial PRIMARY KEY, First_Name text NOT NULL, Last_Name text NOT NULL)"""
            #    )
            #    print("Table 'Person' created...")

    #def create_table(self):
        #tname = input("Table name: ").strip()
        #tfields = {"fieldname" : "constraints",}
        #while True:
        #    input fields
        #    tfields[fieldname] = constraints
        #    more? else break
        #    create table
    
    def add_info(self):
        #clear screen
        while True:
            f_name = input("Enter first name: ").strip()
            l_name = input("Enter last name: ").strip()

            with psycopg.connect(f"dbname={self.db} user={self.user_name} password={self.passwd} host={self.host_add} port={self.port_no}") as conn:
                with conn.cursor() as cur:
                    cur.execute(
                        """INSERT INTO person(First_Name, Last_Name) VALUES (%s, %s)""", (f_name, l_name)
                    )
                conn.commit()
                conn.close()

            choice = input("Add more? y/n: ").strip()
            if choice == "n":
                break
        


    def read_info(self):
        #clear screen
        with psycopg.connect(f"dbname={self.db} user={self.user_name} password={self.passwd} host={self.host_add} port={self.port_no}") as conn:
            with conn.cursor() as cur:
                record = cur.execute("""SELECT * FROM person""").fetchall()
                #add proper grid view
                print("ID      First Name      Last Name")              
                for row in record:
                    print(f"{row[0]}       {row[1]}          {row[2]}")
            conn.close()

    def update_info(self):
        self.read_info()
        
        choice = int(input("Enter ID: ").strip())
        f_name = input("First name to: ").strip()
        l_name = input("Last name to: ").strip()
        with psycopg.connect(f"dbname={self.db} user={self.user_name} password={self.passwd} host={self.host_add} port={self.port_no}") as conn:
            with conn.cursor() as cur:
                cur.execute(
                    """UPDATE person SET First_Name = %s, Last_Name = %s WHERE ID = %s""", (f_name, l_name, choice)
                )
            conn.commit()
            conn.close()            

    def delete_info(self):
        self.read_info()
        
        choice = int(input("Enter ID: ").strip())
        with psycopg.connect(f"dbname={self.db} user={self.user_name} password={self.passwd} host={self.host_add} port={self.port_no}") as conn:
            with conn.cursor() as cur:
                cur.execute(
                    """DELETE FROM person WHERE ID = %s""", (choice)
                )
            conn.commit()
            conn.close()

def operate_db(db):
    print("Options Available")
    print("1. Add Info \n2. Read Info \n3. Update Info \n4. Delete Info")
    
    choice = int(input("Select: ").strip())
    
    match choice:
        case 1:
            db.add_info()
        case 2:
            db.read_info()
        case 3:
            db.update_info()
        case 4:
            db.delete_info()
        case _:
            pass
                

def main():
    db = input("Database: ").strip()
    user_name = input("Username: ").strip()
    passwd = getpass()
    host_add = input("Host: ").strip()
    port_no = int(input("Port: ").strip())
    
    database = Database(db, user_name, passwd, host_add, port_no)
    operate_db(database)


if __name__ == "__main__":
    main()
