import psycopg


def add_info():
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

with psycopg.connect("dbname=postgres user=sirees password=sirees host=localhost") as conn:
    with conn.cursor() as cur:
        #try:
        cur.execute(
            """CREATE TABLE person(ID serial PRIMARY KEY, First_Name text NOT NULL, Last_Name text NOT NULL)"""
        )
        #except psycopg.errors.DuplicateTable:
            #print("Table 'Person' already exists!")
        #else:
            #print("Creating 'Person' table...")

        add_info()
        conn.commit()
        conn.close()
