# -*- coding: utf-8 -*-
"""
Created on Wed Sep 14 08:31:15 2022
1-mavzu, Taymerni ishga tushirish.Moslik shablonlari.2-mavzu, takrorlash
@author: HP
"""
# vaqtni aniqalash dasturi vvv
from datetime import datetime
nw=datetime.now()
yil=nw.strftime("%d-%B,%Y-yil, %H:%M:%S")
#print(yil)
sonlar=list(range(0,51))
#print(sonlar)
print(f"{yil} kunda {sonlar} sonlarni sanadik. E'tiboringgiz uchun raxmat.")
# Vaqtni anqlash va rendom orqali ismni, mevani tanlash .vvv
print('---------------')
import random as tanlash
guruh=['Akmal','Begzod','Salim','Odil','Komil','Tohir','Ilhom']
mevalar=["olma",'behi','nok','uzum','banan','apilsin']
son=tanlash.choice(guruh)
son1=tanlash.choice(mevalar)
#print(son)
print(f"{son} {yil} kuni {son1}ni tanlab oldi.")












