import threading

class BankAccount(threading.Thread):
    def __init__(self,  *args, **kwargs):
        super(BankAccount, self).__init__(*args, **kwargs)
        self.balans = 1000
        self.lock = threading.Lock()

    def deposit(self, amount):
        self.amount = amount
        with self.lock:
            self.balans += self.amount
            print(f'Deposited {self.amount}, new balance is {self.balans}')

    def withdraw(self, amount):
        self.amount = amount
        with self.lock:
            self.balans -= self.amount
            print(f'Withdrew {self.amount}, new balance is {self.balans}')

def deposit_task(account, amount):
    for _ in range(5):
        account.deposit(amount)

def withdraw_task(account, amount):
    for _ in range(5):
        account.withdraw(amount)

account = BankAccount()

deposit_thread = threading.Thread(target=deposit_task, args=(account, 100))
withdraw_thread = threading.Thread(target=withdraw_task, args=(account, 150))

deposit_thread.start()
withdraw_thread.start()

deposit_thread.join()
withdraw_thread.join()