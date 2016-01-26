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
	print quote
	return
	
def time(symbol,exch):
	base_url = 'https://in.finance.yahoo.com/q?s=' + symbol +'.'+ exch
	content = urllib.urlopen(base_url).read()
	m = re.search('id="yfs_t.*?"><.*?".*?">(.*?)<', content)
	if m:
		quote = 'Time Updated: ' + m.group(1)+"\n"
	else:
		quote = 'No quote available for: ' + symbol
	print quote
	return
	
def bse(symbol,exch):
	base_url = 'https://in.finance.yahoo.com/'
	content = urllib.urlopen(base_url).read()
	m1 = re.search('id="yfs_l84..b.*>(.*?)<', content)
	m2 = re.search('class="yfi-price-change.*">(.*?)<', content)
	m3 = re.search('b class="yfi-price-change.*">(.*?)<', content)
	if m1 and m2 and m3:
		quote = 'BSE: ' + m1.group(1)+'   '+m2.group(1)+'   '+m3.group(1)
	else:
		quote = 'No quote available for: ' + symbol
	print quote
	return

def nse(symbol,exch):
	base_url = 'https://in.finance.yahoo.com/'
	content = urllib.urlopen(base_url).read()
	m1 = re.search('id="yfs_l84..n.*>(.*?)<', content)
	m2 = re.search('id="yfs_c63_.nsei" class="c63">\s                                   <span class="yfi-price-change.*">(.*?)<',content)
	m3 = re.search('<span id="yfs_pp0_.nsei" class="pp0">\s\s\s\s\s\s\s                           \s\s\s<b class="yfi-price-change-green">(.*?)<',content)
	if m1 and m2 and m3:
		quote = 'NSE: ' + m1.group(1)+'    '+m2.group(1)+'    '+m3.group(1)+"\n"
	else:
		quote = 'No quote available for: ' + symbol
	print quote
	return
	
def run(nam,exch):
	ltp(nam,exch)
	color = checkColor(nam,exch)
	changePrice(nam,exch,color)
	changePerc(nam,exch,color) 
	time(nam,exch) 
	bse(nam,exch)
	nse(nam,exch)
	return

print "\n\n\t\t\t\tWelcome!\n\n"
ans=raw_input('Want to enter data? (Y/N)\n')
while ans=='y' or ans=='Y':
	exch = raw_input("\nEnter the exchange (BSE/NSE): ")
	nam = raw_input("\nEnter the name of the company: ")
	if exch =='nse' or exch=='ns' or exch=='n':
		run(nam,'NS')
	else:
		run(nam,'BO')
	ans=raw_input('Want to enter more? (Y/N)\n')
	
print "\n\n\t\t\t\tThank you!\n\n"


#class="ch bld.*?><.*>(.*?)<
#//*[@id="fac-ut"]/div[1]/div[2]/text()
#//*[@id="mainContent"]/div/div[1]/div[6]/div/div/div[175]/ul/li[1]/a
#//*[@id="mainContent"]/div/div[1]/div[6]/div/div/div[175]/ul/li[1]/a
#//*[@id="fac-ut"]/div[1]/div[2]/span/span/@data-symbol
