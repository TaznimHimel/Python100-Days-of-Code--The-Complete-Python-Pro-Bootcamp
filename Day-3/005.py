print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0
if height >= 120:
    print("You can ride in the rollercoaster!")
    age = int(input("What is your age? "))
    if age < 12:
        bill = 5
        print("Childs ticket is $5.")
    elif age <= 18:
        bill = 7
        print("Youths ticket is  $7.")
    else:
        bill = 12
        print("Adults ticket is $12.")
        
    want_photos = input("Do you want a photo taken? Type Y or N? ")
    
    if want_photos == "y":
        bill+=3
        print(f"Your bill is ${bill} ")
    else:
        print(f"Your bill is ${bill}. ")
else:
    print("Sorry! you have to grow taller before you can ride.")