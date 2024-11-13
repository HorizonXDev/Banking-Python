import server as s

def main():
    while True:
        print("\nWelcome to the Banking App!")
        print("1. Create Account")
        print("2. Check Balance")
        print("3. Deposit Money")
        print("4. Withdraw Money")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            username = input("Enter a username: ")
            initial_balance = float(input("Enter initial balance: "))
            success, message = s.create_account(username, initial_balance)
            print(message)

        elif choice == '2':
            username = input("Enter your username: ")
            success, message = s.check_balance(username)
            print(message)

        elif choice == '3':
            username = input("Enter your username: ")
            amount = float(input("Enter amount to deposit: "))
            success, message = s.deposit(username, amount)
            print(message)

        elif choice == '4':
            username = input("Enter your username: ")
            amount = float(input("Enter amount to withdraw: "))
            success, message = s.withdraw(username, amount)
            print(message)

        elif choice == '5':
            print("Exiting the banking app. Goodbye!")
            break

        else:
            print("Invalid choice, please try again.")

if __name__ == '__main__':
    main()
