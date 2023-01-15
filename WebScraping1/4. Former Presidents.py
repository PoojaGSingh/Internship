#!/usr/bin/env python
# coding: utf-8

# In[41]:


get_ipython().system('pip install bs4')
get_ipython().system('pip install requests')


# In[42]:


# importing required libraries
from bs4 import BeautifulSoup
import requests
import pandas as pd


# In[43]:


page = requests.get("https://presidentofindia.nic.in/former-presidents.htm")


# In[44]:


page


# In[45]:


soup = BeautifulSoup (page.content)
soup


# In[46]:


name = []
for i in soup.find_all ('div' , class_='presidentListing'):
    name.append (i.h3.text.split('(')[0])
    
name


# In[47]:


tenure = []
for i in soup.find_all ('div' , class_='presidentListing'):
    tenure.append (i.p.text.split(':')[1])
    
tenure


# In[48]:


print(len(name),len(tenure))


# In[49]:


df= pd.DataFrame({'Name':name,'Tenure':tenure})
df


# In[ ]:




