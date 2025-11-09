from flask import Flask, render_template
import mysql.connector

app = Flask(__name__)

@app.route('/')
def home():
    # Connect to MySQL/MariaDB
    conn = mysql.connector.connect(
        host="localhost",
        user="exampleuser",
        password="linuxkurssi",
        database="exampledb"
    )
    cursor = conn.cursor()
    cursor.execute("SELECT NOW()")  # Get SQL server time
    result = cursor.fetchone()
    cursor.close()
    conn.close()

    # Render HTML template and pass SQL time
    return render_template('test_nginx.html', sql_time=result[0])

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
