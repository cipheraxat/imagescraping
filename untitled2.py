# -*- coding: utf-8 -*-
"""
Created on Tue Jan 28 03:27:00 2020

@author: AKSHAT ANAND
"""

from selenium import webdriver
import urllib.request 

c2w_driver = webdriver.Chrome('C:/webdriver/chromedriver.exe')
i=1
c2w_driver.get('https://www.flipkart.com/mobiles-accessories/pr?sid=tyy&q=mobiles&otracker=categorytree')
price=c2w_driver.find_elements_by_class_name("a-price-whole")
i=1
while(i!=5):
    
    i=str(i)
    im=c2w_driver.find_element_by_xpath('//*[@id="container"]/div/div[3]/div[2]/div[1]/div[2]/div[2]/div/div['+i+']/div/a[1]/div[1]/div/div/img')
                          
    src = im.get_attribute('src')

    nam="captcha"+i+".png"
    i=int(i)
    i=i+1
    print(i)
    urllib.request.urlretrieve(src, nam)

c2w_driver.close()

#//*[@id="container"]/div/div[3]/div[2]/div[1]/div[2]/div[2]/div/div[1]/div/a[1]/div[1]/div/div/img

