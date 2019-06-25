def calculate_balance(balance):
    monthlyPaymentRate = 0.02
    annualInterestRate = 0.18
    for i in range(0,12):
        remainingBalance = balance - (balance * monthlyPaymentRate)
        remainingBalance = remainingBalance + (annualInterestRate / 12) * remainingBalance
        balance = remainingBalance
    return balance

print("""
***********************************************

balance - the outstanding balance on the credit card
annualInterestRate - annual interest rate as a decimal
monthlyPaymentRate - minimum monthly payment rate as a decimal

For each month, calculate statements on the monthly payment and remaining balance. At the end of 12 months, 
print out the remaining balance. Be sure to print out no more than two decimal digits of accuracy - so print

***********************************************
""")


while True:
    try:
        print("Press 'q' for exit\n")
        balance = input("Give me your balance : \n")
        if (balance == "q"):
            break
        else:
            balance = float(balance)
            if(balance < 0):
                print("Balance cannot be a negative value ! please try again\n")
            else:
                print("\nYour remaining balance is %.2f\n" % calculate_balance(balance))
    except ValueError:
        print("\nInvalid Operation ! please try again \n")



