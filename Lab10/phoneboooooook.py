import psycopg2
import csv
from config import load_config

def create_table():
    command = """
    CREATE TABLE phonebook (
        id SERIAL PRIMARY KEY,
        name VARCHAR(255) NOT NULL,
        phone VARCHAR(20) NOT NULL UNIQUE
    );
    """
    config = load_config()
    with psycopg2.connect(**config) as conn:
        with conn.cursor() as cur:
            cur.execute(command)
        conn.commit()

def insert_from_console():
    name = input("Name: ")
    phone = input("Phone: ")
    sql = "INSERT INTO phonebook (name, phone) VALUES (%s, %s)"
    config = load_config()
    with psycopg2.connect(**config) as conn:
        with conn.cursor() as cur:
            cur.execute(sql, (name, phone))
        conn.commit()

def insert_from_csv(csv_file):
    sql = "INSERT INTO phonebook (name, phone) VALUES (%s, %s)"
    config = load_config()
    with psycopg2.connect(**config) as conn:
        with conn.cursor() as cur:
            with open(csv_file, 'r') as f:
                reader = csv.reader(f)
                next(reader)  # Пропускаем заголовок
                for row in reader:
                    cur.execute(sql, (row[0], row[1]))
        conn.commit()

def update_user(user_id, new_name=None, new_phone=None):
    config = load_config()
    with psycopg2.connect(**config) as conn:
        with conn.cursor() as cur:
            if new_name:
                cur.execute("UPDATE phonebook SET name = %s WHERE id = %s", (new_name, user_id))
            if new_phone:
                cur.execute("UPDATE phonebook SET phone = %s WHERE id = %s", (new_phone, user_id))
        conn.commit()

def query_users(filter_value=None):
    config = load_config()
    with psycopg2.connect(**config) as conn:
        with conn.cursor() as cur:
            if filter_value:
                sql = "SELECT * FROM phonebook WHERE name ILIKE %s OR phone ILIKE %s"
                cur.execute(sql, (f'%{filter_value}%', f'%{filter_value}%'))
            else:
                sql = "SELECT * FROM phonebook"
                cur.execute(sql)
            rows = cur.fetchall()
            for row in rows:
                print(row)

def delete_user(name_or_phone):
    config = load_config()
    with psycopg2.connect(**config) as conn:
        with conn.cursor() as cur:
            sql = "DELETE FROM phonebook WHERE name = %s OR phone = %s"
            cur.execute(sql, (name_or_phone, name_or_phone))
        conn.commit()

if __name__ == '__main__':
    create_table()
    
    while True:
        print("\n1. User input via the consol")
        print("2. Uploading users from CSV")
        print("3. Update the use")
        print("4. User Search")
        print("5. Delete the use")
        print("0. Exit")

        choice = input("Select an action: ")

        if choice == '1':
            insert_from_console()
        elif choice == '2':
            csv_file = input("Enter the path to the CSV file: ")
            insert_from_csv(csv_file)
        elif choice == '3':
            user_id = int(input("Enter the user's ID: "))
            new_name = input("Enter a new name (or skip it):")
            new_phone = input("Enter a new phone number (or skip it): ")
            update_user(user_id, new_name if new_name else None, new_phone if new_phone else None)
        elif choice == '4':
            filter_value = input("Enter the filter (or leave it empty to output all of them): ")
            query_users(filter_value if filter_value else None)
        elif choice == '5':
            name_or_phone = input("Enter a name or phone number to delete:")
            delete_user(name_or_phone)
        elif choice == '0':
            break
        else:
            print("Wrong choice.")
