
import requests

url = "https://cdn.jsdelivr.net/gh/akabab/superhero-api@0.3.0/api/all.json"

resp = requests.get(url)
heroes_dict = {}
max = 0

def search(heroes):
    for hero in resp.json():
        if hero['name'] in heroes:
            powerstats = hero['powerstats']
            intell = powerstats['intelligence']
            heroes_dict[heroes] = int(intell)


search('Hulk')
search('Captain America')
search('Thanos')
print(heroes_dict)

for key, value in heroes_dict.items():
    if value > max:
        max = value
    if value == max:
        more_intel = key

print(more_intel)
