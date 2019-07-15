
# -*- coding: utf-8 -*-
from selenium import webdriver
import requests
from bs4 import BeautifulSoup as BF
import re
import readability
from newspaper import Article
import time
import os


headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate, compress',
    'Accept-Language': 'en-us;q=0.5,en;q=0.3',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:22.0) Gecko/20100101 Firefox/22.0'
}

MAX_PAGEs=10
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


    #谷歌  #需使用VPN
def get_url_set(driver,key_word):
    container_list=[]           #存放临时URL
    real_url_set=set()          #URL集

    baidu_url_list=["https://www.baidu.com/s?ie=UTF-8&wd="+key_word,"https://www.baidu.com/s?ie=UTF-8&tn=news&wd="+key_word]
    for i in range(2):
        driver.get(baidu_url_list[i])
        #获取每条搜索结果的URL
        for page in range(1,MAX_PAGEs+1):
            BF1=BF(driver.page_source,'lxml')   
            #print(driver.page_source)
            if i==0:
                page_container_list=BF1.findAll("div",{"class":re.compile(".*c-container.*")})
            else:
                page_container_list=BF1.findAll("div",{"class":re.compile("result")})
            #print(page_container_list)
            container_list.extend(page_container_list)
            b=driver.find_element_by_xpath("//*[text()='下一页>']").click() 
            time.sleep(2)
        if i==0:
            #print(container_list)
            for container in container_list:
                print(container)
                href=container.find("h3").find("a").get("href")
                try:
                    baidu_url = requests.get(url=href, headers=headers, allow_redirects=False)
                except:
                    continue
                real_url = baidu_url.headers['Location']  #得到网页原始地址
                if real_url.startswith('http'):
                    real_url_set.add(real_url + '\n')
                container_list=[]
        else:
            for container in container_list:
                href=container.find("h3").find("a").get("href")
                if "baijiahao" not in href:
                    real_url_set.add(href)
    return real_url_set
    

key_word="大停电"
driver=get_driver()
real_url_set=get_url_set(driver,key_word)
print(real_url_set)
print(len(real_url_set))