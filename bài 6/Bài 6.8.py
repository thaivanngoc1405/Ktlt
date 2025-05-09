print("Thai Van Ngoc ")
print("MSSV:235752020710016 ")
print("#####################")
class ATM:
    def __init__(self, balance=0):
        self.balance = balance

    def check_balance(self):
        return self.balance

    def deposit(self, amount):
        self.balance += amount
        return f"Deposit successful. Your new balance is {self.balance}"

    def withdraw(self, amount):
        if amount > self.balance:
            return "Insufficient funds"
        else:
            self.balance -= amount
            return f"Withdrawal successful. Your new balance is {self.balance}"


def main():
    atm = ATM(1000)

    while True:
        print("\n*** Welcome to Simple ATM ***")
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            print(f"Your balance: {atm.check_balance()}")

        elif choice == "2":
            amount = float(input("Enter deposit amount: "))
            print(atm.deposit(amount))

        elif choice == "3":
            amount = float(input("Enter withdrawal amount: "))
            print(atm.withdraw(amount))

        elif choice == "4":
            print("Thank you for using our ATM. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
