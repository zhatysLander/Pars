import requests
from bs4 import BeautifulSoup
from time import sleep

headers={'User-agent':
        'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.5) Gecko/20091102 Firefox/3.5.5 (.NET CLR 3.5.30729)'}

for count in range(1,8):
    sleep(3)
    url=f'https://scrapingclub.com/exercise/list_basic/?page={count}'
    responce=requests.get(url,headers=headers)
    # print(responce)
    # print(responce.text)

    soup=BeautifulSoup(responce.text,'lxml')
    # print(soup)

    data=soup.find_all('div',class_='col-lg-4 col-md-6 mb-4')
    # print(data)
    for i in data:
        name= i.find('h4',class_='card-title').text.replace('\n',"")
        # print(name)
        price=i.find('h5').text
        # print(price)
        url_img='https://scrapingclub.com'+i.find('img',class_='card-img-top img-fluid').get('src')
        print(name+'\n'+price+'\n'+url_img+'\n\n')