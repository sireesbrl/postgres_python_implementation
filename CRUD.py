import psycopg


def add_info():
    while True:
        f_name = input("Enter first name: ").strip()
        l_name = input("Enter last name: ").strip()

        cur.execute(
            """INSERT INTO person(f_name, l_name) VALUES (%s, %s)""", (f_name, l_name)
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
    pass

def delete_info():
    pass

with psycopg.connect("dbname=postgres user=sirees password=sirees host=localhost") as conn:
    with conn.cursor() as cur:
        #try:
        cur.execute(
            """CREATE TABLE person(id serial PRIMARY KEY, f_name text NOT NULL,l_name text NOT NULL)"""
        )
        #except psycopg.errors.DuplicateTable:
            #print("Table 'Person' already exists!")
        #else:
            #print("Creating 'Person' table...")

        add_info()
        conn.commit()
        conn.close()
