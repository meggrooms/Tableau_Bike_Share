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


# 3. Convert the 'tripduration' column to datetime datatype.
#new_tripduration = nyc_citibike_df.tripduration
# print(new_tripduration)

#new_tripduration_datetime = pd.to_datetime(new_tripduration, unit='s')
# print(new_tripduration_datetime)

# Add a new column for the converted trip duration
nyc_citibike_df['tripduration'] = pd.to_datetime(nyc_citibike_df['tripduration'], unit="s")

# Convert the numeric gender values to string values 
#nyc_citibike_df['gender'].replace([0,1,2],['Unknown','Male','Female'],inplace=True)
#nyc_citibike_df.head()





# In[ ]:





# In[5]:


# Remove old 'tripduration' column

# nyc_citibike_df.drop(['tripduration'], axis=1).head(6)


# In[6]:


###### rearrange column


# In[7]:


# 4. Check the datatypes of your columns. 
nyc_citibike_df.dtypes


# In[ ]:





# In[ ]:





# In[8]:


##### Reorder the columns

#nyc_citibike_df2=nyc_citibike_df.reindex(columns= ['new_tripduration', 'starttime', 'start station id','start station name', 'start station latitude', 'start station longitude','end station id', 'end station name','end station latitude','end station longitude','bikeid', 'usertype','birth year', 'gender'   ])

#new_tripduration_datetime = pd.to_datetime(new_tripduration, unit='m')
#nyc_citibike_df2.head(6) 


# In[9]:


# 5. Export the Dataframe as a new CSV file without the index.

nyc_citibike_df.to_csv("nyc_citibike_3.csv", index = False)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




