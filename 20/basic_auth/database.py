import sqlite3
import hashlib
import os


def hash_password(password):
    """Hash a password with a unique salt."""
    salt = os.urandom(16)  # 16 bytes salt
    return hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100000)


def ok_user_and_password(username, password):
    """Test whether the supplied username and password match."""
    conn = sqlite3.connect('your_database.db')
    cursor = conn.cursor()

    cursor.execute(
        "SELECT password_hash FROM users WHERE username = ?", (username,))
    stored_password_hash = cursor.fetchone()

    if stored_password_hash:
        return hash_password(password) == stored_password_hash[0]
    return False
