#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


df = pd.read_csv('loans_full_schema.csv')


# In[3]:


df.head()


# ### One problem may be that the values in the column "annual_income" and "deby_to_income" are needed to be standardized to make sure they are on the same scale before building models.
# ### Second, there are some null values in some numeric columns, we can dealing with those values by replacing them with the average values.

# In[4]:


import numpy as np
import matplotlib.pyplot as plt


# ### The total balance of each state

# In[5]:


df1 = df.groupby('state').sum()['balance'].reset_index()


# In[6]:


fig = plt.figure(figsize = (20, 5))
plt.bar(df1['state'], df1['balance'], color = 'maroon')
plt.xlabel('States')
plt.ylabel('Sum of Balance')


# In[7]:


df['state'].value_counts()


# ### In the above chart, CA has the highest balance. It may be due to that most of the loans data are from CA.

# In[8]:


df['disbursement_method'].unique()


# In[9]:


df2 = df[df['disbursement_method']=='Cash'][["paid_late_fees",'disbursement_method']]
df2


# In[10]:


cnt_c = df[df['disbursement_method']=='Cash']['disbursement_method'].count()


# In[11]:


df3 = df[df['disbursement_method']=='DirectPay'][["paid_late_fees",'disbursement_method']]
df3


# In[12]:


cnt_dp = df[df['disbursement_method']=='DirectPay']['disbursement_method'].count()


# In[13]:


y = np.array([cnt_c, cnt_dp])
lb = ['Cash', 'DirectPay']


# ### Pie Chart for The "disbursement_method" Column

# In[14]:


plt.pie(y, labels = lb, autopct='%1.1f%%')


# In[15]:


fig = plt.figure(figsize = (20, 5))
plt.hist(df2['paid_late_fees'], color = 'maroon')
plt.xlabel('paid_late_fees')


# In[16]:


df2['paid_late_fees'].mean()


# In[17]:


# Remove the zeros
df2[df2['paid_late_fees'] != 0].mean()


# In[18]:


fig = plt.figure(figsize = (20, 5))
plt.hist(df3['paid_late_fees'], color = 'maroon')
plt.xlabel('paid_late_fees')


# In[19]:


df3['paid_late_fees'].mean()


# In[20]:


# Remove the zeros
df3[df3['paid_late_fees'] != 0].mean()


# ### From the charts above, we can know that most of the disbursement method is Cash, but average paid_late_fees is lower with the direct pay disbursement method. Clients tend to pay on time with the direct pay method.

# In[21]:


df['homeownership'].unique()


# In[22]:


cnt_m = df[df['homeownership'] == 'MORTGAGE']['homeownership'].count()


# In[23]:


cnt_r = df[df['homeownership'] == 'RENT']['homeownership'].count()


# In[24]:


cnt_o = df[df['homeownership'] == 'OWN']['homeownership'].count()


# In[25]:


y = np.array([cnt_m, cnt_r, cnt_o])
lb = ['Mortgage', 'Rent', 'Own']


# In[26]:


plt.pie(y, labels = lb, autopct='%1.1f%%', explode = [0.05, 0, 0]) 


# ### We can see most of the loans are related to mortgage. We can do more analysis on each part separately.

# ## We can do more analysis on some columns and display on a dashboard so that we can see all the changes together. If I have more time, I will take a look on the columns which are related to income. Those will definately be the important features that would have impact on loan data.

# ## For the feature selection, I will select all the numerical data and standardize them. Besides, for the categorical data, I will choose "homeownership", "emp_title", "verified_income", and "disbursement_method". I will encode them first before building the models.

# ## Since we are going to predict the interest rate, which is numerical, I will choose regression models and decision trees. However, I do not have enough time to complete this parts. If I have more time, I will be very interested to see the results.

# In[ ]:




