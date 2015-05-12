#!/usr/bin/env python
# -*- coding: utf-8 -*-
 
from selenium.webdriver import Firefox # pip install selenium
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
from lxml import html
from os import sys
 
url="https://www.reichelt.de/"
wiki=sys.argv[1]
 
browser = webdriver.Firefox()
 
"""Wiki Seite öffnen, Tabelle parsen"""
browser.get(wiki)
page_source = browser.page_source
 
tree = html.fromstring(page_source)
artno = tree.xpath('//td[@class="col2 leftalign"]/text()')
artno = [x.strip() for x in artno]
 
menge = tree.xpath('//td[@class="col1 leftalign"]/text()') 
menge = [x.strip() for x in menge]
 
"""Reichelt Warenkorb öffnen, Eingabe finden"""
browser.get(url)
button = browser.find_element_by_id('basketamount')
button.click()
 
field_artnr = browser.find_element_by_id("DirectInput_1")
field_menge = browser.find_element_by_id("DirectInput_1_count")
 
 
 
for i in range(0,len(artno)):
	field_artnr.send_keys(''.join(artno[i]))
	field_menge.send_keys(''.join(menge[i]),Keys.ENTER)
	field_artnr = browser.find_element_by_id("DirectInput_1")
	field_menge = browser.find_element_by_id("DirectInput_1_count")
