import time

def ks(n,c):
	w=[None,1,2,3,4,5]
	v=[None,5,3,5,3,2]
	if n==0 or c==0:
		result=0
	elif w[n]>c:
		result=ks(n-1,c)
	else:
		temp1=ks(n-1,c)
		temp2=v[n]+ks(n-1,c-w[n])
		result=max(temp1,temp2)
	return result

def ks_dy(n,c,temp):
	w=[None,1,2,3,4,5]
	v=[None,5,3,5,3,2]
	if temp[n][c]!=None:
		return temp[n][c]
	elif n==0 or c==0:
		result=0
	elif w[n]>c:
		result=ks_dy(n-1,c,temp)
	else:
		temp1=ks_dy(n-1,c,temp)
		temp2=v[n]+ks_dy(n-1,c-w[n],temp)
		result=max(temp1,temp2)
	temp[n][c]=result
	return result

a=5
b=100
temp=[[None]*(b+1)for i in range(a+1)]
start_time=time.time()
print(ks(a,b))
print("%s"%(time.time()-start_time))
start_time=time.time()
print(ks_dy(a,b,temp))
print("%s"%(time.time()-start_time))