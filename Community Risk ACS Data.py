#!/usr/bin/env python
# coding: utf-8

# In[7]:


import requests
import json
import pandas as pd


# In[77]:


##need endpoint

response = requests.get("https://api.census.gov/data/2019/acs/acs5/profile?get=NAME,DP02_0001E,DP04_0064E&for=tract:*&for=county:033&in=state:24")
    
#"https://api.census.gov/data/2019/acs/acs5/profile?get=B24022_060E,NAME&for=county:033&in=state:24")


# In[78]:


#"311343","24","033"
print(response)


# In[116]:


data = pd.DataFrame(response.json())


# In[129]:


new_header = data.iloc[0] #grab the first row for the header
data = data[1:] #take the data less the header row
data.columns = new_header


# In[130]:


data


# In[131]:


pg = data.loc[data['county'] == '033']


# In[133]:


pg.T.reset_index()


# In[81]:


vresp = requests.get("https://api.census.gov/data/2019/acs/acs5/profile/variables")


# In[93]:


vresp = vresp.json()


# In[95]:


vresp


# In[107]:


v = pd.DataFrame(vresp)


# In[109]:


v.drop(v.head(4).index,inplace=True)


# In[111]:


v.columns = ['Variable', 'Description', 'Category']


# In[134]:


pd.set_option('display.max_colwidth', None)


# In[136]:


v


# In[ ]:




