#!/usr/bin/env python
# -*- coding: utf-8 -*-
 
########################################################################
outfile = "/home/foo/output.txt"
profil = "/home/foo/.mozilla/firefox/fooprofile/"
username = "bar"
quiet = True
new = True
 
########################################################################
 
url = "https://reichelt.de"
 
 
from selenium.webdriver import Firefox # pip install selenium
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
from lxml import html
import requests
import codecs
 
"""Profile setzen"""
fp = webdriver.FirefoxProfile(profil)
browser = webdriver.Firefox(fp)
 
"""Warenkorb runterladen und in page_source speichern"""
browser.get(url)
button = browser.find_element_by_id('basketamount')
button.click()
page_source = browser.page_source
browser.close()
 
"""Parsen und Aufräumen"""
tree = html.fromstring(page_source)
 
artno = tree.xpath('//a[@xmlns=""]/text()')
artno = [x for x in artno if not x.startswith('\n')]
 
besch = tree.xpath('//li[@class="al_gall_liste_article_besch"]/text()')
 
anz = tree.xpath('//input[@type="text"]/@value')
while True:
	try:
		anz.remove("")
	except ValueError:
		break
 
epreis = tree.xpath('//span[@itemprop="price"]/text()')
summe = tree.xpath('//li[@class="PriceSum"]/text()')
 
 
"""Liste erstellen"""
def output(quiet,pfad,new):
	if pfad:
		f = codecs.open(pfad, "wb",encoding='utf-8')
		if new:
			f.write('^Wer^Stk^Artikelnummer^Beschreibung^Einzelpreis^Gesamt^Bemerkung^\n')
		for i in range(0,len(artno)):
			f.write('|'+username+'|')
			f.write(anz[i])
			f.write('|')
			f.write(artno[i])
			f.write('|')
			f.write(besch[i])
			f.write('|')
			f.write(epreis[i])
			f.write('|')
			f.write(summe[i])
			f.write('|')
			f.write(' ')
			f.write('|')
			f.write('\n')
		f.close()
	if quiet == False:
		if new:
			print '^Wer^Stück^Artikelnummer^Beschreibung^Einzelpreis^Gesamt^Bemerkung^'
		for i in range(0,len(artno)):
			print '|'+username+'|',
			print anz[i],
			print '|', 
			print artno[i], 
			print '|', 
			print besch[i], 
			print '|', 
			print epreis[i], 
			print '|', 
			print summe[i], 
			print '|', 
			print ' ', 
			print '|', 
			print '\n', 
 
output(quiet,outfile,new)
