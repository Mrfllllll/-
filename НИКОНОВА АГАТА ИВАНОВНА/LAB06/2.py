class BankAccount:
    def __init__(self, start_balance):
        self.__balance = start_balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance = self.__balance + amount
        else:
            print("Нельзя пополнить на неположительную сумму.")

    def withdraw(self, amount):
        if amount <= 0:
            print("Сумма снятия должна быть больше 0.")
            return

        if amount <= self.__balance:
            self.__balance = self.__balance - amount
        else:
            print("Недостаточно средств. Баланс:", self.__balance)

    def get_balance(self):
        return self.__balance


acc1 = BankAccount(100)
acc2 = BankAccount(50)

acc1.deposit(30)
acc1.withdraw(200)
acc1.withdraw(50)

acc2.withdraw(10)
acc2.deposit(100)

print("Баланс acc1:", acc1.get_balance())
print("Баланс acc2:", acc2.get_balance())
print("Попытка обойти приватность:", acc1._BankAccount__balance)
