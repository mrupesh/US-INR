print("Currency Converter(Only Dollars And Indian Rupees)")
while True:
    currency = input("($)Dollars or (R)Rupees:")
    if currency == "$":
        amount = int(input('Enter the amount:'))
        Rupees = amount * 76.50
        print(f"${amount} is equal to: ₹{Rupees}")
    elif currency.upper() == "R":
        amount = int(input('Enter the amount:'))
        Dollars = amount / 76.50
        print(f"₹{amount} is equal to: ${Dollars}")
    else:
        print("Sorry! I don't understand that...")
        break