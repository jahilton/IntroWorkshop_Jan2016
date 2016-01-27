'''class Customer():
	def __init__(self,name,balance,deposit,withdraw):
		self.balance = balance
		self.deposit = deposit
		self.withdraw = withdraw
	def new_balance(self):
		return self.balance - self.withdraw + self.deposit
	
Joe_Shmoe = Customer(25000,500,6000)

print('Current balance:','$'+str(Joe_Shmoe.balance))
print('Amount deposit:','$'+str(Joe_Shmoe.deposit))
print('Amount withdrawn:','$'+str(Joe_Shmoe.withdraw))
if Joe_Shmoe.new_balance() < 0:
	print('ERROR: Withdraw amount greater than available balance.')
	print('Overdraft by','$'+str(-1*Joe_Shmoe.new_balance()))
else:
	print('Remaining balance:','$'+str(Joe_Shmoe.new_balance()))
'''
#Other way
class Customer():
	def __init__(self,name,balance):
		self.name = name
		self.balance = balance
	def withdraw(self,amount):
		self.balance -= amount
		print(self.balance)
	def deposit(self,amount):
		self.balance += amount
		print(self.balance)
	def check_balance(self):
		print(self.balance)

joe = Customer('Joe',2000)
joe.check_balance()
