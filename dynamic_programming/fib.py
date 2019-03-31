import time
def fib(n):
	if(n==1) or (n==2):
		result=1
	else:
		result=fib(n-1)+fib(n-2)
	return result

def fib_dy(n,memo):
	if memo[n]!=None:
		return memo[n]
	if n==1 or n==2:
		result=1
	else:
		result=fib_dy(n-1,memo)+fib_dy(n-2,memo)
	memo[n] = result
	return result

def fib_bot(n):
	if n==1 or n==2:
		return 1
	bottom_up=[None]*(n+1)
	bottom_up[1]=1
	bottom_up[2]=1
	for i in range(3,n+1):
		bottom_up[i]=bottom_up[i-1]+bottom_up[i-2]
	return bottom_up[n]

a=35
memo=[None]*(a+1)
start_time=time.time()
print(fib(a))
print("%s" % (time.time() - start_time))
start_time=time.time()
print(fib_dy(a,memo))
print("%s" % (time.time() - start_time))
start_time=time.time()
print(fib_bot(a))
print("%s" % (time.time() - start_time))
