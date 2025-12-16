import mysql.connector

def test_mysql_connection():
    conn = mysql.connector.connect(
        host="localhost",
        user="exampleuser",
        password="linuxkurssi",
        database="exampledb"
    )
    cursor = conn.cursor()
    cursor.execute("SELECT 1")
    result = cursor.fetchone()
    cursor.close()
    conn.close()
    assert result[0] == 1
