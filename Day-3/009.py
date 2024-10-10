print("Thank you for choosing Python Pizza Deliveries!")
size = input()
add_pepperoni = input()
extra_cheese = input()

bill = 0

if size == "s":
    bill += 15
elif size == "m":
    bill += 20
else:
    bill += 25

if add_pepperoni == "y":
    if size == "s":
        bill += 2
    else:
        bill += 3

if extra_cheese == "y":
    bill += 1
    print(f"Your final bill is ${bill}")
else:
    print(f"Your final bill is ${bill}")