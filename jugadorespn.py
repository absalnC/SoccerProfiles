# -*- coding: utf-8 -*-
"""
Created on Thu Oct 30 13:02:31 2014

@author: absa
"""
import requests
from bs4 import BeautifulSoup
from selenium import webdriver

driver=webdriver.Firefox()
driver.get("http://www.espn.com.mx/futbol/jugador/_/id/45843/")
#subUrl='http://www.espndeportes.com/futbol/jugador/_/id/')

r=requests.get('http://www.espndeportes.com/futbol/jugador/_/id/')
data=[]
dict={}
maxJugadores=213420
minJugadores=2654


#for cuenta in range(minJugadores,2660):
 #   print cuenta
#r=requests.get(subUrl+str(cuenta))
#text=r.text.encode('utf-8').strip()
#soup=BeautifulSoup(text,"html5lib")
#name=soup.find("div",class_="profile")
 #   items=  soup.find("ul",class_="profile-items")
 #   
   
#    if name:
#        print name.contents[0]
#        if items:
#            for ch in items:
#               print ch.string
#f=open("/home/absalnc/Documentos/procesado.html","w")
#f.write(profile.encode('utf-8'.strip()))
elem=driver.find_element_by_css_selector("#statsTab>a")
elem.click()

text=r.text.encode('utf-8').strip()
soup=BeautifulSoup(driver.page_source,"html5lib")
#print soup.prettify
stats=soup.find("div",id="ui-tabs-1")
for child in stats.findAll('table',):
    count =0   
    for tr in child.findAll('tr',{"class":lambda L:L!="colhead"}):
        if count==0 :
            dict["Temporada"]=tr.text.encode('utf-8'.strip())
        else:
            countb=0
            for td in tr.findAll("td"):
                if countb==0:
                    dict["Equipo"]=td.text
                if countb==1:
                    dict["Competicion"]=td.text
                if countb==2:
                    dict["Iniciados"]=int(td.text)
                if countb==3:
                    dict["Bancas"]=int(td.text)
                if countb==4:
                    dict["Goles"]=int(td.text)
                if countb==5:
                    dict["Asistencias"]=int(td.text)
                if countb==6:
                    dict["Disaros"]=int(td.text)
                if countb==7:
                    dict["Al_arco"]=int(td.text)
                if countb==8:
                    dict["Cometidas"]=int(td.text)
                if countb==9:
                    dict["Recibidas"]=int(td.text)
                if countb==10:
                    dict["Amarillas"]=int(td.text)
                if countb==11:
                    dict["Rojas"]=int(td.text)
                countb+=1
            data.append(dict)
        count+=1       
    #print dict
        
    #f.write(child.encode('utf-8'.strip()))
   
    #print count 
print data
