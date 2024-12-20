# initial version

balance = 0

def main():
    print("Balance: ", balance)
    deposit(100)
    withdraw(50)
    print("Balance: ", balance)

def deposit(n):
    balance += n

def withdraw(n):
    balance -= n


if __name__ == "__main__":
    main()

# fixing errors and next version introducing global to function

balance = 0

def main():
    print("Balance: ", balance)
    deposit(100)
    withdraw(50)
    print("Balance: ", balance)

def deposit(n):
    global balance
    balance += n

def withdraw(n):
    global balance
    balance -= n


if __name__ == "__main__":
    main() 


# object oriented programming

class Account:
    def __init__(self):
        self._balance = 0

    @property # instance veriable it controls how its red and writen.
    def balance(self):
        return self._balance
    
    def deposit(self, n):
        self._balance += n

    def withdraw(self, n):
        self._balance -= n

def main():
    account = Account()
    print("Balance: ", account.balance)
    account.deposit(100)
    account.withdraw(50)
    print("Balance: ", account.balance)

if __name__ == "__main__":
    main()