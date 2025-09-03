from dotenv import load_dotenv
import os
import mysql.connector
from pathlib import Path

env_path = Path(__file__).resolve().parent.parent / 'myproject' / '.env'
load_dotenv()  # Load environment variables from .env file

def get_db_connection():
    try:
        connection = mysql.connector.connect(
            host=os.getenv('DB_HOST', 'localhost'),
            user=os.getenv('DB_USER', 'yourusername'),
            password=os.getenv('DB_PASSWORD', 'yourpassword'),
            database=os.getenv('DB_NAME', 'yourdatabase')
        )
        if connection.is_connected():
            print("Connection to the database was successful.")
            return connection
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None
    except Exception as e:
        print(f"Unexpected error: {e}")
        return None