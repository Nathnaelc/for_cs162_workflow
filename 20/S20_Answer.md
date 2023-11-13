### SQL Injection Attacks

#### Database Structure

```sql
CREATE TABLE users (
    userid INT PRIMARY KEY,
    username TEXT,
    email TEXT,
    password TEXT
);

INSERT INTO users VALUES (1, "cs162_user", "cs162@minerva.kgi.edu", "longpasswordsaresecure");
INSERT INTO users VALUES (2, "admin", "admin@minerva.kgi.edu", "123456");
INSERT INTO users VALUES (3, "prof_smith", "smith@minerva.kgi.edu", "password123");
```

#### Vulnerable SQL Query

```sql
"SELECT userid, username FROM users WHERE username='" + username + "' AND password='" + password + "';"
```

#### 1. Attack to Identify a Known User Without Knowing Their Password

- **Objective**: Log in as a known user (e.g., `admin`) without knowing their password.
- **Injection**: For the username, use `admin' --`. This will comment out the password check.
- **Resulting SQL Query**:
  ```sql
  SELECT userid, username FROM users WHERE username='admin' --' AND password='...';
  ```
- **Explanation**: The `--` is a SQL comment. Everything after `--` will be ignored, effectively bypassing the password check.

#### 2. Attack to Identify an Unknown User

- **Objective**: Log in as any user without knowing the username or password.
- **Injection**: Use `' OR '1'='1` for both username and password fields.
- **Resulting SQL Query**:
  ```sql
  SELECT userid, username FROM users WHERE username='' OR '1'='1' AND password='' OR '1'='1';
  ```
- **Explanation**: The condition `'1'='1'` is always true, so this query will return all users in the database, effectively bypassing both username and password checks.

These attacks highlight the importance of sanitizing and validating user inputs in applications to prevent SQL injection vulnerabilities. In practice, using parameterized queries or ORM frameworks like SQLAlchemy can help mitigate these risks. For instance, I use parameterized queries in my Express apps.

```bash
const grabUserInfo = async (userId) => {
  try {
    const query = `
      SELECT * FROM users
      WHERE user_id = $1;
    `;
    const res = await pool.query(query, [userId]);
    return res.rows[0];
  } catch (err) {
    console.error(err);
    throw new Error("Error fetching user information");
  }
};
```

In this code:
The userId is passed as a parameter to the query, not concatenated directly into the query string.
This method ensures that userId is always treated as a value, not as executable code, thus preventing SQL injection.
