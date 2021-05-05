import pandas as pd
import numpy as np
from scipy import stats

import matplotlib.pyplot as plt
import seaborn as sns


fb = pd.read_csv("../00_Data/FB_Data.csv")

# select valid rows
fb.fillna(0, inplace = True)
fb = fb[fb["Cumulative Reach"] > 1]

fb["DailyReach"] = fb["Daily Male Reach"] + fb["Daily Female Reach"]
fb["ConvertRate"] = fb["Daily Likes"] / fb["DailyReach"]
fb["ConvertRate Male"] = fb["Daily Male Likes"] / fb["Daily Male Reach"]
fb["ConvertRate Female"] = fb["Daily Female Likes"] / fb["Daily Female Reach"]
fb.head()


df_photo = fb[fb.Advertisement == "Photo"]
df_video = fb[fb.Advertisement == "Video"]


#=======================================
# Cost per Result
#=======================================
plt.figure(figsize=(8, 6))

sns.barplot(x="Date", y="Cost per Result", hue="Advertisement", data=fb)
plt.title("DailyReach")
stats.ttest_rel(df_photo["Cost per Result"], df_video["Cost per Result"])




#=======================================
# Convert Rate
#=======================================

sns.barplot(x="Date", y="ConvertRate", hue="Advertisement", data=fb)
plt.title("Convert Rate")
stats.ttest_rel(df_photo["ConvertRate"], df_video["ConvertRate"])


sns.barplot(x="Date", y="ConvertRate Male", hue="Advertisement", data=fb)
plt.title("Convert Rate --- Male")
stats.ttest_rel(df_photo["ConvertRate Male"], df_video["ConvertRate Male"])

sns.barplot(x="Date", y="ConvertRate Female", hue="Advertisement", data=fb)
plt.title("Convert Rate --- Female")
stats.ttest_rel(df_photo["ConvertRate Female"], df_video["ConvertRate Female"])

#=======================================
# Daily Like
#=======================================
sns.barplot(x="Date", y="Daily Likes", hue="Advertisement", data=fb)
plt.title("DailyReach")
stats.ttest_rel(df_photo["Daily Likes"], df_video["Daily Likes"])

sns.barplot(x="Date", y="Daily Male Likes", hue="Advertisement", data=fb)
plt.title("DailyReach")
stats.ttest_rel(df_photo["Daily Male Likes"], df_video["Daily Male Likes"])

sns.barplot(x="Date", y="Daily Female Likes", hue="Advertisement", data=fb)
plt.title("DailyReach")
stats.ttest_rel(df_photo["Daily Female Likes"], df_video["Daily Female Likes"])


#=======================================
# Daily Reach
#=======================================

sns.barplot(x="Date", y="DailyReach", hue="Advertisement", data=fb)
plt.title("DailyReach")
stats.ttest_rel(df_photo["DailyReach"], df_video["DailyReach"])

sns.barplot(x="Date", y="Daily Male Reach", hue="Advertisement", data=fb)
plt.title("Convert Rate --- Male")
stats.ttest_rel(df_photo["Daily Male Reach"], df_video["Daily Male Reach"])

sns.barplot(x="Date", y="Daily Female Reach", hue="Advertisement", data=fb)
plt.title("Convert Rate --- Female")
stats.ttest_rel(df_photo["Daily Female Reach"], df_video["Daily Female Reach"])




























