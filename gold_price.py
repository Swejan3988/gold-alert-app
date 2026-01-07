import requests

def get_gold_price():
    url = "https://www.goldapi.io/api/XAU/INR"
    headers = {
        "x-access-token": "YOUR_API_KEY",
        "Content-Type": "application/json"
    }

    response = requests.get(url, headers=headers)
    data = response.json()

    # price per gram (24K)
    price_per_gram = data["price"] / 31.1
    return round(price_per_gram, 2)
