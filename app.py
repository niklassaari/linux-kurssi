<<<<<<< HEAD
from flask import Flask, render_template
=======
from flask import Flask, jsonify
>>>>>>> 43d2b63 (v1)
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
<<<<<<< HEAD
    cursor.execute("SELECT NOW()")  # Get SQL server time
    result = cursor.fetchone()
    cursor.close()
    conn.close()

    # Render HTML template and pass SQL time
    return render_template('test_nginx.html', sql_time=result[0])

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
=======
    cursor.execute("SELECT 'Hello from MySQL!'")
    result = cursor.fetchone()
    # Clean up
    cursor.close()
    conn.close()
    return f"<h1>{result[0]}</h1>"

# Yksi terveystarkistusfunktio / endpoint
@app.route('/health', endpoint='health_page')
def health_page():
    return "OK", 200

@app.route('/api/health', endpoint='health_api')
def health_api():
    return jsonify({"status": "ok"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
>>>>>>> 43d2b63 (v1)
