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

def changePrice(symbol,exch):
	base_url = 'https://in.finance.yahoo.com/q?s=' + symbol +'.'+ exch
	content = urllib.urlopen(base_url).read()
	m = re.search('id="yfs_c.*?"><.*?>(.*?)<', content)
	if m:
		quote = 'Change: ' + m.group(1)[3:]
	else:
		quote = 'No quote available for: ' + symbol
	print colored(quote,'green')
	return
	
def changePerc(symbol,exch):
	base_url = 'https://in.finance.yahoo.com/q?s=' + symbol +'.'+ exch
	content = urllib.urlopen(base_url).read()
	m = re.search('id="yfs_p4.*?">(.*?)<', content)
	if m:
		quote = 'Percentage change: ' + m.group(1)[1:-1]
	else:
		quote = 'No quote available for: ' + symbol
	print colored(quote+"\n",'green')
	return
      
def run(nam,exch):
	ltp(nam,exch)
	changePrice(nam,exch)
	changePerc(nam,exch)  

exch = raw_input("\nEnter the exchange: ")
nam = raw_input("\nEnter the name of the company: ")
if exch =='nse':
	run(nam,'NS')
else:
	run(nam,'BO')

#class="ch bld.*?><.*>(.*?)<
#//*[@id="fac-ut"]/div[1]/div[2]/text()
#//*[@id="mainContent"]/div/div[1]/div[6]/div/div/div[175]/ul/li[1]/a
#//*[@id="mainContent"]/div/div[1]/div[6]/div/div/div[175]/ul/li[1]/a
#//*[@id="fac-ut"]/div[1]/div[2]/span/span/@data-symbol
