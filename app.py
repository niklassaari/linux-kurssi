from flask import Flask, render_template, jsonify
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
    cursor.execute("SELECT 'Hello from MySQL!'")  # Or SELECT NOW() for current time
    result = cursor.fetchone()
    cursor.close()
    conn.close()

    # Render HTML template or return as a simple message
    return f"<h1>{result[0]}</h1>"

# Yksi terveystarkistusfunktio / endpoint
@app.route('/health', endpoint='health_page')
def health_page():
    return "OK", 200

@app.route('/api/health', endpoint='health_api')
def health_api():
    return jsonify({"status": "ok"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002)  # Muutettu portti 5002
