#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import datetime as dt


# In[ ]:





# In[2]:


# 1. Create a DataFrame for the 201908-citibike-tripdata data. 

file_to_load = "201908-citibike-tripdata.csv"
nyc_citibike_df = pd.read_csv(file_to_load)
nyc_citibike_df.head(5)


# In[3]:


# 2. Check the datatypes of your columns. 
nyc_citibike_df.dtypes


# In[4]:


# Convert tripduration to datetime
nyc_citibike_df['tripduration'] = pd.to_datetime(nyc_citibike_df['tripduration'], unit="s")


# In[ ]:





# In[ ]:





# In[ ]:





# In[5]:


# 4. Check the datatypes of your columns. 
nyc_citibike_df.dtypes


# In[ ]:





# In[ ]:





# In[ ]:





# In[6]:


# 5. Export the Dataframe as a new CSV file without the index.

nyc_citibike_df.to_csv("nyc_citibike_3.csv", index = False)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




