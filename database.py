import sqlite3

# Connect to SQLite and set up tables if not already existing
def init_db():
    conn = sqlite3.connect('keylogger_detection.db')
    cursor = conn.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS user_details (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        mobile TEXT NOT NULL,
        email TEXT NOT NULL,
        address TEXT NOT NULL,
        education TEXT NOT NULL
    )
    ''')
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS keylogger_status (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        status BOOLEAN NOT NULL,
        timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
    )
    ''')
    conn.commit()
    conn.close()

def save_user_details(name, mobile, email, address, education):
    conn = sqlite3.connect('keylogger_detection.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO user_details (name, mobile, email, address, education) VALUES (?, ?, ?, ?, ?)',
                   (name, mobile, email, address, education))
    conn.commit()
    conn.close()

def toggle_keylogger_status(activate):
    conn = sqlite3.connect('keylogger_detection.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO keylogger_status (status) VALUES (?)', (activate,))
    conn.commit()
    conn.close()

# Initialize database
init_db()
