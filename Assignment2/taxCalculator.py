income_ = 85528
income = float(input("Enter income: "))
tax1 = ((18*income) / 100) - 556.2
tax2 = 14839.2 + ((income - income_)*32) / 100
if income < income_:
    print("Tax: ",round(tax1))
elif income > income_:
    print("Tax: ",round(tax2))
else:
    print("No tax")