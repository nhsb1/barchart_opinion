#!/usr/bin/env python
from bs4 import BeautifulSoup
import urllib2


def get_barchart_opinion(ticker):
	"""
    Returns barchart.com opinion as a percentage (e.g. 88%) from URL - https://www.barchart.com/stocks/quotes/OLED/opinion
    """

	baseurl = 'https://www.barchart.com/stocks/quotes/'
	endurl = ticker
	urlsuffix = '/opinion'
	url = baseurl + ticker + urlsuffix
	page = urllib2.urlopen(url)
	soup = BeautifulSoup(page.read(), "lxml")
	#data = soup.find_all("div", {"class": "opinion-status"}) 
	try:
		data2 = soup.find("span", {"class": "opinion-percent buy"})
	except:
		data2 = "NA"
	try:
		data3 = soup.find("span", {"class": "opinion-percent sell"})
	except:
		data3 = "NA"


	return data2, data3 #


opinion_buy, opinion_sell = get_barchart_opinion('OLED')

if opinion_buy is not None:
	print "Buy: " + opinion_buy.text

if opinion_sell is not None:
	print "Sell: " + opinion_sell.text
