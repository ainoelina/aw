import requests
import json

def json_data():
    r = requests.get('https://api.github.com/search/repositories?q=language:python')
    data = r.json()
    str = ""
    dict = {}
    add = ""
    for i in data['items']:
        str = ""
        str = f"{i['forks']}.{i['name']}: {i['description']}"
        print(str)

def main():
    json_data()

main()