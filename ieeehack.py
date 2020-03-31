import requests
from bs4 import BeautifulSoup,SoupStrainer
#import winsound
import webbrowser as wb
import time

class datacollecter:
	

	def __init__(self):
		self.h={
			"User-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'
		}


	def t_searcher(self, key):
		hold="https://www.google.com/search?q="
		key=key.replace(' ',"+")
		url=hold+key
		ls=[]
		st=[]
		ress=requests.get(url,headers=self.h)
		ss=BeautifulSoup(ress.content,'html.parser')
		for div in ss.find_all('div',attrs={'class':'rc'}):
			for link in div.find_all('a'):
				s=str(link['href'])
				if s.find("ieeexplore") >= 0 and len(s)<50:
					ls.append(s)
					st.append(link.find('h3').text)

		return 	ls,st	

					

	def p_searcher(self,url):
		url="https://www.sci-hub.tw/"+url
		ress=requests.get(url,headers=self.h)
		ss=BeautifulSoup(ress.content,'html.parser')
		for link in ss.find_all('a'):
		    oo=str(link).find("pdf")
		    if  oo>=0:
		    	a,q,h1=str(link).split("'")
		    	if q.find("https:")==-1:
		    		q="https:"+q
		    	x=q.split('?')
		    	print(x[0])
		    	wb.open(x[0])


#dc=datacollecter()
#l1,l2=dc.t_searcher("ieee object detection using cnn")
#print(l2)