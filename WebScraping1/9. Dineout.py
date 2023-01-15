#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install bs4')
get_ipython().system('pip install requests')


# In[2]:


# importing required libraries
from bs4 import BeautifulSoup
import requests
import pandas as pd


# In[3]:


page = requests.get("https://www.dineout.co.in/delhi-restaurants/buffet-special")


# In[4]:


page


# In[6]:


soup = BeautifulSoup (page.content)
soup


# In[8]:


name = []
for i in soup.find_all ('a' , class_='restnt-name ellipsis'):
    name.append (i.text)
    
name


# In[10]:


cusine = []
for i in soup.find_all ('span' , class_='double-line-ellipsis'):
    cusine.append (i.text.split('|')[1])
cusine


# In[12]:


location = []
for i in soup.find_all ('div' , class_='restnt-loc ellipsis'):
    location.append (i.text)
    
location


# In[13]:


ratings = []
for i in soup.find_all ('div' , class_='restnt-rating rating-4'):
    ratings.append (i.text)
    
ratings


# In[21]:


image = []
for i in soup.find_all ('img' , class_='no-img'):
    image.append (i.get('data-src'))
image


# In[23]:


print(len(name),len(cusine),len(location),len(ratings),len(image))


# In[24]:


df= pd.DataFrame({'Name':name,'Cusine':cusine,'Location':location,'Ratings':ratings,'ImgURL':image})
df


# In[ ]:




