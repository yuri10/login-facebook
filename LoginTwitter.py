# -*- coding: utf-8 -*-
"""
Created on Tue Jun  2 15:27:56 2020

@author: olive
"""

from selenium import webdriver

driver = webdriver.Chrome("C:/chromedriver.exe")

driver.get('https://twitter.com/login')


def login(email, password):
    #css selector path
    email_path = '#react-root > div > div > div.css-1dbjc4n.r-13qz1uu.r-417010 > main > div > div > form > div > div:nth-child(6) > label > div > div.css-1dbjc4n.r-18u37iz.r-16y2uox.r-1wbh5a2.r-1udh08x > div > input'
    password_path = '#react-root > div > div > div.css-1dbjc4n.r-13qz1uu.r-417010 > main > div > div > form > div > div:nth-child(7) > label > div > div.css-1dbjc4n.r-18u37iz.r-16y2uox.r-1wbh5a2.r-1udh08x > div > input'
    botao_path = '#react-root > div > div > div.css-1dbjc4n.r-13qz1uu.r-417010 > main > div > div > form > div > div:nth-child(8) > div'
    
    #identifica e retorna os elementos
    email_element = driver.find_element_by_css_selector(email_path)
    password_element = driver.find_element_by_css_selector(password_path)
    botao_element = driver.find_element_by_css_selector(botao_path)
    
    #manda as informacoes para os campos
    email_element.send_keys(email)
    password_element.send_keys(password)
    
    #clicka no botao de logar
    botao_element.click()

password = input('Digite a senha do Twitter: ')
email = 'oliveirayuri10@hotmail.com'

login(email, password)

