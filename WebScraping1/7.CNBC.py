#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install bs4')
get_ipython().system('pip install requests')


# In[2]:


from bs4 import BeautifulSoup
import requests
import pandas as pd


# In[3]:


page = requests.get("https://www.cnbc.com/world/")
page


# In[4]:


soup = BeautifulSoup (page.content)
soup


# In[5]:


headline = []

for i in soup.find_all ("div", class_="SecondaryCard-headline"):
    headline.append(i.a.text)

for i in soup.find_all ("div", class_="LatestNews-headlineWrapper"):
    headline.append(i.a.text)



headline


# In[16]:


time = []

for i in soup.find_all ("time" , class_="LatestNews-timestamp"):
    time.append(i.text)
time.insert(0 , '-----')
time.insert(1 , '-----')

time


# In[10]:


link = []
for i in soup.find_all ("div", class_="SecondaryCard-headline"):
    link.append(i.a['href'])

for i in soup.find_all ("a" , class_="LatestNews-headline"):
    link.append(i['href'])
link


# In[17]:


print (len(headline), len(time), len(link))


# In[19]:


Headlines = pd.DataFrame({'Headline':headline, 'Time':time, 'Link':link})
Headlines


# In[ ]:




