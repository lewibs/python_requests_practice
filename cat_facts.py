# https://cat-fact.herokuapp.com
# https://alexwohlbruck.github.io/cat-facts/docs/

import requests

res = requests.get("https://cat-fact.herokuapp.com/facts")

for fact in res.json():
    print(fact["text"])