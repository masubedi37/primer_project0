
while True:
  name = input("Enter your name: ")
  try:
    if  name.isalnum() == False:
     print(name)
     break
    
  except:
    print("Invalid Input. Please Try Again")

while True:
    try:
     age = int(input("Enter your age(age should be between 21 to 65): "))
     if (age > 20) and (age <= 65):
      print(age)
      break
      
    except ValueError:
      print("Invalid Input. Please Try Again.")

while True:
    try:
        bank_st = int(input("Enter your current bank statement: "))
        print(bank_st)
        break
    except ValueError:
        print('Invalid Input. Please Try Again')

while True:
    try:
        credit_score = int(input("Enter your Credit Score: "))
        print(credit_score)
        break
    except ValueError:
        print("Invalid Input. Please Try Again")
while True:
        try:
            monthly_income = int(input("Enter your monthly Income: "))
            print(monthly_income)
            break
        except ValueError:
            print("Invalid Input. Please Try Again")
while True:
            try:
                monthly_payments = int(
                    input("Enter your monthly payments including rent, credit cards, loans and mortgage: "))
                print(monthly_payments)
                break
            except ValueError:
                print("Invalid Input. Please Try Again")
while True:
        try:
            loanAmt = int(input("Enter the loan amount you want to borrow: "))
            print(loanAmt)
            break
        except ValueError:
            print("Invalid Input. Please Try Again")

DI_ratio = monthly_payments / monthly_income
print("DI_ratio: " + str(DI_ratio))

rDownPayment = 0.20 * loanAmt
print("Required down payment : " + str(rDownPayment))

reqBankB = rDownPayment + (0.05 * loanAmt)
print("Required bank balance : " + str(reqBankB))

reqDE = 0.42
reqCS = 700
checknbal = DI_ratio



if checknbal > reqDE:
    print("YOUR INCOME IS LOWER THAN REQUIRED")
elif bank_st < reqBankB:
    print("PLEASE TRY FOR A LOWER LOAN AMOUNT")
elif credit_score < reqCS:
    print("YOUR CREDIT SCORE IS LOWER THAN REQUIRED")
else:
    print("CONGRATULATIONS YOU ARE PRE-QUALIFIED. SCHEDULE AN APPOINTMENT WITH US FOR NEXT STEP")
