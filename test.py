import requests
import openpyxl
from bs4 import BeautifulSoup
import requests

url = "https://www.home.ge/saxlebi-agarakebi/iyideba-saxlebi-agarakebi/iyideba-sakhli-bakuriani-297726.html"

html_text = requests.get(url).text
soup = BeautifulSoup(html_text, 'html.parser')

sqm_tag = soup.find_all('div', class_= "value")

sqm_list = []
for sqm in sqm_tag:
    sqm_info = sqm.text.lstrip().rstrip()
    sqm_split = sqm_info.split(" ")
    if len(sqm_split) == 2:
        if "113" in sqm_split:
            sqm_join = "".join(sqm_split)
            print(sqm_join)
            
            


        
    
