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


page = requests.get("https://www.icc-cricket.com/rankings/womens/team-rankings/odi")
page


# In[4]:


soup = BeautifulSoup (page.content)
soup


# In[5]:


team = []
for i in soup.find_all ("span" , class_="u-hide-phablet"):
    team.append(i.text)
teams = team [0:10]
teams


# In[13]:


bmatches = []
for i in soup.find_all ("td" , class_="rankings-block__banner--matches"):
    bmatches.append(i.text)
matches = []
for i in soup.find_all ("td" , class_="table-body__cell u-center-text"):
    matches.append(i.text)
match = matches[0:18:2]
match.insert(0,bmatches[0])


match


# In[10]:


wpoints = []
for i in soup.find_all ("td" , class_="rankings-block__banner--points"):
    wpoints.append(i.text)
point = []
for i in soup.find_all ("td" , class_="table-body__cell u-center-text"):
    point.append(i.text)
points = point[1:19:2]
points.insert(0,wpoints[0])


points


# In[11]:


rating = []
for i in soup.find_all ("td" , class_="rankings-block__banner--rating u-text-right"):
    rating.append(i.text.strip(' \n'))
                  

for i in soup.find_all ("td" , class_="table-body__cell u-text-right rating"):
    rating.append(i.text)
ratings = rating [0:10]
ratings


# In[14]:


print (len(teams), len(match),len(points),len(ratings))


# In[15]:


WODITeams = pd.DataFrame ({'Teams':teams, 'Matches':match, 'Points':points, 'Rating':ratings})
WODITeams


# In[16]:


page = requests.get("https://www.icc-cricket.com/rankings/womens/player-rankings/odi/batting")
page


# In[17]:


bat = BeautifulSoup (page.content)
bat


# In[18]:


name = []

for i in bat.find_all ("div" , class_="rankings-block__banner--name-large"):
    name.append(i.text)


for i in bat.find_all ("td" , class_="table-body__cell rankings-table__name name"):
    name.append(i.a.text)
names = name[0:10]



names


# In[28]:


teamb = []
for i in bat.find ("div" , class_="rankings-block__banner--nationality"):
        teamb.append(i.text)
team = []


for i in bat.find_all ("span" , class_="table-body__logo-text"):
    team.append(i.text)


teams = team[0:9]

teams.insert(0,teamb[4])
teams[0] = 'AUS'

teams


# In[29]:


rating = []
for i in bat.find ("div" , class_="rankings-block__banner--rating"):
    rating.append(i.text)

for i in bat.find_all ("td" , class_="table-body__cell rating"):
    rating.append(i.text)
ratings = rating[0:10]
ratings


# In[30]:


print (len(names),len(teams),len(ratings))


# In[31]:


ODIBating = pd.DataFrame ({'Name':names,'Team':teams,'Rating':ratings})
ODIBating


# In[32]:


page = requests.get ("https://www.icc-cricket.com/rankings/womens/player-rankings/odi/all-rounder")
page


# In[33]:


olr = BeautifulSoup (page.content)
olr


# In[34]:


name = []
for i in olr.find_all ("div" , class_="rankings-block__banner--name-large"):
    name.append(i.text)
for i in olr.find_all ("td" , class_="table-body__cell rankings-table__name name"):
    name.append(i.a.text)
names = name[0:10]


names


# In[36]:


teamb = []
for i in olr.find ("div" , class_="rankings-block__banner--nationality"):
        teamb.append(i.text)

team = []

for i in olr.find_all ("span" , class_="table-body__logo-text"):
    team.append(i.text)


teams = team[0:9]
teams.insert(0,teamb[4])
teams[0] = 'AUS'

teams


# In[37]:


rating = []
for i in olr.find ("div" , class_="rankings-block__banner--rating"):
    rating.append(i.text)

for i in olr.find_all ("td" , class_="table-body__cell rating"):
    rating.append(i.text)
ratings = rating[0:10]
ratings


# In[38]:


print (len(names),len(teams),len(ratings))


# In[39]:


ODIAllRounders = pd.DataFrame ({'Name':names,'Team':teams,'Rating':ratings})
ODIAllRounders


# In[ ]:




