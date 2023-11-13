import sqlite3
import hashlib
import os


def hash_password(password):
    """Hash a password with a unique salt."""
    salt = os.urandom(16)  # 16 bytes salt
    return hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100000)


def create_users_table():
    """Create the users table in the database."""
    conn = sqlite3.connect('your_database.db')
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            userid INTEGER PRIMARY KEY,
            username TEXT UNIQUE NOT NULL,
            password_hash BLOB NOT NULL
        )
    ''')
    conn.commit()
    conn.close()


def add_user(username, password):
    """Add a new user to the database."""
    conn = sqlite3.connect('your_database.db')
    cursor = conn.cursor()

    password_hash = hash_password(password)

    cursor.execute('''
        INSERT INTO users (username, password_hash) VALUES (?, ?)
    ''', (username, password_hash))

    conn.commit()
    conn.close()


def main():
    """Main function to set up the database."""
    create_users_table()

    # Add some users
    add_user('cs162_user', 'longpasswordsaresecure')
    add_user('admin', '123456')
    add_user('prof_smith', 'password123')
    # Add more users as needed


if __name__ == '__main__':
    main()
