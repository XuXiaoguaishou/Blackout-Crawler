
# -*- coding: utf-8 -*-
from selenium import webdriver
import requests
from bs4 import BeautifulSoup as BF
import re
import readability
from newspaper import Article
import time

key_words="大停电"
max_pages=10

url1='https://www.baidu.com/s?ie=UTF-8&wd='
url=url1+key_words

def get_driver():
    options=webdriver.ChromeOptions()
    prefs={
        'profile.default_content_setting_values': {
            'images': 2,
            #'video':2
        }
    }
    options.add_experimental_option('prefs',prefs)
    return webdriver.Chrome(chrome_options=options)

driver =get_driver()
driver.get(url)

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate, compress',
    'Accept-Language': 'en-us;q=0.5,en;q=0.3',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:22.0) Gecko/20100101 Firefox/22.0'
}

real_url_list=[]
container_list=[]
for page in range(1,max_pages+1):
        BF1=BF(driver.page_source)   
        #print(driver.page_source)
        page_container_list=BF1.findAll("div",{"class":re.compile(".*c-container.*")})
        container_list.extend(page_container_list)
        b=driver.find_element_by_xpath("//*[text()='下一页>']").click()
        time.sleep(2)

#get all URLs

for container in container_list:
    href=container.find('h3').find('a').get('href')
    try:
        baidu_url = requests.get(url=href, headers=headers, allow_redirects=False)
    except:
        continue
    real_url = baidu_url.headers['Location']  #得到网页原始地址
    if real_url.startswith('http'):
        real_url_list.append(real_url + '\n')

#get all original URLs

print(real_url_list)
for real_url in real_url_list:
    try:
        news=Article(real_url,language='zh')
        news.download()
        news.parse()
        print(real_url)
        print(news.text)
    except:
        continue
#get the body content of webpages
