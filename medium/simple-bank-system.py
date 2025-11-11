 
class Bank:
    def validate(self, a):
        return 1 <= a < len(self.balance)

    def __init__(self, balance: List[int]):
        self.balance = [0] + balance

    def transfer(self, a: int, b: int, money: int) -> bool:
        if not self.validate(a) or not self.validate(b):
            return False

        if self.balance[a] < money:
            return False

        self.balance[a] -= money
        self.balance[b] += money

        return True



    def deposit(self, account: int, money: int) -> bool:
        if not self.validate(account):
            return False
        self.balance[account] += money
        return True

        

    def withdraw(self, account: int, money: int) -> bool:
        if not self.validate(account):
            return False

        if self.balance[account] < money:
            return False 

        self.balance[account] -= money

        return True


# Your Bank object will be instantiated and called as such:
# obj = Bank(balance)
# param_1 = obj.transfer(account1,account2,money)
# param_2 = obj.deposit(account,money)
# param_3 = obj.withdraw(account,money)
