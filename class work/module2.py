from ATM import checkbalance,deposit,withdraw,viewTransactions

u_pin= int(input("Enter the pin: "))

if login(u_pin):

    while True:
        print('\n\n\n')
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. View Transactions")
        print("0. Exit")

        ch = int(input("Enter the choice: "))
        if ch==1:
            checkbalance(u_pin)
        elif ch==2:
            deposit(u_pin)
        elif ch==3:
            withdraw(u_pin)
        elif ch==4:
            viewTransactions(u_pin)
        elif ch==0:
            print("Thankyou")
            break
        else:
            print("Invalid choice")