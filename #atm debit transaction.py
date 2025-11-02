#atm debit transaction
balance=10000.0
withdraw=int(input("enter the amount:"))
if withdraw>0:
    if withdraw%100==0:
        if withdraw<=balance:
            balance=balance-withdraw
            print("transaction successfully")
            print("available balance",balance)
        else:
            print("insufficient balance")
    else:
        print("invalid amount")

    