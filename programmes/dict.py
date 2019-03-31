from bs4 import BeautifulSoup
import requests
import csv
import pandas as pd
from pandas.io.json import json_normalize

data=open('word.json')
json_normalize(data)

url='https://www.thefreedictionary.com/'
# file=open('dict.txt','w')
dictionary=pd.read_csv('words.csv')

word='job'

url+=word


print(url)

page=requests.get(url)#return 200 tells download successful

soup = BeautifulSoup(page.text, 'html.parser')
temp=soup.find(class_='sds-list')

print(temp.get_text()[3:])

for i in range(0,len(dictionary)):
	word=dictionary[i]
	url+=word
	page=requests.get(url)
	soup=BeautifulSoup(page.text, 'html.parser')
	temp=soup.find(class_='sds-list')
	