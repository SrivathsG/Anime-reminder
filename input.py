
import random
import keyboard
import os
import smtplib
import time
from bs4 import BeautifulSoup
import requests
import csv
from csv import writer
import pandas as pd
import numpy as np

accounts = pd.read_csv('User.csv', usecols=[0])
global flag
if (len(accounts) == 0):
    flag = 0
else:
    flag = 1
temperorygmail = ''

try:
    smt = smtplib.SMTP('smtp.gmail.com', '587')
    smt.ehlo()
    smt.starttls()
    smt.login('srivathsgondi19@gmail.com', 'rsmsxvueknxoibtx')
except:
    print(" \n\nERROR: Unable to fetch the request, Check your Internet connection \n\n")
    exit()


def Account(flag):
    os.system('cls')
    accounts = pd.read_csv('User.csv', usecols=[0])
    Accounts = np.unique(accounts)
    # print(Accounts)
    i = 0
    if(flag==1):
        print("\t\n Choose from the following accounts\n")
    for account in Accounts:

        print(f" \n{i}:{account} \n")
        i += 1
    while (1):
        for i in range(0, np.size(Accounts)+1):
            if (keyboard.is_pressed(f"{i}")):
                gm = Accounts[i]
                global temperorygmail
                temperorygmail = gm
                # flag = 1

                home(temperorygmail)
                break

        if (flag == 0):
            print("Signup? press s")
            time.sleep(4)
            while (1):
                if (keyboard.is_pressed("s")):
                    retry(flag)


def resend(gm):
    keyboard.unhook_all()
    otp=''
    for i in range(0, 4):
        otp += str(random.randint(0, 9))
    # gm = input("Please enter the gmail where you wish to be notified: \n")
    smt.sendmail('srivathsgondi19@gmail.com',
                 f'{gm}', f'subject: Verification code \n\n The otp for signing up is: \n {otp}')
    uotp = input(f"please enter the otp sent to the gmail address {gm} \n\n")
    if (uotp == otp):
        print("Successfully signed up")
        with open('User.csv', 'a') as f:
            write = csv.writer(f)
            # blank=[]
            # write.writerow(blank)
            gmail=[gm, 'Null']
            write.writerow(gmail)

        # Also to make a moving text displaying returning to home
        home(gm)
    else:
        print("invalid otp \n")
        print(''' 
                r: Retry
                s: Resend Otp
                e: Home
                ''')
        while (1):
            if (keyboard.is_pressed == "r"):
                retry(flag)
                break
            if (keyboard.is_pressed == "s"):
                resend(gm)
                break
            if (keyboard.is_pressed == "e"):
                home()
                break


def retry(flag):
    os.system('cls')
    otp = ''
    for i in range(0, 4):
        otp += str(random.randint(0, 9))
    g = input("Please enter the gmail where you wish to be notified : \n")
    try:
        smt.sendmail('srivathsgondi19@gmail.com',
                    f'{g}', f'subject: Verification code \n\n The otp for signing up is: \n {otp}')
        uotp = input(f"please enter the otp sent to the gmail address {g} \n\n")
    except:
        print("Invalid Gmail!! \n")
        time.sleep(3)
        print("\n R: retry or H: Return Home \n")
        while(1):
            if(keyboard.is_pressed("r")):
                retry(flag)
            if(keyboard.is_pressed("h")):
                home(temperorygmail)
    # write code to check if the gmail already exists

    if (uotp == otp):

        print("Successfully signed up")
        time.sleep(3)

        with open('User.csv', 'a') as f:
            write = csv.writer(f, lineterminator='\n')
            # blank=[]
            # write.writerow(blank)   # Activate it when needed
            gmail = [f"{g}", "Null"]
            write.writerow(gmail)
        if (flag == 0):
            flag = 1
            Account(flag)
        # Also to make a moving text displaying returning to home

        home(temperorygmail)
    else:
        print("invalid otp \n")
        print(''' 
                r: Retry
                s: Resend Otp
                e: Home
                ''')
        while (1):
            if (keyboard.is_pressed("r")):
                retry()
                break
            if (keyboard.is_pressed("s")):
                resend(temperorygmail)
                break
            if (keyboard.is_pressed("e")):
                home()
                break


######     || ABOVE CODE FOR SIGNUP||  ######
     ######     || ABOVE CODE FOR SIGNUP||  ######
          ######     || ABOVE CODE FOR SIGNUP||  ######
              ######     || ABOVE CODE FOR SIGNUP||  ######

def add(gm):
    os.system('cls')
    wanime = []

    url = "https://www.animefillerlist.com/shows"
    load = requests.get(url)
    soup = BeautifulSoup(load.content, 'html.parser')
    groups = soup.find_all('li')
    animes = []

    for group in groups[4:]:

        animes.append(group.text)
        # print(f"{group.text} \n")

    # reenter option
    inp = "yes"
    fl = ""
    while (inp == "yes"):
        os.system('cls')
        anime = input("please enter the anime you wish to be notified \n")
        for an in animes:
            if (anime == an):
                fl = int(1)  # flag variable
                wanime.append(anime)
                print("Successfully added \n")
                break

        if (fl == ""):
            print("we couldnt find the anime you were looking for please check if it exists in the following list \n\n")
            for ani in animes:
                print(f"{ani} \n")
            print(
                "\n If you found please enter in the exact name as displayed with dashes instead of spaces \n")
        inp = input("ADD ANOTHER or retry? \n")

    with open('User.csv', 'a') as f:
        write = csv.writer(f, lineterminator='\n')
        # blank=[]
        # write.writerow(blank) #when needed
        for wani in wanime: 
            attribute = [gm, wani]
            write.writerow(attribute)
    f.close()
    time.sleep(3)
    home(gm)


def remove(gm):

    ask = "yes"
    while (ask == "YES" or ask == "yes" or ask == "Yes"):
        os.system('cls')
        fl = ""
        with open('User.csv', 'r') as f:
            read = csv.reader(f)
            newfile = []
            a = input("Enter the anime you wish to delete \n")
            for r in read:
                if (a == r[1] and gm == r[0]):
                    fl = 1
                    continue
                else:
                    newfile.append(r)

            if (fl == 1):
                with open('User.csv', 'w', newline='') as f:
                    write = csv.writer(f)
                    write.writerows(newfile)
                    print(" \nSuccessfully deleted \n")
            else:
                with open('User.csv', 'r', newline='') as f:
                    read = csv.reader(f)
                    print(" \nCouldn't find, try deleting from the following \n")
                    for i in read:
                        if (i[1] == "Null" or i[1] == "animename"):
                            continue
                        print(f"{i[1]} \n")

            print("\n")
            ask = input("Delete another or retry? YES/NO")
        f.close()
    home(gm)


def showlist(gm):
    os.system('cls')
    keyboard.unhook_all()
    with open('User.csv','r') as f:
        data=csv.reader(f)
        for dt in data:
            if(dt[1]=="animename" or dt[1]=="Null"):
                continue
            if(dt[0]==gm):
                print(f"\n {dt[1]} ")
    f.close()     
    print("\nH : RETURN HOME")
    while(1):
        if(keyboard.is_pressed("h")):
            home(gm)
            break  


def home(gm):  # Main interface for the user
    keyboard.unhook_all()
    os.system('cls')
    if(flag==0):
        print("Make an Account first ")
        time.sleep(2.5)
        retry(flag)
    
    print(''' 
                    a: ADD ACCOUNT
                    b: ADD A NEW ANIME
                    c: REMOVE AN ANIME
                    d: CHANGE ACCOUNT
                    e: Showlist
          ''')
    while (1):
        if (keyboard.is_pressed("a")):
            retry(flag)
            break
        if (keyboard.is_pressed("b")):
            add(gm)
            break
        if (keyboard.is_pressed("c")):
            remove(gm)
            break
        if (keyboard.is_pressed("d")):
            Account(flag)
            break
        if (keyboard.is_pressed("e")):
            showlist(gm)
            break


Account(flag)
