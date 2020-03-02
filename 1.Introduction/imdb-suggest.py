import requests
import json

def getRecommendations(query):
    # http://sg.media-imdb.com/suggests/a/ab.json
    first = query[0]
    template = 'http://sg.media-imdb.com/suggests/{first}/{query}.json'
    url = template.format(first = first, query = query)
    proxies = {
        "http": "http://proxy.ase.ro:8080",
        "https": "https://proxy.ase.ro:8080"
    }
    response = requests.get(url, proxies=proxies)
    # response = requests.get(url)
    jsonpData = response.text
    print(jsonpData)
    s = slice(6 + len(query), -1)
    jsonData = jsonpData[s]
    recommendations = json.loads(jsonData)
    for item in recommendations['d']:
        if item['s'].startswith('Act'):
            print(item['l'])

def main():
    getRecommendations('ab')


if __name__ == "__main__":
    main()