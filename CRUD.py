import psycopg
from getpass import getpass

def add_info():
    #clear screen
    while True:
        f_name = input("Enter first name: ").strip()
        l_name = input("Enter last name: ").strip()

        cur.execute(
            """INSERT INTO person(First_Name, Last_Name) VALUES (%s, %s)""", (f_name, l_name)
        )

        choice = input("Add more? y/n: ").strip()
        if choice == "n":
            break


def read_info():
    #clear screen
    record = cur.execute("""SELECT * FROM person""").fetchall()
    
    print("ID    First Name     Last Name")
    for row in record:
        print(f"{row[0]}    {row[1]}    {row[2]}")

def update_info():
    read_info()
    
    choice = int(input("Enter ID: ").strip())
    f_name = input("First name to: ").strip()
    l_name = input("Last name to: ").strip()
    
    cur.execute(
        """UPDATE person SET First_Name = %s, Last_Name = %s WHERE ID = %d""", (f_name, l_name, choice)
    )

def delete_info():
    read_info()
    
    choice = int(input("Enter ID: ").strip())
    
    cur.execute(
        """DELETE FROM person WHERE ID = %d""", (choice)
    )

def connect_db(db, user_name, passwd, host_add, port_no):
    with psycopg.connect(f"dbname={db} user={user_name} password={passwd} host={host_add} port={port_no}") as conn:
        with conn.cursor() as cur:
            cur.execute(
                """CREATE TABLE person(ID serial PRIMARY KEY, First_Name text NOT NULL, Last_Name text NOT NULL)"""
            )

        print("Table 'Person' created...")
        print("Options Available")
        print("1. Add Info \n2. Read Info \n3. Update Info \n4. Delete Info")
        
        choice = int(input("Select: ").strip())
        
        match choice:
            case 1:
                add_info()
            case 2:
                read_info()
            case 3:
                update_info()
            case 4:
                delete_info()
            case _:
                pass
                
        conn.commit()
        conn.close()

def main():
    db = input("Database: ").strip()
    user_name = input("Username: ").strip()
    passwd = getpass()
    host_add = input("Host: ").strip()
    port_no = int(input("Port: ").strip())
    
    connect_db(db, user_name, passwd, host_add, port_no)

if __name__ == "__main__":
    main()
