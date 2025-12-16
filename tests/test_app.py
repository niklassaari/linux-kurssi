def test_health():
    import requests
    r = requests.get("http://localhost:5001/health")
    assert r.status_code == 200
    assert "OK" in r.text
