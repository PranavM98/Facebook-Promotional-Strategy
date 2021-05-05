#!/usr/bin/env python
# coding: utf-8

# In[13]:


import pandas as pd
raw_data=pd.read_csv("FB_Data.csv",)
del raw_data["Unnamed: 6"]
raw_data=raw_data.dropna()
raw_data


# In[50]:


data_photo=raw_data[raw_data['Advertisement']=="Photo"]
data_video=raw_data[raw_data['Advertisement']=="Video"]
data_photo.loc[:,'Page Likes']=data_photo['Page Likes'].values - data_photo['Page Likes'].shift(periods=1, fill_value=0)
data_video.loc[:,'Page Likes']=data_video['Page Likes'].values - data_video['Page Likes'].shift(periods=1, fill_value=0)
data_photo.loc[:,'Reach']=data_photo['Reach'].values - data_photo['Reach'].shift(periods=1, fill_value=0)
data_video.loc[:,'Reach']=data_video['Reach'].values - data_video['R#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
raw_data=pd.read_csv("FB_Data (2).csv")
raw_data=raw_data.dropna()
raw_data=raw_data[raw_data["Date"]!='6-Apr']
raw_data


# In[2]:


data_photo=raw_data[raw_data['Advertisement']=="Photo"]
data_video=raw_data[raw_data['Advertisement']=="Video"]
data_photo.loc[:,'Daily Page Likes']=data_photo['Cumulative Page Likes'].values - data_photo['Cumulative Page Likes'].shift(periods=1, fill_value=0)
data_video.loc[:,'Daily Page Likes']=data_video['Cumulative Page Likes'].values - data_video['Cumulative Page Likes'].shift(periods=1, fill_value=0)
data_photo.loc[:,'Daily Reach']=data_photo['Cumulative Reach'].values - data_photo['Cumulative Reach'].shift(periods=1, fill_value=0)
data_video.loc[:,'Daily Reach']=data_video['Cumulative Reach'].values - data_video['Cumulative Reach'].shift(periods=1, fill_value=0)
data_photo.loc[:,'Daily Impressions']=data_photo['Cumulative Impressions'].values - data_photo['Cumulative Impressions'].shift(periods=1, fill_value=0)
data_video.loc[:,'Daily Impressions']=data_video['Cumulative Impressions'].values - data_video['Cumulative Impressions'].shift(periods=1, fill_value=0)
print(data_photo)
print(data_video)


# In[3]:


data=data_photo.append(data_video)
data=data.sort_values('Date',ascending=True)
data


# In[4]:


#Basic Comparison
print("Photos")
print(data[data['Advertisement']=="Photo"].mean())
print("Videos")
print(data[data['Advertisement']=="Video"].mean())


# Is the Reach Balanced?

# In[5]:


from scipy.stats import ttest_ind, ttest_ind_from_stats
print(ttest_ind(data[data['Advertisement']=="Photo"]["Daily Reach"], data[data['Advertisement']=="Video"]["Daily Reach"], equal_var=False, nan_policy
='omit'))


# In[6]:


print(ttest_ind(data[data['Advertisement']=="Photo"]["Daily Male Likes"], data[data['Advertisement']=="Video"]["Daily Male Likes"], equal_var=False, nan_policy
='omit'))


# In[7]:


print(ttest_ind(data[data['Advertisement']=="Photo"]["Daily Female Likes"], data[data['Advertisement']=="Video"]["Daily Female Likes"], equal_var=False, nan_policy
='omit'))


# The p-value <0.5. The Reach does not seem to be balanced.
# 
# ## Looking at the Difference in the Cost per Likes

# In[8]:


ttest_ind(data_photo['Cost per Result'], data_video['Cost per Result'], equal_var=False, nan_policy
='omit')


# #### Significant at level 0.05, p<0.05. The data is not balanced in terms of reach and male and female likes overall, though.

# In[9]:


data['cost_per_result']=data["Cost per Result"]
import statsmodels.formula.api as smf

smf.ols("cost_per_result ~ Advertisement", data).fit().summary()

each'].shift(periods=1, fill_value=0)
data_photo.loc[:,'Impressions']=data_photo['Impressions'].values - data_photo['Impressions'].shift(periods=1, fill_value=0)
data_video.loc[:,'Impressions']=data_video['Impressions'].values - data_video['Impressions'].shift(periods=1, fill_value=0)
print(data_photo)
print(data_video)


# In[52]:


data=data_photo.append(data_video)
data=data.sort_values('Date',ascending=True)
data


# In[54]:


#Basic Comparison
print("Photos")
print(data[data['Advertisement']=="Photo"].mean())
print("Videos")
print(data[data['Advertisement']=="Video"].mean())


# In[56]:


from scipy.stats import ttest_ind, ttest_ind_from_stats
ttest_ind(data[data['Advertisement']=="Photo"]["Page Likes"], data[data['Advertisement']=="Video"]['Page Likes'], equal_var=False, nan_policy
='omit')
#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
raw_data=pd.read_csv("FB_Data (2).csv")
raw_data=raw_data.dropna()
raw_data=raw_data[raw_data["Date"]!='6-Apr']
raw_data


# In[2]:


data_photo=raw_data[raw_data['Advertisement']=="Photo"]
data_video=raw_data[raw_data['Advertisement']=="Video"]
data_photo.loc[:,'Daily Page Likes']=data_photo['Cumulative Page Likes'].values - data_photo['Cumulative Page Likes'].shift(periods=1, fill_value=0)
data_video.loc[:,'Daily Page Likes']=data_video['Cumulative Page Likes'].values - data_video['Cumulative Page Likes'].shift(periods=1, fill_value=0)
data_photo.loc[:,'Daily Reach']=data_photo['Cumulative Reach'].values - data_photo['Cumulative Reach'].shift(periods=1, fill_value=0)
data_video.loc[:,'Daily Reach']=data_video['Cumulative Reach'].values - data_video['Cumulative Reach'].shift(periods=1, fill_value=0)
data_photo.loc[:,'Daily Impressions']=data_photo['Cumulative Impressions'].values - data_photo['Cumulative Impressions'].shift(periods=1, fill_value=0)
data_video.loc[:,'Daily Impressions']=data_video['Cumulative Impressions'].values - data_video['Cumulative Impressions'].shift(periods=1, fill_value=0)
print(data_photo)
print(data_video)


# In[3]:


data=data_photo.append(data_video)
data=data.sort_values('Date',ascending=True)
data


# In[4]:


#Basic Comparison
print("Photos")
print(data[data['Advertisement']=="Photo"].mean())
print("Videos")
print(data[data['Advertisement']=="Video"].mean())


# Is the Reach Balanced?

# In[5]:


from scipy.stats import ttest_ind, ttest_ind_from_stats
print(ttest_ind(data[data['Advertisement']=="Photo"]["Daily Reach"], data[data['Advertisement']=="Video"]["Daily Reach"], equal_var=False, nan_policy
='omit'))


# In[6]:


print(ttest_ind(data[data['Advertisement']=="Photo"]["Daily Male Likes"], data[data['Advertisement']=="Video"]["Daily Male Likes"], equal_var=False, nan_policy
='omit'))


# In[7]:


print(ttest_ind(data[data['Advertisement']=="Photo"]["Daily Female Likes"], data[data['Advertisement']=="Video"]["Daily Female Likes"], equal_var=False, nan_policy
='omit'))


# The p-value <0.5. The Reach does not seem to b#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
raw_data=pd.read_csv("FB_Data (2).csv")
raw_data=raw_data.dropna()
raw_data=raw_data[raw_data["Date"]!='6-Apr']
raw_data


# In[2]:


data_photo=raw_data[raw_data['Advertisement']=="Photo"]
data_video=raw_data[raw_data['Advertisement']=="Video"]
data_photo.loc[:,'Daily Page Likes']=data_photo['Cumulative Page Likes'].values - data_photo['Cumulative Page Likes'].shift(periods=1, fill_value=0)
data_video.loc[:,'Daily Page Likes']=data_video['Cumulative Page Likes'].values - data_video['Cumulative Page Likes'].shift(periods=1, fill_value=0)
data_photo.loc[:,'Daily Reach']=data_photo['Cumulative Reach'].values - data_photo['Cumulative Reach'].shift(periods=1, fill_value=0)
data_video.loc[:,'Daily Reach']=data_video['Cumulative Reach'].values - data_video['Cumulative Reach'].shift(periods=1, fill_value=0)
data_photo.loc[:,'Daily Impressions']=data_photo['Cumulative Impressions'].values - data_photo['Cumulative Impressions'].shift(periods=1, fill_value=0)
data_video.loc[:,'Daily Impressions']=data_video['Cumulative Impressions'].values - data_video['Cumulative Impressions'].shift(periods=1, fill_value=0)
print(data_photo)
print(data_video)


# In[3]:


data=data_photo.append(data_video)
data=data.sort_values('Date',ascending=True)
data


# In[4]:


#Basic Comparison
print("Photos")
print(data[data['Advertisement']=="Photo"].mean())
print("Videos")
print(data[data['Advertisement']=="Video"].mean())


# Is the Reach Balanced?

# In[5]:


from scipy.stats import ttest_ind, ttest_ind_from_stats
print(ttest_ind(data[data['Advertisement']=="Photo"]["Daily Reach"], data[data['Advertisement']=="Video"]["Daily Reach"], equal_var=False, nan_policy
='omit'))


# In[6]:


print(ttest_ind(data[data['Advertisement']=="Photo"]["Daily Male Likes"], data[data['Advertisement']=="Video"]["Daily Male Likes"], equal_var=False, nan_policy
='omit'))


# In[7]:


print(ttest_ind(data[data['Advertisement']=="Photo"]["Daily Female Likes"], data[data['Advertisement']=="Video"]["Daily Female Likes"], equal_var=False, nan_policy
='omit'))


# The p-value <0.5. The Reach does not seem to be balanced.
# 
# ## Looking at the Difference in the Cost per Likes

# In[8]:


ttest_ind(data_photo['Cost per Result'], data_video['Cost per Result'], equal_var=False, nan_policy
='omit')


# #### Significant at level 0.05, p<0.05. The data is not balanced in terms of reach and male and female likes overall, though.

# In[9]:


data['cost_per_result']=data["Cost per Result"]
import statsmodels.formula.api as smf

smf.ols("cost_per_result ~ Advertisement", data).fit().summary()

e balanced.
# 
# ## Looking at the Difference in the Cost per Likes

# In[8]:


ttest_ind(data_photo['Cost per Result'], data_video['Cost per Result'], equal_var=False, nan_policy
='omit')


# #### Significant at level 0.05, p<0.05. The data is not balanced in terms of reach and male and female likes overall, though.

# In[9]:


data['cost_per_result']=data["Cost per Result"]
import statsmodels.formula.api as smf

smf.ols("cost_per_result ~ Advertisement", data).fit().summary()



# #### Significant at level 0.05, p<0.05

# In[ ]:



#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
raw_data=pd.read_csv("FB_Data (2).csv")
raw_data=raw_data.dropna()
raw_data=raw_data[raw_data["Date"]!='6-Apr']
raw_data


# In[2]:


data_photo=raw_data[raw_data['Advertisement']=="Photo"]
data_video=raw_data[raw_data['Advertisement']=="Video"]
data_photo.loc[:,'Daily Page Likes']=data_photo['Cumulative Page Likes'].values - data_photo['Cumulative Page Likes'].shift(periods=1, fill_value=0)
data_video.loc[:,'Daily Page Likes']=data_video['Cumulative Page Likes'].values - data_video['Cumulative Page Likes'].shift(periods=1, fill_value=0)
data_photo.loc[:,'Daily_Reach']=data_photo['Cumulative Reach'].values - data_photo['Cumulative Reach'].shift(periods=1, fill_value=0)
data_video.loc[:,'Daily_Reach']=data_video['Cumulative Reach'].values - data_video['Cumulative Reach'].shift(periods=1, fill_value=0)
data_photo.loc[:,'Daily Impressions']=data_photo['Cumulative Impressions'].values - data_photo['Cumulative Impressions'].shift(periods=1, fill_value=0)
data_video.loc[:,'Daily Impressions']=data_video['Cumulative Impressions'].values - data_video['Cumulative Impressions'].shift(periods=1, fill_value=0)
print(data_photo)
print(data_video)


# In[3]:


data=data_photo.append(data_video)
data=data.sort_values('Date',ascending=True)
data


# In[4]:


#Basic Comparison
print("Photos")
print(data[data['Advertisement']=="Photo"].mean())
print("Videos")
print(data[data['Advertisement']=="Video"].mean())


# Is the Reach Balanced?

# In[5]:


from scipy.stats import ttest_ind, ttest_ind_from_stats
print(ttest_ind(data[data['Advertisement']=="Photo"]["Daily_Reach"], data[data['Advertisement']=="Video"]["Daily_Reach"], equal_var=False, nan_policy
='omit'))


# In[6]:


print(ttest_ind(data[data['Advertisement']=="Photo"]["Daily Male Likes"], data[data['Advertisement']=="Video"]["Daily Male Likes"], equal_var=False, nan_policy
='omit'))


# In[7]:


print(ttest_ind(data[data['Advertisement']=="Photo"]["Daily Female Likes"], data[data['Advertisement']=="Video"]["Daily Female Likes"], equal_var=False, nan_policy
='omit'))


# The p-value <0.5. The Reach does not seem to be balanced.
# 
# ## Looking at the Difference in the Cost per Likes

# In[8]:


ttest_ind(data_photo['Cost per Result'], data_video['Cost per Result'], equal_var=False, nan_policy
='omit')


# #### Significant at level 0.05, p<0.05. The data is not balanced in terms of reach and male and female likes overall, though.

# In[9]:


data['cost_per_result']=data["Cost per Result"]
import statsmodels.formula.api as smf

smf.ols("cost_per_result ~ Advertisement", data).fit().summary()


# In[10]:


smf.ols("cost_per_result ~ Advertisement + Daily_Reach", data).fit().summary()


# In[11]:


smf.ols("cost_per_result ~ Advertisement + Daily_Reach", data).fit().summary()


