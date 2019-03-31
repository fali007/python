class employee:
	amount=1.04
	def __init__(self,first,last,pay):
		self.first=first
		self.last=last
		self.pay=pay
		self.email=first+last+"@gmail.com"

	def fullname(self):
		return '{} {}'.format(self.first,self.last)

	def raise_amount(self):
		self.pay=int(self.pay*self.amount)


emp_1=employee('jake','bilal',2000)
emp_2=employee('nake','num',3000)

print(emp_1.email)
print(emp_1.fullname())
print(emp_1.pay)
emp_1.raise_amount()
print(emp_1.pay)

print(emp_2.email)
print(emp_2.fullname())
print(emp_2.pay)
emp_2.raise_amount()
print(emp_2.pay)

employee.amount=1.05

print(emp_1.email)
print(emp_1.fullname())
print(emp_1.pay)
emp_1.raise_amount()
print(emp_1.pay)

print(emp_2.email)
print(emp_2.fullname())
print(emp_2.pay)
emp_2.raise_amount()
print(emp_2.pay)