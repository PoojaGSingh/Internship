#!/usr/bin/env python
# coding: utf-8

# In[2]:


get_ipython().system('pip install bs4')
get_ipython().system('pip install requests')


# In[3]:


# importing required libraries
from bs4 import BeautifulSoup
import requests
import pandas as pd


# In[4]:


page = requests.get("https://www.imdb.com/india/top-rated-indian-movies/?sort=ir,desc&mode=simple&page=1")


# In[5]:


page


# In[6]:


soup = BeautifulSoup (page.content)
soup


# In[7]:


name = []
for i in soup.find_all ('td' , class_='titleColumn'):
    name.append (i.a.text)
    
name


# In[8]:


rating = []
for i in soup.find_all ('td' , class_='ratingColumn imdbRating'):
    rating.append (i.text[1:4])
    
rating


# In[9]:


yor = []
for i in soup.find_all ('span' , class_='secondaryInfo'):
    yor.append (i.text)
yor
    
    


# In[10]:


print(len(name),len(rating),len(yor))


# In[11]:


df= pd.DataFrame({'Name':name[0:99],'Rating':rating[0:99],'Year Of Release':yor[0:99]})
df


# In[ ]:




