while True:
    accno=int(input("Enter account no: "))
    name =input("Enter name: ")
    if(accno == 123456789 and name == "Sanju"):
       print("Account is matched")
    else:
       print("Account is not matched")

    balance=int(input("Enter bank Balance: "))

    transaction = input("Do you want to withdrawl/deposit: ").lower()

    if transaction == "withdrawl":

       withdrawl=int(input("Enter a amount to withdrawl: "))

       if(balance>=withdrawl):
          print("The balance amount in the account is: ",balance-withdrawl)
       else:
          print("Insufficient Balance")

    elif transaction =="deposit":

        deposit=int(input("Enter a amount to deposit: "))

        if(deposit>=0):
           print("The balance after deposited the amount: ",balance+deposit)
        else:
           print("Deposit amount should not be an negative")


    response = input("Do you want to continue transaction? (yes/no): ")
    if response.lower() != "yes":
       print("Thank you for your transaction.")
       break


