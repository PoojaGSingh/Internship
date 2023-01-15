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


page = requests.get("https://www.journals.elsevier.com/artificial-intelligence/most-downloaded-articles")
page


# In[4]:


soup = BeautifulSoup (page.content)
soup


# In[6]:


title = []

for i in soup.find_all ("h2" , class_="sc-1qrq3sd-1 gRGSUS sc-1nmom32-0 sc-1nmom32-1 btcbYu goSKRg"):
    title.append(i.text)
title


# In[8]:


authors = []

for i in soup.find_all ("span" , class_="sc-1w3fpd7-0 dnCnAO"):
    authors.append(i.text)
authors


# In[10]:


date = []

for i in soup.find_all ("span" , class_="sc-1thf9ly-2 dvggWt"):
    date.append(i.text)
date


# In[14]:


url = []
for i in soup.find_all ("a" , class_="sc-5smygv-0 fIXTHm"):
    url.append(i['href'])
url


# In[15]:


print (len(title), len(authors),len(date),len(url))


# In[16]:


AIArticles = pd.DataFrame({'Title':title,'Authors':authors,'PublishedDate':date,'PaperURL':url})
AIArticles


# In[ ]:




