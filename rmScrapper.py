#-*- coding: utf-8 -*- 
from bs4 import BeautifulSoup
import urllib
import re
import requests
import json


r1 = urllib.urlopen('https://www.rottentomatoes.com').read()
soup1 = BeautifulSoup(r1, "lxml")
#print (soup1.get_text)
link5=soup1.find('a',id="Top-Box-Office-view-all")
link5=link5['href']
#print link5
#print type(link5)

r5=urllib.urlopen('https://www.rottentomatoes.com'+link5).read()
soup7=BeautifulSoup(r5,"lxml")
jsons=list()
jsons=soup7.find_all('script')
jsons= str(jsons[35])
jsons=jsons.split(";")[7]
jsons=jsons.split(",")
newlists=list()
k=0
for t in jsons:
	if t.find("url")>0:
		k=k+1
		t=t[6:]
		t=t.replace('"','')
		#list.extend(newlists,t)
		#print type(t)
		#print(t)
		r = urllib.urlopen('https://www.rottentomatoes.com'+t).read()
		soup = BeautifulSoup(r, "lxml")
		comment=soup.find_all('p',class_="comment clamp clamp-6")
		links=list()
		links=soup.findAll('a', href=True, text=re.compile("All Critics"))
		link1=links[1]['href'] 
		r2=urllib.urlopen("https://www.rottentomatoes.com"+link1).read()
		soup2=BeautifulSoup(r2, "lxml")
		page=str()
		page=soup2.find('span',{'class':'pageInfo'})
		i=page.text.split(" ")[3]
		out_file = open("//Users/Alicia/Desktop/nwhack/text"+str(k)+".txt", "a")
		out_file1 = open("//Users/Alicia/Desktop/nwhack/image"+str(k)+".txt", "a")
		imge=soup.find('img',class_="posterImage")
		print imge['src']
		out_file1.write(imge['src']+"\n")
		for num in range(1,int(i)):
			num1=str(num)
			r3=urllib.urlopen("https://www.rottentomatoes.com"+link1+"/?page="+num1+"&sort=").read()
			soup3=BeautifulSoup(r3, "lxml")
			comment2=str()
		#	for review in soup3.find_all('div',class_="the_review"):
		#		out_file.write(review.text.encode('utf-8')+"\n")
			


