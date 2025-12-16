import requests

def test_health():
    r = requests.get("http://localhost:5002/health")  # Muuta tähän oikea portti
    assert r.status_code == 200
    assert "OK" in r.text
