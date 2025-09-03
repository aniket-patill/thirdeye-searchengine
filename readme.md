# ThirdEyeData-Project

A Django-based user registration and login API using MySQL, JWT authentication, and secure password hashing.

---

## 📦 Project Structure

```
myproject/
├── manage.py
├── myproject/
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── .env
└── searchengine/
    ├── register.py
    ├── login.py
    ├── database/
    │   └── create_connection.py
    ├── urls.py
    └── ...
```

---

## 🛠️ Prerequisites

- Python 3.8+
- MySQL Server
- pip (Python package manager)
- [Postman](https://www.postman.com/) (for API testing)

---

## 1️⃣ MySQL Database Setup

1. **Start MySQL Server** and log in:
    ```
    mysql -u root -p
    ```

2. **Create the database:**
    ```sql
    CREATE DATABASE thirdeyedb;
    USE thirdeyedb;
    ```

3. **Create the users table:**
    ```sql
    CREATE TABLE users (
        id INT AUTO_INCREMENT PRIMARY KEY,
        username VARCHAR(150) NOT NULL UNIQUE,
        password VARCHAR(255) NOT NULL,
        email VARCHAR(255) NOT NULL UNIQUE,
        Token TEXT,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
    ```

---

## 2️⃣ Clone the Repository

```
git clone <your-repo-url>
cd ThirdEyeData-Project/myproject
```

---

## 3️⃣ Python Environment Setup

1. **Create a virtual environment (recommended):**
    ```
    python -m venv venv
    venv\Scripts\activate   # On Windows
    ```

2. **Install dependencies:**
    ```
    pip install django mysql-connector-python python-dotenv pyjwt bcrypt
    ```

---

## 4️⃣ Configure Environment Variables

1. **Edit the `.env` file** at `myproject/myproject/.env`:

    ```
    DB_HOST=localhost
    DB_USER=root
    DB_PASSWORD=root@123
    DB_NAME=thirdeyedb

    SECRET_KEY=your-very-secret-key
    ```

    - Replace values as needed for your MySQL setup.
    - Use a strong random string for `SECRET_KEY`.

---

## 5️⃣ Django Settings

- The project is already configured to use MySQL and environment variables in `settings.py`.
- No changes needed unless your setup differs.

---

## 6️⃣ Run Migrations (Optional)

If you use Django models, run:
```
python manage.py makemigrations
python manage.py migrate
```
> For this project, user registration uses direct SQL, so this step is optional.

---

## 7️⃣ Start the Django Server

```
python manage.py runserver
```
- The server will run at [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

---

## 8️⃣ Test the APIs in Postman

### Register User

- **Method:** POST  
- **URL:** `http://127.0.0.1:8000/register/`
- **Body:** `x-www-form-urlencoded`
    - `username`: your_username
    - `password`: your_password
    - `email`: your_email@example.com

**Success Response:**
```json
{
  "message": "User registered successfully",
  "token": "<JWT token>"
}
```

---

### Login User

- **Method:** POST  
- **URL:** `http://127.0.0.1:8000/login/`
- **Body:** `x-www-form-urlencoded`
    - `username`: your_username
    - `password`: your_password

**Success Response:**
```json
{
  "message": "Login successful",
  "token": "<JWT token>"
}
```

---

## 9️⃣ Troubleshooting

- **Database connection errors:** Check your `.env` values and MySQL server status.
- **Module not found:** Ensure all dependencies are installed in your virtual environment.
- **JWT/SECRET_KEY errors:** Make sure `SECRET_KEY` is set in `.env` and loaded correctly.

---

## 🔒 Security Notes

- Passwords are securely hashed with bcrypt before storage.
- JWT tokens are generated for authentication.
- Never commit your `.env` file or real secret keys to public repositories.

---

## 📧 Questions?

Open an issue or contact