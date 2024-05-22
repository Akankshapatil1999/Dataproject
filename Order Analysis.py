#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Import Libraries

#!pip install kaggle
import kaggle


# In[2]:


#downlaod a dataset from kaggle api
get_ipython().system('kaggle datasets download ankitbansal06/retail-orders -f orders.csv')


# In[3]:


#extract file from zip file
import zipfile
zip_ref=zipfile.ZipFile('orders.csv.zip')
zip_ref.extractall() #extract file to dir
zip_ref.close() #close file


# In[4]:


#read the data and handle the null values
import pandas as pd
df = pd.read_csv('orders.csv',na_values=['Not Available','unknown'])
df['Ship Mode'].unique()


# In[5]:


#rename columns names ..make them lower case and replace space with underscore
#df.rename(columns={'Order Id':'order_id', 'City':'city'})
df.columns=df.columns.str.lower()
df.columns=df.columns.str.replace(' ','_')
df.head(5)


# In[6]:


#derive new columns discount , sale price and profit
df['discount']=df['list_price']*df['discount_percent']*.01
df['sale_price']= df['list_price']-df['discount']
df['profit']=df['sale_price']-df['cost_price']
df


# In[7]:


#convert order date from object data type to datetime
df['order_date']=pd.to_datetime(df['order_date'],format="%Y-%m-%d")
df


# In[8]:


#drop cost price list price and discount percent columns
df.drop(columns=['list_price','cost_price','discount_percent'],inplace=True)


# In[9]:


#load the data into sql server using replace option
import sqlalchemy as sal
engine = sal.create_engine('mssql://HP/master?driver=ODBC+DRIVER+17+FOR+SQL+SERVER')
conn=engine.connect()


# In[11]:


#load the data into sql server using append option
df.to_sql('df_orders', con=conn , index=False, if_exists = 'append')


# In[ ]:




