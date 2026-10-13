# Database Connection Logic
import mysql.connector


def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="chatbot_db"
    )

# the pydantics is not appropriate for chatbot for we remove the