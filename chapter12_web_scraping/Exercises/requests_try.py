import requests

res = requests.get('https://automatetheboringstuff.com/files/rj.txt')
try:
    res.raise_for_status()
except Exception as exc:
    print('there was a problem')