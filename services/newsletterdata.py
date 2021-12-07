import requests


def generateNewsData():
    url = ('https://newsapi.org/v2/everything?'
           'q=Steel&'
           'from=2021-11-27&'
           'sortBy=popularity&'
           'apiKey=b69886d32bdd4beab5b74b3385ac7dbc')
    response = requests.get(url)
    return response.json()



