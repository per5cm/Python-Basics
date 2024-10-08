import sys
import requests

if len(sys.argv) == 2:
    try: 
        value = float(sys.argv[1])
    except ValueError:
        print("Command-line argument is not a number")
        sys.exit(1)
else:
    print("Missing command-line argument")
    sys.exit(1)

try:
    request = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    request.raise_for_status()
    response = request.json()
    bitcoin = response["bpi"]["USD"]["rate_float"]
    total_amount = bitcoin * value
    print(f"${total_amount:,.4f}")

except requests.RequestException:
    print("Request exception")