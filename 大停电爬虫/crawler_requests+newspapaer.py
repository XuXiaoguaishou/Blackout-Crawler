
# -*- coding: utf-8 -*-
from selenium import webdriver
import requests
from bs4 import BeautifulSoup as BF
import re
import readability
from newspaper import Article
from newspaper.api import fulltext
import time
import os

import multiprocessing

method="requests_newspaper"
key_list=['大停电',"停电","大规模停电"]
MAX_PAGEs=10

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate, compress',
    'Accept-Language': 'en-us;q=0.5,en;q=0.3',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:22.0) Gecko/20100101 Firefox/22.0'
}


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

def get_url_set(driver,key_word):
    container_list=[]           #存放临时URL
    real_url_set=set()          #URL集

    #百度搜索结果
    baidu_url="https://www.baidu.com/s?ie=UTF-8&wd="+key_word
    driver.get(baidu_url)
    #获取每条搜索结果的URL
    for page in range(1,MAX_PAGEs+1):
        BF1=BF(driver.page_source)   
        #print(driver.page_source)
        page_container_list=BF1.findAll("div",{"class":re.compile(".*c-container.*")})
        container_list.extend(page_container_list)
        b=driver.find_element_by_xpath("//*[text()='下一页>']").click()
        
        time.sleep(2)

    #将每条URL进行一次跳转，得到初始URL，并添加进real_url_set中
    for container in container_list:
        href=container.find('h3').find('a').get('href')
        try:
            baidu_url = requests.get(url=href, headers=headers, allow_redirects=False)
        except:
            continue
        real_url = baidu_url.headers['Location']  #得到网页原始地址
        if real_url.startswith('http'):
            real_url_set.add(real_url + '\n')


    #必应搜索结果
    
    being_url="https://cn.bing.com/search?q="+key_word+"&FORM=PORE"
    try:
        driver.get(being_url)
    except:
        driver.refresh()
    #需要刷新一下界面
    time.sleep(2)
    driver.refresh()
    time.sleep(5)
    for page in range(1,MAX_PAGEs+1):
        BF1=BF(driver.page_source)   
        #print(driver.page_source)
        page_container_list=BF1.find("ol",{"id":"b_results"}).findAll("h2")
        for page_container in page_container_list:
            try:
                real_url_set.add(page_container.find("a").get('href'))
            except:
                break
        b=driver.find_element_by_xpath(".//*[@title='下一页']").click()
        time.sleep(2)

    #谷歌暂时没做
    #google_url=""
    return real_url_set

def getArticle(key_word,real_url_set):
    path="C:/Users/Liuyus/Desktop/大停电爬虫/"+method+key_word
    os.mkdir(path)
    print(real_url_set)
    count=0
    for real_url in real_url_set:
        try:
            time.sleep(1)
            response=requests.get(url=real_url, headers=headers)
            print(response.text)
            text=fulltext(response.text,language='zh')

            #news=Article(real_url,language='zh')
            #news.download()
            #news.parse()
            print(real_url)
            #print(news.text)
            filename=str(count)+".txt"
            f=open(path+"/"+filename,"w")
            #f.write(news.title)
            f.write(real_url)
            #f.write(news.text)
            print(text)
            f.write(text)
            f.close()
            count=count+1
        except:
            continue
    return 0
        
if __name__ == '__main__':
    for key_word in key_list:
        driver=get_driver()
        real_url_set=get_url_set(driver,key_word)
        getArticle(key_word,real_url_set)

