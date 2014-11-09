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
       'Altura','Peso','Temporada','Equipo','Competicion','Iniciados','Bancas',
       'Goles','Asistencias','Disparos','Al_Arco','Cometidas','Recibidas',
       'Amarillas','Rojas']
f=open("/home/absalnc/Python/messi.csv","w")       
if name:
    nombre=name.contents[0].string.encode('utf-8'.strip())
    if items:
        count = 0
        for ch in items:            
        
            if count==1:
                numero=ch.string.encode('utf-8'.strip())
            if count==3:
                posicion=ch.string.encode('utf-8'.strip())
            if count==5:
                edad=ch.string.encode('utf-8'.strip())
            if count==7:
                fecha_Nacimiento=ch.string.encode('utf-8'.strip())
            if count==9:
                lugar_Nacimiento=ch.string.encode('utf-8'.strip())
            if count==11:
                altura=ch.string.encode('utf-8'.strip())
            if count==13:
                peso=ch.string.encode('utf-8'.strip())
        
            count+=1
            
    
    w=csv.DictWriter(f,delimiter=',',fieldnames=names)
    w.writeheader()

    


    
    stats=soup.find("div",id="ui-tabs-1")
    for child in stats.findAll('table',):
        count =0   
        for tr in child.findAll('tr',{"class":lambda L:L!="colhead"}):
            dict["Nombre"]=nombre
            dict["Numero"]=numero
            dict["Posicion"]=posicion
            dict["Lugar_Nacimiento"]=lugar_Nacimiento
            dict["Fecha_Nacimiento"]=fecha_Nacimiento
            dict["Altura"]=altura
            dict["Peso"]=peso
            if count==0 :
                dict["Temporada"]=tr.text.encode('utf-8'.strip())
                
            else:
                countb=0
                for td in tr.findAll("td"):                                       
                    if countb==0:
                       dict["Equipo"] =td.text.encode('utf-8'.strip())
                    if countb==1:
                        dict["Competicion"]=td.text.encode('utf-8'.strip())
                    if countb==2:
                        dict["Iniciados"]=int(td.text)
                    if countb==3:
                        dict["Bancas"]=int(td.text)
                    if countb==4:
                        dict["Goles"]=int(td.text)
                    if countb==5:
                       dict["Asistencias"] =int(td.text)
                    if countb==6:
                        dict["Disparos"]=int(td.text)
                    if countb==7:
                        dict["Al_Arco"]=int(td.text)
                    if countb==8:
                        dict["Cometidas"]=int(td.text)
                    if countb==9:
                        dict["Recibidas"]=int(td.text)
                    if countb==10:
                        dict["Amarillas"]=int(td.text)
                    if countb==11:
                        dict['Rojas']=int(td.text)
                
                    countb+=1                                 
                w.writerow(dict)
            count+=1       
    f.close()
