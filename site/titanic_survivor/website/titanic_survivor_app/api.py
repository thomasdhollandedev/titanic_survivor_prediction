import requests


def getPercentageSurvived(body):
    response = requests.post('http://127.0.0.1:8001/predict', json=body)
    print(response.json())
    return response.json()
