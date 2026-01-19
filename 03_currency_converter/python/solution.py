RATES = {
    "USD": 1.0,
    "EUR": 0.92,
    "INR": 83.0,
    "GBP": 0.79,
    "JPY": 144.0
}

def convert(amount, from_currency, to_currency):
    return (amount / RATES[from_currency]) * RATES[to_currency]

def main():
    print("Available currencies:", ", ".join(RATES.keys()))

    try:
        amount = float(input("Enter amount: "))
        from_currency = input("From currency: ").upper()
        to_currency = input("To currency: ").upper()

        if from_currency not in RATES or to_currency not in RATES:
            print("Unsupported currency.")
            return

        result = convert(amount, from_currency, to_currency)
        print(f"{amount:.2f} {from_currency} = {result:.2f} {to_currency}")

    except ValueError:
        print("Invalid amount entered.")

if __name__ == "__main__":
    main()
