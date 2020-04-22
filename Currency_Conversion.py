import requests 
from bs4 import BeautifulSoup
resp=requests.get('http://data.fixer.io/api/latest?access_key=['YOUR API_KEY']&format=1')
con_url=resp.content
resp_dict = resp.json()
dict=resp_dict['rates']
for i in dict:
	inp_cur=input('Enter the currency that you want to convert ')
	print(dict[inp_cur])
	


