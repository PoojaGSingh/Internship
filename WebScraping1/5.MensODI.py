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


page = requests.get("https://www.icc-cricket.com/rankings/mens/team-rankings/odi")


# In[4]:


page


# In[5]:


soup = BeautifulSoup (page.content)
soup


# In[6]:


team = []
for i in soup.find_all ("span" , class_="u-hide-phablet"):
    team.append(i.text)
teams = team [0:10]
teams


# In[7]:


matches = []
for i in soup.find_all ("td" , class_="rankings-block__banner--matches"):
    matches.append(i.text)
for i in soup.find_all ("td" , class_="table-body__cell u-center-text"):
    matches.append(i.text)
match = matches [1:20:2]

match


# In[8]:


points = []
for i in soup.find_all ("td" , class_="rankings-block__banner--points"):
    points.append(i.text)
for i in soup.find_all ("td" , class_="table-body__cell u-center-text"):
    points.append(i.text)
point = points [0:20:2]
point


# In[9]:


rating = []
for i in soup.find_all ("td" , class_="rankings-block__banner--rating u-text-right"):
    rating.append(i.text.strip(' \n'))
                  

for i in soup.find_all ("td" , class_="table-body__cell u-text-right rating"):
    rating.append(i.text)
ratings = rating [0:10]
ratings


# In[10]:


print (len(teams), len(match),len(point),len(ratings))


# In[11]:


MensODITeams = pd.DataFrame ({'Teams':teams, 'Matches':match, 'Points':point, 'Rating':ratings})
MensODITeams


# In[12]:


page = requests.get("https://www.icc-cricket.com/rankings/mens/player-rankings/odi/batting")
page


# In[13]:


bat = BeautifulSoup (page.content)
bat


# In[27]:


name = []

for i in bat.find_all ("div" , class_="rankings-block__banner--name-large"):
    name.append(i.text)


for i in bat.find_all ("td" , class_="table-body__cell rankings-table__name name"):
    name.append(i.a.text)
names = name[0:10]



names


# In[31]:


teamb = []
for i in bat.find ("div" , class_="rankings-block__banner--nationality"):
        teamb.append(i.text)

team = []

for i in bat.find_all ("span" , class_="table-body__logo-text"):
    team.append(i.text)


teams = team[0:9]
teams.insert(0,teamb[4])
teams[0] = 'PAK'

teams


        





# In[36]:


rating = []
for i in bat.find ("div" , class_="rankings-block__banner--rating"):
    rating.append(i.text)

for i in bat.find_all ("td" , class_="table-body__cell rating"):
    rating.append(i.text)
ratings = rating[0:10]
ratings


# In[37]:


print (len(names),len(teams),len(ratings))


# In[38]:


ODIBatsmen = pd.DataFrame ({'Name':names,'Team':teams,'Rating':ratings})
ODIBatsmen


# In[39]:


page = requests.get ("https://www.icc-cricket.com/rankings/mens/player-rankings/odi/bowling")
page


# In[40]:


bowl = BeautifulSoup (page.content)
bowl


# In[42]:


name = []
for i in bowl.find_all ("div" , class_="rankings-block__banner--name-large"):
    name.append(i.text)
for i in bowl.find_all ("td" , class_="table-body__cell rankings-table__name name"):
    name.append(i.a.text)
names = name[0:10]


names


# In[43]:


teamb = []
for i in bowl.find ("div" , class_="rankings-block__banner--nationality"):
        teamb.append(i.text)

team = []

for i in bowl.find_all ("span" , class_="table-body__logo-text"):
    team.append(i.text)


teams = team[0:9]
teams.insert(0,teamb[4])
teams[0] = 'NZ'

teams


# In[44]:


rating = []
for i in bowl.find ("div" , class_="rankings-block__banner--rating"):
    rating.append(i.text)

for i in bowl.find_all ("td" , class_="table-body__cell rating"):
    rating.append(i.text)
ratings = rating[0:10]
ratings


# In[45]:


print (len(names),len(teams),len(ratings))


# In[46]:


ODIBowlers = pd.DataFrame ({'Name':names,'Team':teams,'Rating':ratings})
ODIBowlers


# In[ ]:




