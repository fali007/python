from bs4 import BeautifulSoup
import requests
import csv
url='http://rubberboard.org.in/public'
file=open('rubber.csv','w')

page=requests.get(url)#return 200 tells download successful

soup = BeautifulSoup(page.text, 'html.parser')
temp=soup.find_all(class_='price-table')

for i in range(0,4):
    temp1=soup.find_all(class_='price-table')[i]
    temp2=temp1.get_text()
    file.write(temp2+",")
file.close()
