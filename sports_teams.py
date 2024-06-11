# https://docs.sportmonks.com/football/endpoints-and-entities/endpoints/teams/get-all-teams

import dotenv
import requests
import os

dotenv.load_dotenv()

key = os.environ.get("SPORTS")
print(key)

res = requests.get("https://api.sportmonks.com/v3/football/teams", headers={"Authorization":key})

if res.headers.get("Content-Type") != "application/json":
    raise Exception(res.headers.get("Content-Type"))

body = res.json()

teams = [team["name"] for team in body["data"]]