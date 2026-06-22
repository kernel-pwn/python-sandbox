def show_balance(balance):
    print(f"Your current balance is ${balance:.2f}")

def deposit_():
    amount = float(input(f"enter an amount to deposit: $"))

    if amount < 0:
        print("----------------------------------")
        print()
        print("that's not a valid amount")
        return 0
    else:
        return amount

def withdraw(balance):
    amount = float(input("enter an amount to withdraw: "))
    print()
    if amount > balance:
        print("----------------------------------")
        print()
        print("insufficient funds")
        return 0
    elif amount < 0:
        print("amount must be greater than 0")
        return 0
    else:
        return amount

def main():
    balance = 0
    is_running = True

    while is_running:
        print("---------------")
        print("Banking program")
        print("---------------")
        print("1.show balance")
        print("2.deposit")
        print("3.withdraw")
        print("4.exit")
        print("----------------------------------")
        choice = input("Enter your choice (1-4): ")
        print("----------------------------------")
        print()

        if choice == "1":
            show_balance(balance)
        elif choice == "2":
            balance += deposit_()
        elif choice == "3":
            balance -= withdraw(balance)
        elif choice == "4":
            is_running = False
        else:
            print("Please enter a valid choice")
        print()
        print("----------------------------------")

    print("Thank you for using banking program")

if __name__ == "__main__":
    main()