#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
raw_data=pd.read_csv("FB_Data1.csv")
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


smf.ols("Daily_Female_CPR ~ Advertisement", data).fit().summary()


# Treatment Effect by Gender

# In[10]:


smf.ols("Daily_Male_CPR ~ Advertisement", data).fit().summary()


# ## Looking at the Likes per Reach for each ad

# In[11]:


data['adviews_per_likes']=data['Daily_Reach']/data['Daily_Likes']


# In[12]:


ttest_ind(data[data['Advertisement']=="Photo"]['adviews_per_likes'], data[data['Advertisement']=="Video"]['adviews_per_likes'], equal_var=False, nan_policy
='omit')


# In[13]:


smf.ols("adviews_per_likes ~ Advertisement", data).fit().summary()


# In[14]:


smf.ols("Cost_per_Result ~ Advertisement + adviews_per_likes", data).fit().summary()


# In[15]:


smf.ols("Daily_Male_CPR ~ Advertisement + adviews_per_likes", data).fit().summary()


# In[16]:


smf.ols("Daily_Female_CPR ~ Advertisement + adviews_per_likes", data).fit().summary()


# In[ ]:




