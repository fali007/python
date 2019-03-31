from bs4 import BeautifulSoup

with open("styles.html") as fp:
	    soup = BeautifulSoup(fp)
temp=soup.find_all('h4')
# print(temp)
i=0
for a in temp:
	temp0 = soup.find_all('h4')[i]
	temp1=temp0.get_text()
	print(temp1)
	i+=1