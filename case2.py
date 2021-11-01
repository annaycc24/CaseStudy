#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


df = pd.read_csv('casestudy.csv')


# In[3]:


df.head()


# In[4]:


df['customer_email'] = df['customer_email'].str.strip()


# In[5]:


# total revenue


# In[6]:


total_revenue = df.groupby(['year']).sum()['net_revenue']
total_revenue


# In[7]:


# New Customer Revenue


# In[8]:


# all the customers in 2015


# In[9]:


tmp1 = df[df['year'] == 2015]['customer_email'].unique().tolist()
tmp1


# In[10]:


# customers in 2016 but not in 2015 (New Customers)


# In[11]:


df[df['year'] == 2016]['customer_email'].isin(tmp1) == False


# In[12]:


tmp2 = df[df['year'] == 2016]['customer_email'][df[df['year'] == 2016]['customer_email'].isin(tmp1) == False]
tmp2


# In[13]:


df2 = df[df['customer_email'].isin(tmp2)]
ans = df2[df2['year'] == 2016]['net_revenue'].sum()
print('The total revenue in 2016 for new customers not present in previous year only is $', ans, '.', sep='')


# In[14]:


# all customers in 2016


# In[15]:


tmp3 = df[df['year'] == 2016]['customer_email'].unique().tolist()
tmp3


# In[16]:


# customers in 2017 but not in 2015 and 2016 (New Customers)


# In[17]:


(df[df['year'] == 2017]['customer_email'].isin(tmp3) == False) & (df[df['year'] == 2017]['customer_email'].isin(tmp1) == False)


# In[18]:


tmp4 = df[df['year'] == 2017]['customer_email'][(df[df['year'] == 2017]['customer_email'].isin(tmp3) == False) & (df[df['year'] == 2017]['customer_email'].isin(tmp1) == False)]
tmp4


# In[19]:


df3 = df[df['customer_email'].isin(tmp4)]
ans = df3[df3['year'] == 2017]['net_revenue'].sum()
print('The total revenue in 2017 for new customers not present in previous year only is $', ans, '.', sep='')


# In[20]:


# Existing Customer Growth


# In[21]:


# 2016 - 2015


# In[22]:


df[df['year'] == 2016]['customer_email'].isin(tmp1)


# In[ ]:


# Existing customers


# In[25]:


df[df['year'] == 2016]['customer_email'][df[df['year'] == 2016]['customer_email'].isin(tmp1)]


# In[39]:


df_2016 = df[df['customer_email'].isin(df[df['year'] == 2016]['customer_email'][df[df['year'] == 2016]['customer_email'].isin(tmp1)])]
ans = df_2016[df_2016['year'] == 2016]['net_revenue'].sum() - df[df['year'] == 2015]['net_revenue'].sum()
print("Existing Customer Growth in 2016 (2016 - 2015):", ans)


# In[40]:


# 2017 - 2016 - 2015


# In[48]:


(df[df['year'] == 2017]['customer_email'].isin(tmp3)) | (df[df['year'] == 2017]['customer_email'].isin(tmp1))


# In[56]:


tmp5 = df[df['year'] == 2017]['customer_email'][(df[df['year'] == 2017]['customer_email'].isin(tmp3)) | (df[df['year'] == 2017]['customer_email'].isin(tmp1))]


# In[64]:


df_2017 = df[df['customer_email'].isin(tmp5)]
ans = df_2017[df_2017['year'] == 2017]['net_revenue'].sum() - (df_2017[df_2017['year'] == 2016]['net_revenue'].sum() + df_2017[df_2017['year'] == 2015]['net_revenue'].sum())
print("Existing Customer Growth in 2017 (2017 - 2016 - 2015):", ans)


# In[65]:


# Existing Customer Revenue Current Year (2017)
df_2017[df_2017['year'] == 2017]['net_revenue'].sum()


# In[66]:


# Existing Customer Revenue Current Year (2016)
df_2016[df_2016['year'] == 2016]['net_revenue'].sum()


# In[67]:


# Existing Customer Revenue Current Year (2015)
df[df['year'] == 2015]['net_revenue'].sum()


# In[ ]:




