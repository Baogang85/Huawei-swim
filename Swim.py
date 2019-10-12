#!/usr/bin/env python
# coding: utf-8

# In[9]:


import sqlite3
import pandas as pd
swim_db = sqlite3.connect(r"C:\Users\Bogdan\Desktop\wear_133.db")

def run_query(query):
    return pd.read_sql_query(query,swim_db)


# In[10]:


query = '''
SELECT id,sporttype,calories,distance,speed,pace,duration,createtime FROM m_133_SingleMovementStatistic
WHERE sporttype=6 OR sporttype=10
'''
swim_panda=run_query(query)
swim_panda.rename(columns={'sporttype':'swim type', 'calories':'calories(kcal)','distance':'distance (m)','duration':'duration (hh:mm:ss)','createtime':'start at','speed':'speed (m/s)', 'pace':'pace (s/km)'}, inplace=True)
swim_panda.head(10)





# In[22]:





# In[53]:





# In[87]:



    


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




