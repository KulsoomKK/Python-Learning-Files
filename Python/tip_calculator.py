total = input("What is your total bill? ")

dollar = total.replace("$", "")
total = float(dollar)

tip = float(input("Please select your tip percentage between: 15%, 18% and 20%? "))

tip_amt = (tip/100) * total
net_total = tip_amt + total

print(f"Your tip amount is {tip_amt:.2f}")
print(f"Your total amount including tip is {net_total:.2f}")

