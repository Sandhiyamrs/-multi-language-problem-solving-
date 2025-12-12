import requests

def get_rate(from_currency, to_currency):
    try:
        url = f"https://api.exchangerate.host/convert?from={from_currency}&to={to_currency}"
        response = requests.get(url).json()
        return response['info']['rate']
    except Exception as e:
        print("Error fetching rate:", e)
        return None

amount = float(input("Amount: "))
from_curr = input("From (USD/EUR/INR/...): ").upper()
to_curr = input("To (USD/EUR/INR/...): ").upper()

rate = get_rate(from_curr, to_curr)
if rate:
    print(f"{amount} {from_curr} = {amount*rate:.2f} {to_curr}")
else:
    print("Conversion failed.")

