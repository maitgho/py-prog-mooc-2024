# Write your solution here

gift_value = int(input("Value of gift: "))

if gift_value < 5000:
    amount = 0
elif gift_value < 25000:
    tax = 100
    tax_rate = 0.08
    amount = (tax + (gift_value - 5000) * tax_rate)
elif gift_value < 55000:
    tax = 1700
    tax_rate = 0.10
    amount = (tax + (gift_value - 25000) * tax_rate)
elif gift_value < 200000:
    tax = 4700
    tax_rate = 0.12
    amount = (tax + (gift_value - 55000) * tax_rate)
elif gift_value < 1000000:
    tax = 22100
    tax_rate = 0.15
    amount = (tax + (gift_value - 200000) * tax_rate)
else:
    tax = 142100
    tax_rate = 0.17
    amount = (tax + (gift_value - 1000000) * tax_rate)

if amount > 0:
    print(f"Amount of tax: {amount} euros")
else:
    print("No tax!")
