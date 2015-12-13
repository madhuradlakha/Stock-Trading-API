import urllib
import re
from lxml import html
import requests
from termcolor import colored, cprint
#import stockquote

def ltp(symbol,exch):
    base_url = 'https://in.finance.yahoo.com/q?s=' + symbol +'.'+ exch
    content = urllib.urlopen(base_url).read()
    m = re.search('id="yfs_l.*?">(.*?)<', content)
    if m:
        quote = "\n"+'Last Traded Price of %s: '%(symbol.upper()) + m.group(1)
    else:
        quote = 'No quote available for: ' + symbol
    print quote
    return

def changePrice(symbol,exch,color):
	base_url = 'https://in.finance.yahoo.com/q?s=' + symbol +'.'+ exch
	content = urllib.urlopen(base_url).read()
	m = re.search('id="yfs_c.*?"><.*?>(.*?)<', content)
	if m:
		quote = 'Change: ' + m.group(1)[3:]
	else:
		quote = 'No quote available for: ' + symbol
	print colored(quote,color)
	return
	
def changePerc(symbol,exch,color):
	base_url = 'https://in.finance.yahoo.com/q?s=' + symbol +'.'+ exch
	content = urllib.urlopen(base_url).read()
	m = re.search('id="yfs_p4.*?">(.*?)<', content)
	if m:
		quote = 'Percentage change: ' + m.group(1)[1:-1]
	else:
		quote = 'No quote available for: ' + symbol
	print colored(quote,color)
	return
      
def checkColor(symbol,exch):
	base_url = 'https://in.finance.yahoo.com/q?s=' + symbol +'.'+ exch
	content = urllib.urlopen(base_url).read()
	m = re.search('.*<span class="(.*?)_. time.*?"><', content)
	if m:
		quote = m.group(1)
		if quote == 'up':
			return 'green'
		elif quote == 'down':
			return 'red'
		else:
			return 'yellow'
	return
		
def date(symbol,exch):
	base_url = 'https://in.finance.yahoo.com/q?s=' + symbol +'.'+ exch
	content = urllib.urlopen(base_url).read()
	m = re.search('id="yfs_t.*?">(.*?)<', content)
	if m:
		quote = 'Time updated: ' + m.group(1)
	else:
		quote = 'No quote available for: ' + symbol
	print quote+'\n'
	return
	
def run(nam,exch):
	ltp(nam,exch)
	color = checkColor(nam,exch)
	changePrice(nam,exch,color)
	changePerc(nam,exch,color) 
	date(nam,exch) 

ans=raw_input('Want to enter more?\n')
while ans=='y':
	exch = raw_input("\nEnter the exchange: ")
	nam = raw_input("\nEnter the name of the company: ")
	if exch =='nse' or exch=='ns' or exch=='n':
		run(nam,'NS')
	else:
		run(nam,'BO')
	ans=raw_input('Want to enter more?\n')
	
print "\nThank you!"


#class="ch bld.*?><.*>(.*?)<
#//*[@id="fac-ut"]/div[1]/div[2]/text()
#//*[@id="mainContent"]/div/div[1]/div[6]/div/div/div[175]/ul/li[1]/a
#//*[@id="mainContent"]/div/div[1]/div[6]/div/div/div[175]/ul/li[1]/a
#//*[@id="fac-ut"]/div[1]/div[2]/span/span/@data-symbol
