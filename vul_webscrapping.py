import bs4
from urllib.request import Request,urlopen
from bs4 import BeautifulSoup as soup

#my_url='https://pythonprogramming.net/parsememcparseface/'
my_url='https://threats.kaspersky.com/en/vulnerability/'

req=Request(my_url, headers={'User-Agent': 'Mozilla/5.0'})
web_byte = urlopen(req).read()
# opening connection to grab the page html
#uClient=req(my_url)
#web_byte=uClient.read()
#close the connection
#uClient.close()

page_soup = soup(web_byte, "html.parser")
#csv creation
filename="vul.csv"
f=open(filename,"w")

#grabs all categories

table = page_soup.table
table_rows = table.find_all('tr')
for tr in table_rows:
    kId= tr.find_all('td')[0].get_text().strip()
    name= tr.find_all('td')[1].get_text().strip()
    prod= tr.find_all('td')[2].get_text().strip()
    date= tr.find_all('td')[3].get_text().strip()
    cvss= tr.find_all('td')[4].get_text().strip()
    print(kId +"," + name +","+ prod +","+ date +","+ cvss +"\n")
    f.write(kId +"," + name +","+ prod +","+ date +","+ cvss +"\n")
f.close()
#containers = page_soup.findAll("table",{"class":"table_informations vulnerability table_informations_produkts list2_uyazvim"})

#containersA= page_soup.findAll("div",{"id":"detection_types_container"})
#categories= page_soup.findAll("li",{"class":"symbol"})




