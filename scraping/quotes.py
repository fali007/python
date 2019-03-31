from bs4 import BeautifulSoup
import requests
import csv
url='https://www.brainyquote.com/quote_of_the_day'
file=open('quotes.txt','w')

page=requests.get(url)#return 200 tells download successful

soup = BeautifulSoup(page.text, 'html.parser')
temp=soup.find_all(class_='oncl_q')
i=0
for a in temp:
	temp1=soup.find_all(class_='oncl_q')[i]
	auth=soup.find_all('a',class_='oncl_a')[i-1]
	temp2=temp1.get_text()
	auth1=auth.get_text()
	file.write('"'+temp2+'"'+" -"+auth1+'\n')
	i+=1
file.close()
