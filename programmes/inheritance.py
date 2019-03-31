class employee:
	amount=1.04
	def __init__(self,first,last,pay):
		self.first=first
		self.last=last
		self.pay=pay
		self.email=self.first+self.last+"@gmail.com"

	def fullname(self):
		return '{} {}'.format(self.first,self.last)

	def raise_salary(self):
		self.pay=int(self.pay*self.amount)

	@classmethod
	def set_raise_amount(cls,amount):
		cls.raise_amount=amount

emp_1=employee('felix', 'george',4000)
emp_2=employee('alex', 'john',6000)

print(emp_1.pay)
print(emp_2.pay)
employee.set_raise_amount(1.05)
emp_1.raise_salary()
emp_2.raise_salary()
print(emp_1.pay)
print(emp_2.pay)