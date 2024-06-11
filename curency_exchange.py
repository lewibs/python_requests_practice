import requests
# https://github.com/fawazahmed0/exchange-api

eur = requests.get("https://cdn.jsdelivr.net/npm/@fawazahmed0/currency-api@latest/v1/currencies/eur.json")
eur = eur.json()
eur_usd = eur.get("eur").get("usd")
usd = requests.get("https://cdn.jsdelivr.net/npm/@fawazahmed0/currency-api@latest/v1/currencies/usd.json")
usd = usd.json()
usd_eur = usd.get("usd").get("eur")

if abs(1-eur_usd) == abs(1-usd_eur):
    print("No proffit to be made")
else: 
    print("proffit to be made")
