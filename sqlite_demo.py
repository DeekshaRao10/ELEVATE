

import sqlite3
def connect_db():
    """Create and return a database connection."""
    return sqlite3.connect("students.db")


def create_table(conn):
    """Create students table programmatically."""
    query = """
    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        age INTEGER,
        marks REAL
    )
    """
    conn.execute(query)
    conn.commit()


def insert_student(conn, name, age, marks):
    """Insert a new student record safely (parameterized query)."""
    query = "INSERT INTO students (name, age, marks) VALUES (?, ?, ?)"
    conn.execute(query, (name, age, marks))
    conn.commit()



def fetch_students(conn):
    """Fetch all student records."""
    cursor = conn.execute("SELECT * FROM students")
    return cursor.fetchall()


def update_marks(conn, student_id, new_marks):
    """Update marks for a specific student."""
    query = "UPDATE students SET marks = ? WHERE id = ?"
    conn.execute(query, (new_marks, student_id))
    conn.commit()


def delete_student(conn, student_id):
    """Delete a student by ID."""
    query = "DELETE FROM students WHERE id = ?"
    conn.execute(query, (student_id,))
    conn.commit()



def display_students(records):
    """Print student records in table format."""
    print("\n{:<5} {:<15} {:<5} {:<6}".format("ID", "Name", "Age", "Marks"))
    print("-" * 35)
    for row in records:
        print("{:<5} {:<15} {:<5} {:<6}".format(row[0], row[1], row[2], row[3]))



def main():
    conn = connect_db()

    try:
        create_table(conn)

     
        name = input("Enter name: ")
        age = int(input("Enter age: "))
        marks = float(input("Enter marks: "))

        insert_student(conn, name, age, marks)

        print("\nAll Students:")
        records = fetch_students(conn)
        display_students(records)

        
        student_id = int(input("\nEnter student ID to update marks: "))
        new_marks = float(input("Enter new marks: "))
        update_marks(conn, student_id, new_marks)

   
        student_id = int(input("\nEnter student ID to delete: "))
        delete_student(conn, student_id)

        print("\nUpdated Student List:")
        records = fetch_students(conn)
        display_students(records)

    except Exception as e:
        print("Database error:", e)

    finally:
        conn.close()  
        print("\nDatabase connection closed.")


if __name__ == "__main__":
    main()
