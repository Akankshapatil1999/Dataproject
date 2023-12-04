#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd


# In[2]:


df=pd.read_csv("Downloads\\insurance.csv")


# In[3]:


df.head()


# In[4]:


df.isnull().sum()


# In[5]:


import plotly.express as px


# In[6]:


figure=px.histogram(df, x=df['sex'],color=df['smoker'], title='Number of smokers')


# In[7]:


figure.show()


# In[8]:


df['sex']=df['sex'].map({"female":0 , "male":1})
df['smoker']=df['smoker'].map({'no':0,'yes':1})


# In[9]:


df.head()


# In[10]:


df = df.drop(columns = ['region'] , axis = 1)


# In[11]:


df.corr()


# In[12]:


x=np.array(df[['age','sex','bmi','smoker']])
x


# In[13]:


y=np.array(df['charges'])
y


# In[14]:


from sklearn.model_selection import train_test_split


# In[15]:


x_train, x_test , y_train, y_test=train_test_split(x,y,test_size=0.2,random_state=42)


# In[16]:


x_test.shape


# In[17]:


x_train.shape


# In[18]:


from sklearn.ensemble import RandomForestRegressor


# In[21]:


rf=RandomForestRegressor()


# In[22]:


rf.fit(x_train,y_train)


# In[ ]:




