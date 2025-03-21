import psycopg2
from psycopg2.extras import RealDictCursor

DB_NAME="student"
DB_USER = "postgres"
DB_PASSWORD = "1234"
DB_HOST = "localhost"
DB_PORT = "5432"

def get_connection():
    return psycopg2.connect(
        dbname=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD,
        host=DB_HOST,
        port=DB_PORT
    )

def execute_query(query, params=None, fetch=False):
    conn = get_connection()
    try:
        with conn:
            with conn.cursor(cursor_factory=RealDictCursor) as cur:
                cur.execute(query, params)
                if fetch:
                    return cur.fetchall()
    finally:
        conn.close()

def create_record(table, columns, values):
    placeholders = ", ".join(["%s"] * len(values))
    col_names = ", ".join(columns)
    query = f"INSERT INTO {table} ({col_names}) VALUES ({placeholders})"
    execute_query(query, values)

def read_records(table, columns="*", where_clause=None):
    query = f"SELECT {columns} FROM {table}"
    if where_clause:
        query += " " + where_clause
    return execute_query(query, fetch=True)

def update_record(table, updates, where_clause):
    set_clause = ", ".join([f"{col}=%s" for col in updates.keys()])
    query = f"UPDATE {table} SET {set_clause} {where_clause}"
    execute_query(query, list(updates.values()))

def delete_record(table, where_clause):
    query = f"DELETE FROM {table} {where_clause}"
    execute_query(query)
    
def get_student_by_id(sno):
    return read_records("student", where_clause=f"WHERE sno='{sno}'")

def insert_new_student(sno, sname, sage, sgender, sdept):
    create_record("student", ["sno", "sname", "sage", "sgender", "sdept"], [sno, sname, sage, sgender, sdept])
    print(f"Student {sname} with student number {sno} has been successfully added.")

def print_data(record):
    if not record:
        print("No data found.")
        return
    
    for key, value in record[0].items():
        print(f"{key}: {value}", end=" | ")
    print()

def answer_a():
    print("------- Answer to question (a): -------")
    sno = input("Enter student number: ")
    result = get_student_by_id(sno)
    if result:
        print_data(result)
    else:
        print(f"No student found with student number {sno}")

def answer_b():
    print("------- Answer to question (b): -------")
    while True:
        sno = input("Enter student number: ")
        existing_student = get_student_by_id(sno)
        if existing_student:
            print(f"Student number {sno} already exists. Please re-enter.")
            continue
        sname = input("Enter student name: ")
        sage = int(input("Enter student age: "))
        sgender = input("Enter student gender: ")
        sdept = input("Enter student department name: ")
        insert_new_student(sno, sname, sage, sgender, sdept)
        print("The following information has been successfully added.")
        print_data([{"sno": sno, "sname": sname, "sage": sage, "sgender": sgender, "sdept": sdept}])
        break

def answer_c():
    print("------- Answer to question (c): -------")
    sno = input("Enter student number: ")
    student = get_student_by_id(sno)
    if not student:
        print(f"No student found with student number {sno}")
        return

    print("\nCurrent student information:")
    print_data(student)
    
    print("\nPlease enter the new student information:")
    sname = input("Enter new student name: ")
    sage = int(input("Enter new student age: "))
    sgender = input("Enter new student gender: ")
    sdept = input("Enter new student department name: ")

    updates = {
        "sname": sname,
        "sage": sage,
        "sgender": sgender,
        "sdept": sdept
    }
    update_record("student", updates, where_clause=f"WHERE sno='{sno}'")

    updated_student = get_student_by_id(sno)
    print("\nUpdated student information:")
    print_data(updated_student)
    
def answer_d():
    print("------- Answer to question (d): -------")
    sno = input("Enter student number: ")
    student = get_student_by_id(sno)
    if not student:
        print(f"No student found with student number {sno}")
        return
    enrolled_courses = read_records("sc", where_clause=f"WHERE sno='{sno}'")
    if enrolled_courses:
        delete_record("sc", where_clause=f"WHERE sno='{sno}'")
        print(f"Deleted enrollment records for student number {sno} from 'sc' table.")
    
    delete_record("student", where_clause=f"WHERE sno='{sno}'")
    print(f"Deleted student information for student number {sno} from 'student' table.")

if __name__ == "__main__":
    answer_a()
    answer_b()
    answer_c()
    answer_d()