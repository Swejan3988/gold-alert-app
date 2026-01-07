import os
import requests

def get_gold_price():
    api_key = os.getenv("GOLD_API_KEY")

    if not api_key:
        raise Exception("GOLD_API_KEY not found in environment variables")

    url = "https://www.goldapi.io/api/XAU/INR"
    headers = {
        "x-access-token": api_key,
        "Content-Type": "application/json"
    }

    response = requests.get(url, headers=headers, timeout=10)
    response.raise_for_status()

    data = response.json()

    # GoldAPI returns price per troy ounce
    price_per_gram = data["price"] / 31.1035
    return round(price_per_gram, 2)
