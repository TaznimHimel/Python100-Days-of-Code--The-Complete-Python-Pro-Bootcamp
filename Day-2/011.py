print("Welcome to tip the calculator!");

Bill = float(input("What was the total bill? $"));

Tip = int(input("What parcentage tip would you like to give? 10, 12 or 15?"));

TotalBill = (Bill + ((Bill*Tip)/100));

Split = int(input("How many people to split the bill?"));

Pay = float(TotalBill/Split);

final_amount = round (Pay,2);

final_amount = "{:.2f}".format(Pay);

print(f"Each person should pay: ${final_amount}");
