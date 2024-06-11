# https://theaxolotlapi.netlify.app/

import requests

res = requests.get("https://theaxolotlapi.netlify.app/")
print(res.headers.get("Content-Type"))
print(res.text)