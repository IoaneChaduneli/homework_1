import requests,json
from bs4 import BeautifulSoup

url = "https://ss.ge/ka/udzravi-qoneba/qiravdeba-saofise-farti-axali-rustavi-6550403"

html_text = requests.get(url).text

parse_html = BeautifulSoup(html_text, 'html.parser')

data_dict = {}

title = parse_html.find('h1').text
description = parse_html.find('span', class_ ="details_text").text
sqm = parse_html.find('text').text
status = parse_html.find('span', class_= 'PRojeachBlack').text
image = parse_html.find('div', class_= 'OrdinaryContainer').find('img').get('src')



data_dict['title'] = title
data_dict['description'] = description
data_dict['sqm'] = sqm
data_dict['status'] = status
data_dict['image'] = image

with open('data.json', 'w') as jfile:
    json.dump(data_dict, jfile)

with open('data.json', 'r') as jfile:
    data = json.load(jfile)




