# -*- coding: utf-8 -*-
"""
Created on Thu Oct 30 13:02:31 2014

@author: absa
"""
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import csv
driver=webdriver.Firefox()
driver.get("http://www.espn.com.mx/futbol/jugador/_/id/45843/")
#subUrl='http://www.espndeportes.com/futbol/jugador/_/id/')

r=requests.get('http://www.espndeportes.com/futbol/jugador/_/id/')
data=[]
dict={}
maxJugadores=213420
minJugadores=2654

elem=driver.find_element_by_css_selector("#statsTab>a")
elem.click()
soup=BeautifulSoup(driver.page_source,"html5lib")
#for cuenta in range(minJugadores,2660):
name=soup.find("div",class_="profile")
items=  soup.find("ul",class_="profile-items")
numero=0
posicion="NoDisp"
edad=0
fecha_Nacimiento="NoDisp"
lugar_Nacimiento="NoDisp"
altura=0.0
peso="NoDisp"
names=['Nombre','Numero','Posicion','Fecha_Nacimiento','Lugar_Nacimiento',
       'Altura','Peso',]
f=open("/home/absalnc/Python/messi.csv","w")       
if name:
    nombre=name.contents[0].string
    if items:
        count = 0
        for ch in items:            
        
            if count==0:
                numero=ch.string
            if count==1:
                posicion=ch.string
            if count==2:
                edad=ch.string
            if count==3:
                fecha_Nacimiento=ch.string
            if count==4:
                lugar_Nacimiento=ch.string
            if count==5:
                altura=ch.string
            if count==6:
                peso=ch.string
        
            count+=1
            #print ch.string
    
#    w=csv.DictWriter(f)
    #f.write(profile.encode('utf-8'.strip()))

    


    
    stats=soup.find("div",id="ui-tabs-1")
    for child in stats.findAll('table',):
        count =0   
        for tr in child.findAll('tr',{"class":lambda L:L!="colhead"}):
            if count==0 :
                dict["Temporada"]=tr.text.encode('utf-8'.strip())
                dict["Nombre"]=nombre
                dict["Posicio"]=posicion
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
                    print dict
 #                   w.writerow(dict,delimiter=',',fieldnames=names)
            count+=1       
    #print data 
    f.close()#print dict
        
    #f.write(child.encode('utf-8'.strip()))
   
    #print count 
#print data
