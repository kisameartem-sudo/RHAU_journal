from database import get_connection


def init_database():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.executescript("""
    CREATE TABLE IF NOT EXISTS groups (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL UNIQUE
    );

    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        full_name TEXT NOT NULL,
        group_id INTEGER NOT NULL,
        FOREIGN KEY (group_id) REFERENCES groups(id)
    );

    CREATE TABLE IF NOT EXISTS disciplines (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL UNIQUE
    );

    CREATE TABLE IF NOT EXISTS lessons (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        discipline_id INTEGER NOT NULL,
        group_id INTEGER NOT NULL,
        lesson_date DATE NOT NULL,
        lesson_type TEXT,
        topic TEXT,
        FOREIGN KEY (discipline_id) REFERENCES disciplines(id),
        FOREIGN KEY (group_id) REFERENCES groups(id)
    );

    CREATE TABLE IF NOT EXISTS attendance (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        lesson_id INTEGER NOT NULL,
        student_id INTEGER NOT NULL,
        status TEXT NOT NULL,
        FOREIGN KEY (lesson_id) REFERENCES lessons(id),
        FOREIGN KEY (student_id) REFERENCES students(id),
        UNIQUE (lesson_id, student_id)
    );

    CREATE TABLE IF NOT EXISTS practical_works (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        discipline_id INTEGER NOT NULL,
        title TEXT NOT NULL,
        max_score INTEGER DEFAULT 5,
        FOREIGN KEY (discipline_id) REFERENCES disciplines(id)
    );

    CREATE TABLE IF NOT EXISTS practical_results (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        practical_id INTEGER NOT NULL,
        student_id INTEGER NOT NULL,
        submission_date DATE,
        status TEXT NOT NULL,
        score REAL,
        FOREIGN KEY (practical_id) REFERENCES practical_works(id),
        FOREIGN KEY (student_id) REFERENCES students(id),
        UNIQUE (practical_id, student_id)
    );
    """)

    conn.commit()
    conn.close()


if __name__ == "__main__":
    init_database()