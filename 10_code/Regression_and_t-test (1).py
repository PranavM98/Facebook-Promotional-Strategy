#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
raw_data=pd.read_csv("FB_Data (3).csv")
raw_data=raw_data.dropna()
raw_data=raw_data[raw_data["Date"]!='6-Apr']
raw_data


# In[2]:


#Basic Comparison
data=raw_data
print("Photos")
print(data[data['Advertisement']=="Photo"].mean())
print("Videos")
print(data[data['Advertisement']=="Video"].mean())


# Is the Reach Balanced?

# In[3]:


from scipy.stats import ttest_ind, ttest_ind_from_stats
print(ttest_ind(data[data['Advertisement']=="Photo"]["Daily_Reach"], data[data['Advertisement']=="Video"]["Daily_Reach"], equal_var=False, nan_policy
='omit'))


# In[4]:


data['male_reach_prop']=data["Daily_Male_Reach"]/data["Daily_Reach"]
data['female_reach_prop']=data["Daily_Female_Reach"]/data["Daily_Reach"]


# In[5]:


print(ttest_ind(data[data['Advertisement']=="Photo"]["male_reach_prop"], data[data['Advertisement']=="Video"]["male_reach_prop"], equal_var=False, nan_policy
='omit'))


# In[6]:


print(ttest_ind(data[data['Advertisement']=="Photo"]["female_reach_prop"], data[data['Advertisement']=="Video"]["female_reach_prop"], equal_var=False, nan_policy
='omit'))


# The p-value <0.5. The Reach does not seem to be balanced. But, the male and female reach seems to be balanced.
# 
# ## Looking at the Difference in the Cost per Likes

# In[7]:


ttest_ind(data[data['Advertisement']=="Photo"]['Cost_per_Result'], data[data['Advertisement']=="Video"]['Cost_per_Result'], equal_var=False, nan_policy
='omit')


# #### Significant at level 0.05, p<<0.05. The data is not balanced in terms of reach and male and female likes overall, though.

# In[8]:


import statsmodels.formula.api as smf

smf.ols("Cost_per_Result ~ Advertisement", data).fit().summary()


# In[9]:


smf.ols("Cost_per_Result ~ Advertisement + Daily_Reach", data).fit().summary()


# In[10]:


smf.ols("Cost_per_Result ~ Advertisement + Daily_Male_Reach ", data).fit().summary()


# In[11]:


smf.ols("Cost_per_Result ~ Advertisement + Daily_Female_Reach ", data).fit().summary()


# ## Looking at the Likes per Reach for each ad

# In[12]:


data['likes_per_reach']=data['Daily_Likes']/data['Daily_Reach']


# In[13]:


ttest_ind(data[data['Advertisement']=="Photo"]['likes_per_reach'], data[data['Advertisement']=="Video"]['likes_per_reach'], equal_var=False, nan_policy
='omit')


# In[14]:


smf.ols("likes_per_reach ~ Advertisement", data).fit().summary()


# In[15]:


data['female_likes_per_reach']=data['Daily_Female_Likes']/data['Daily_Female_Reach']
ttest_ind(data[data['Advertisement']=="Photo"]['female_likes_per_reach'], data[data['Advertisement']=="Video"]['female_likes_per_reach'], equal_var=False, nan_policy
='omit')


# In[16]:


smf.ols("female_likes_per_reach ~ Advertisement", data).fit().summary()


# In[17]:


data['male_likes_per_reach']=data['Daily_Male_Likes']/data['Daily_Male_Reach']
ttest_ind(data[data['Advertisement']=="Photo"]['male_likes_per_reach'], data[data['Advertisement']=="Video"]['male_likes_per_reach'], equal_var=False, nan_policy
='omit')


# In[18]:


smf.ols("male_likes_per_reach ~ Advertisement", data).fit().summary()


# In[ ]:




