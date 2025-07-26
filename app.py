from flask import Flask, jsonify
import mysql.connector
import os

app = Flask(__name__)

def get_db_connection():
    connection = mysql.connector.connect(
        host=os.environ.get('DATABASE_HOST', 'localhost'),
        user='root',
        password='rootpassword',
        database='app_db'
    )
    return connection

@app.route('/api/message')
def get_message():
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT content FROM messages LIMIT 1")  # Fetch the content from the messages table
        row = cursor.fetchone()
        cursor.close()
        conn.close()
        message = row[0] if row else "No message"
    except Exception as e:
        message = f"Error: {str(e)}"
    return jsonify({'message': message})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
