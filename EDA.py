#!/usr/bin/env python
# coding: utf-8

# In[74]:


import pandas as pd
import numpy as np
import seaborn as sns

df = pd.read_csv("F:/COMPANY/VYAKYA/Technical Assessment/task1/books.csv", error_bad_lines=False)

df.head()


# In[76]:


df.tail()


# In[78]:


df.shape


# In[80]:


df.describe()


# In[81]:


df.columns


# In[82]:


df.nunique()


# In[85]:


df['title'].unique()


# In[ ]:


#cleaning the dataset


# In[86]:


df.isnull().sum()


# In[ ]:


#relationship analysis


# In[87]:


corelation = df.corr()


# In[88]:


sns.heatmap(corelation, xticklabels=corelation.columns, yticklabels=corelation.columns, annot=True)


# In[89]:


sns.pairplot(df)


# In[90]:


sns.relplot(x= 'average_rating', y='ratings_count', hue='bookID', data=df)


# In[91]:


sns.distplot(df['average_rating'], bins=20)


# In[95]:


sns.catplot(x='ratings_count', kind='box', data=df)


# In[ ]:





# In[116]:


from matplotlib import pyplot as plt
sns.barplot(x="authors", y="bookID", data=df[0:5])
plt.show()


# In[127]:


sns.barplot(x="authors", y="bookID", data=df[9999:10004])
plt.show()


# In[132]:


sns.boxplot(x=df["average_rating"])


# In[143]:


df.groupby('bookID')['authors'].value_counts()


# In[ ]:




