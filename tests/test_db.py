import mysql.connector
import pytest

def test_mysql_connection():
    try:
        # Käytä dockerin nimen mukaista yhteyttä, esim. 'mysql' jos käytät docker-composea
        conn = mysql.connector.connect(
            host="mysql",  # Muuta 'localhost' konttien nimeksi (docker-compose) tai IP
            user="exampleuser",
            password="linuxkurssi",
            database="exampledb",
            port=3306
        )
        cursor = conn.cursor()
        cursor.execute("SELECT 'Connection successful!'")
        result = cursor.fetchone()
        cursor.close()
        conn.close()
        assert result[0] == 'Connection successful!'  # tarkista, että yhteys onnistui
    except mysql.connector.Error as err:
        pytest.fail(f"MySQL connection failed: {err}")
