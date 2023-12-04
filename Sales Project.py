#!/usr/bin/env python
# coding: utf-8

# # Total revenue for each product and overall.

# In[1]:


import numpy as np
import pandas as pd


# In[2]:


df=pd.read_csv("Downloads\\sales_data.csv")
df.head()


# In[3]:


df['total_revenue']=df["QuantitySold"]*df['Price']
df


# # total_revenue as per product

# In[4]:


df['total_rev_per']=df.groupby('ProductID')['total_revenue'].transform('sum')
print(df[['ProductID', 'total_rev_per']].drop_duplicates())


# # total_revenue_overall

# In[5]:


overall_revenue = df['total_rev_per'].sum()
print("Overall Revenue:", overall_revenue)


# # Calculate the average profit margin for each product.

# In[6]:


df['profit_margin'] = (df['Profit'] / df['total_revenue']) * 100


# In[7]:


average_profit_margin = df.groupby('ProductID')['profit_margin'].mean()
print(average_profit_margin)


# # Identify the top-selling products and categories.

# In[8]:


product_total_revenue = df.groupby('ProductID')['total_revenue'].sum()
top_selling_products = product_total_revenue.sort_values(ascending=False)
print(top_selling_products)


# In[9]:


category_total_revenue = df.groupby('Category')['total_revenue'].sum()


# In[10]:


top_selling_categories = category_total_revenue.sort_values(ascending=False).head(3) 
print(top_selling_categories)


# In[ ]:




