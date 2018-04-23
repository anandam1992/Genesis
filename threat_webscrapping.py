import bs4
from urllib.request import Request,urlopen
from bs4 import BeautifulSoup as soup

#my_url='https://pythonprogramming.net/parsememcparseface/'
my_url='https://threats.kaspersky.com/en/threat/'

req=Request(my_url, headers={'User-Agent': 'Mozilla/5.0'})
web_byte = urlopen(req).read()
# opening connection to grab the page html
#uClient=req(my_url)
#web_byte=uClient.read()
#close the connection
#uClient.close()

page_soup = soup(web_byte, "html.parser")
#csv creation
filename="threat.csv"
f=open(filename,"w")

#grabs all categories

table = page_soup.table
table_rows = table.find_all('tr')
for tr in table_rows:    
    name= tr.find_all('td')[0].get_text().strip()
    date= tr.find_all('td')[1].get_text().strip()
    print(name +"," + date +"\n")
    f.write(name +"," + date +"\n")
f.close()





