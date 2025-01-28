
# if statement: if sale amount is more than 5000, then give 10% discount

amount = float(input("Enter purchase amount: "))

if amount > 5000:
    disc = amount * 0.10
    amount -= disc

print("Final bill: ", amount)
