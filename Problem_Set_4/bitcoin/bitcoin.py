import sys
import requests


def main():
    # Step 1: Read and validate the command-line argument
    if len(sys.argv) != 2:
        sys.exit("Missing command-line argument")

    try:
        num_bitcoins = float(sys.argv[1])
    except ValueError:
        sys.exit("Command-line argument is not a number")

    # Step 2: Fetch Bitcoin price data from the API
    try:
        response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
        response.raise_for_status()  # Check for HTTP request errors
    except requests.RequestException:
        sys.exit("Error fetching Bitcoin price data")

    # Step 3: Extract Bitcoin price from the JSON response
    try:
        data = response.json()
        bitcoin_price_usd = data['bpi']['USD']['rate_float']
    except (KeyError, TypeError, ValueError):
        sys.exit("Error parsing JSON data")

    # Step 4: Calculate the total cost in USD
    total_cost = num_bitcoins * bitcoin_price_usd

    # Step 5: Format and print the result
    print(f"${total_cost:,.4f}")


if __name__ == "__main__":
    main()
