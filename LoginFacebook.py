# -*- coding: utf-8 -*-
"""
Created on Tue Jun  2 13:48:55 2020

@author: olive
"""

from selenium import webdriver

driver = webdriver.Chrome("C:/chromedriver.exe")

driver.get('https://facebook.com')


#css selector path
email_path = '#email'
password_path = '#pass'
botao_path = '#u_0_b'

#identifica e retorna os elementos
email_element = driver.find_element_by_css_selector(email_path)
password_element = driver.find_element_by_css_selector(password_path)
botao_element = driver.find_element_by_css_selector(botao_path)

#manda as informacoes para os campos
email_element.send_keys('oliveirayuri10@msn.com')
password_element.send_keys('coloqueSuaSenhaAqui')

#clicka no botao de logar
botao_element.click()














