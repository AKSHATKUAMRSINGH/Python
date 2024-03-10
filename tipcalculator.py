print("Welcome to tip calculator!")
Bill=float(input("What was the total Bill? $"))
Tip=int(input("How much tip would you like to give? 10, 12 or 15?"))
people=int(input("How many people to split the bill?"))
Final_Bill=Tip/100*Bill+Bill
print(Final_Bill)