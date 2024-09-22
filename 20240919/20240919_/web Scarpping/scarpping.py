#https://www.bbc.com/news



""""import requests
from bs4 import BeautifulSoup
news_url='https://www.bbc.com/news'
news_res=requests.get(news_url)
soup=BeautifulSoup(news_res.content,'html.parser')
headings=soup.find_all('h2')

with open('new_deading.txt','w',encoding='UTF-8') as news_file:
    for heading in headings:
        news_file.write(heading.text+'\n')

print('bbc') """





""" import subprocess
result = subprocess.run(['python','-c','print(2**3)'],capture_output=True,text=True)
print(result.stdout)
"""



