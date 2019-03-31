t=int(input())
key={}
value={}
maps={'sam':1234,'tom':3213}
for i in range(0,t):
	temp=input().split(" ")
	maps[temp[0]]=temp[1]
for k,v in maps.items():
	print("%s %s"%(k,v))
for i in range(0,t):
	name=input()
	if(maps.get(name)!=None):
		print("%s=%s"%(name,maps.get(name)))
	else:
		print("Not found")
