#!/usr/bin/env python
# coding: utf-8

# In[ ]:


get_ipython().system('pip install bs4')
get_ipython().system('pip install requests')


# In[ ]:


# importing required libraries
from bs4 import BeautifulSoup
import requests
import pandas as pd


# In[ ]:


page = requests.get("https://www.imdb.com/chart/moviemeter/?sort=ir,desc&mode=simple&page=1")


# In[ ]:


page


# In[ ]:


soup = BeautifulSoup (page.content)
soup


# In[ ]:


name = []
for i in soup.find_all ('td' , class_='titleColumn'):
    name.append (i.a.text)
    
name


# In[ ]:


rating = []
for i in soup.find_all ('td' , class_='ratingColumn imdbRating'):
    rating.append (i.text[1:4])
    
rating


# In[135]:


yor = []
for i in soup.find_all ('span' , class_='secondaryInfo'):
    yor.append (i.text)
yor
    
    


# In[147]:


r = '\n'

for i in yor:
        if r in i :
            continue
        else:
            year_of_release.append(i)
year_of_release


# In[148]:


print(len(name),len(rating),len(year_of_release))


# In[149]:


df= pd.DataFrame({'Name':name,'Rating':rating,'Year Of Release':year_of_release})
df


# In[ ]:




