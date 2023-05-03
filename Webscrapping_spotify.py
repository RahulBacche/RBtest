#!/usr/bin/env python
# coding: utf-8

# In[9]:


input_url = "https://charts.spotify.com/charts/view/regional-us-weekly/2023-04-27"


# In[5]:


from time import sleep
from datetime import date, timedelta
import random
from random import randint
from time import sleep
import datetime
import time
import json
import requests
from bs4 import BeautifulSoup
import pandas as pd
import re
import os 


# In[6]:


#from webdriver_manager.chrome import ChromeDriverManager
#from webdrivermanager import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


# In[8]:


userid='rahulbacche3@gmail.com'
password='Rahul@0707'
print("Login to the Spotifty using:" ,userid)


# In[10]:


def get_raw_data(input_url):
    
    #s = Service('/tmp/chrome/latest/chromedriver_linux64/chromedriver')
    s = Service(executable_path=ChromeDriverManager().install())
    options = webdriver.ChromeOptions()
    options.binary_location = "/tmp/chrome/latest/chrome-linux/chrome"
    options.add_argument('headless')
    options.add_argument('--disable-infobars')
    options.add_argument('--disable-dev-shm-usage')
    user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36'    
    options.add_argument('user-agent={0}'.format(user_agent))
    options.add_argument('--no-sandbox')
    options.add_argument('--remote-debugging-port=9222')
    options.add_argument('--homedir=/tmp/chrome/chrome-user-data-dir')
    options.add_argument('--user-data-dir=/tmp/chrome/chrome-user-data-dir')
    prefs = {"download.default_directory":"/tmp/chrome/chrome-user-data-di",
           "download.prompt_for_download":False}
  
    options.add_experimental_option("prefs",prefs)
    driver = webdriver.Chrome(service=s, options=options)
    

    driver.get(input_url)
    time.sleep(2)
    sleep(randint(12,14))
    wait = WebDriverWait(driver, 21)

    if driver.current_url !=input_url:
        driver.get('https://accounts.spotify.com/en/login?continue=https%3A%2F%2Fcharts.spotify.com/login')
    #login_button = WebDriverWait(driver, 11).until(EC.presence_of_element_located((By.XPATH, '//*[@id="__next"]/div/div/main/div[2]/div/header/div/div[2]/a[3]/div[1]')))
    #login_button.click()
        sleep(randint(20,25))
        username = WebDriverWait(driver, 11).until(EC.presence_of_element_located((By.XPATH, '//*[@id="login-username"]')))
        sleep(randint(1,2))
        username.click()
        sleep(randint(1,2))
        username.send_keys(userid)
        sleep(randint(1,2))
        pwd = WebDriverWait(driver, 11).until(EC.presence_of_element_located((By.XPATH, '//*[@id="login-password"]')))
        sleep(randint(1,2))
        pwd.click()
        sleep(randint(1,2))
        pwd.send_keys(password)
        sleep(randint(1,2))
        enter_button = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, '//*[@id="login-button"]/span[1]')))
        sleep(randint(1,2))
        enter_button.click()   
        sleep(randint(12,14))
        print("Logged in Successfully")
        print(driver.current_url)
        driver.save_screenshot('screenshot.png')
        driver.get(input_url)
        sleep(randint(25,30))
    
        if driver.current_url == 'https://charts.spotify.com/home':
            login_button = WebDriverWait(driver, 11).until(EC.presence_of_element_located((By.XPATH, '//*[@id="__next"]/div/div/main/div[2]/div/header/div/div[2]/a[3]/div[1]')))
            login_button.click()
            sleep(randint(12,14))
            username = WebDriverWait(driver, 11).until(EC.presence_of_element_located((By.XPATH, '//*[@id="login-username"]')))
            sleep(randint(1,2))
            username.click()
            sleep(randint(1,2))
            username.send_keys(userid)
            sleep(randint(1,2))
            pwd = WebDriverWait(driver, 11).until(EC.presence_of_element_located((By.XPATH, '//*[@id="login-password"]')))
            sleep(randint(1,2))
            pwd.click()
            sleep(randint(1,2))
            pwd.send_keys(password)
            sleep(randint(1,2))
            enter_button = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, '//*[@id="login-button"]/span[1]')))
            sleep(randint(1,2))
            enter_button.click()   
            sleep(randint(12,14))

            driver.get(input_url)
            sleep(randint(20,25))

            print(driver.current_url)
            soup=''
            soup = BeautifulSoup(driver.page_source,"html.parser")
            sleep(randint(12,14))
            try:
                main=(soup.findAll('table')[0].tbody.findAll('tr'))
            except:
                soup=''
                soup = BeautifulSoup(driver.page_source,"html.parser")
                main=(soup.findAll('table')[0].tbody.findAll('tr'))


        else:
            print("running beautiful soap else loop--2")
            driver.get(input_url)
            sleep(randint(30,50))
            print(driver.current_url)
            sleep(randint(12,14))
            soup=''
            soup = BeautifulSoup(driver.page_source,"html.parser")
            sleep(randint(12,14))
            try:
                main=(soup.findAll('table')[0].tbody.findAll('tr'))
            except:
                sleep(randint(12,14))
                soup=''
                soup = BeautifulSoup(driver.page_source,"html.parser")
                sleep(randint(12,14))
                main=(soup.findAll('table')[0].tbody.findAll('tr'))
    else:
        print("running beautiful soap else loop--3")
        print(driver.current_url)
        sleep(randint(12,14))
        soup=''
        soup = BeautifulSoup(driver.page_source,"html.parser")
        sleep(randint(12,14))
        try:
            main=(soup.findAll('table')[0].tbody.findAll('tr'))
        except:
            soup=''
            soup = BeautifulSoup(driver.page_source,"html.parser")
            main=(soup.findAll('table')[0].tbody.findAll('tr'))
    
    driver.close()
    return main


# In[11]:


main = get_raw_data(input_url)


# In[29]:


def create_dataframe_weekly_top_artists(main):
  '''
  Create datframe for top artists using raw json data
  '''
  rank_list = []
  artist_name_list = []
  peak_list = []
  prev_list =[]
  streak_list =[]
  url_list = []

  for item in main:

    rank = item.find('span', {'class': 'Type__TypeElement-goli3j-0 hgLxdb'}).text
    rank_list.append(rank)

    artist_name = item.find('span', {'class': 'styled__StyledTruncatedTitle-sc-135veyd-22 kKOJRc'}).text
    artist_name_list.append(artist_name)

    peak = item.find_all('td', {'class': 'TableCell__TableCellElement-sc-1nn7cfv-0 dLdEGj styled__RightTableCell-sc-135veyd-4 kGfYTK'})[0].text
    peak_list.append(peak)

    prev = item.find_all('td', {'class': 'TableCell__TableCellElement-sc-1nn7cfv-0 dLdEGj styled__RightTableCell-sc-135veyd-4 kGfYTK'})[1].text
    prev_list.append(prev)

    streak = item.find_all('td', {'class': 'TableCell__TableCellElement-sc-1nn7cfv-0 dLdEGj styled__RightTableCell-sc-135veyd-4 kGfYTK'})[2].text
    streak_list.append(streak)

    url = item.find('div', {'class': 'styled__Wrapper-sc-135veyd-14 gPJpnT'}).find('a',attrs={'href': re.compile("^https://")}).get('href')
    url_list.append(url)
    
  Value=(zip(rank_list, artist_name_list, peak_list, prev_list, streak_list, url_list))
  columns=['Rank','Artist','Peak','Prev','Streak','URL']
  df = pd.DataFrame(Value, columns=columns)
    
  return df


# In[30]:


raw_df=create_dataframe_weekly_top_artists(main)


# In[33]:


#raw_df.head()


# In[ ]:


raw_df.to_csv('data.csv', index=False)

