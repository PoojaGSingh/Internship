#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install bs4')
get_ipython().system('pip install requests')


# In[2]:


# importing required libraries
from bs4 import BeautifulSoup
import requests


# In[3]:


page = requests.get("https://www.wikipedia.org/")


# In[4]:


page


# In[5]:


soup = BeautifulSoup (page.content)
soup


# In[19]:


head = []

for i in soup.find_all ('meta'):
    print (i)

head

    


# In[ ]:




