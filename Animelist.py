from bs4 import BeautifulSoup
# from requests_html import HTMLsession
import requests
from datetime import datetime
import time
import smtplib
import input
import pandas as pd
import csv

with open('User.csv', 'r', newline='') as f:
    data=csv.reader(f)
    for dt in data:
        if(dt[1]=="Null" or dt[1]=="animename"):
            continue

         
        string=dt[1].replace(' ', '-')
        url=f"https://www.animefillerlist.com/shows/{string}"

        load=requests.get(url)
        soup=BeautifulSoup(load.content, 'html.parser')
        all=soup.find('table', class_='EpisodeList')

        smt=smtplib.SMTP('smtp.gmail.com','587')
        smt.ehlo()
        smt.starttls()
        smt.login('srivathsgondi19@gmail.com','rsmsxvueknxoibtx')
        #print(len(episodes))
        pdate=datetime.now().date()

        episodes=all.find_all('tr', class_=['filler','manga_canon','mixed_canon/filler','anime_canon'])
        for episode in episodes:
            eptitle=episode.find('td', class_='Title').text
            epnumber=episode.find('td', class_='Number').text
            epdate=episode.find('td', class_='Date').text
            #print(f"The episode number is{epnumber} and the date of release is:  {epdate} \n\n")
            date=datetime.strptime(epdate,  '%Y-%m-%d').date()
            if(date>pdate):
                break
            elif(date==pdate):
                smt.sendmail('srivathsgondi19@gmail.com',
                                    f'{dt[0]}',
                                    f"subject: Reminder \n\n Your new episode number {epnumber} of {dt[1]} has arrived \n {eptitle}! \n")

        


    
    


    

