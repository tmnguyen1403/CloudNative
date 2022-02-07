import requests

HEALTH_ENDPOINT = "http://localhost:5000/health"
r = requests.get(HEALTH_ENDPOINT)

if r.status_code == 200:
    print(r.json())
