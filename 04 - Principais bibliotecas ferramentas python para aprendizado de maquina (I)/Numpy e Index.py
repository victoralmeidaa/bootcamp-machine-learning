#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


# In[2]:


minha_lista = [1,2,3]


# In[3]:


minha_lista


# In[4]:


np.array(minha_lista)


# In[5]:


minha_matriz = [[1,2,3],[4,5,6],[7,8,9]]


# In[6]:


np.array(minha_matriz)


# In[8]:


np.arange(0, 10)


# In[9]:


np.zeros(3)


# In[10]:


arr = np.zeros((5, 5))


# In[11]:


arr


# In[12]:


np.ones((3, 3))


# In[13]:


np.eye(4)


# In[14]:


np.linspace(0, 10, 2)


# In[15]:


np.linspace(0, 10, 3)


# In[16]:


np.random.rand(5)


# In[17]:


np.random.randn(5)


# In[18]:


np.random.randint(0, 100, 10)


# In[19]:


np.random.rand(5) * 100


# In[20]:


np.round(np.random.rand(5) * 100, 0)


# In[21]:


arr = np.random.rand(25)


# In[22]:


arr


# In[29]:


arr = arr.reshape((5,5))


# In[30]:


arr.shape


# In[32]:


arr.max()


# In[33]:


arr.argmax()


# In[34]:


arr.argmin()


# === Index ===

# In[35]:


arr = np.arange(0, 30, 3)


# In[36]:


arr


# In[37]:


arr[3]


# In[38]:


arr[2:5]


# In[39]:


arr[:5]


# In[40]:


arr[2:]


# In[41]:


arr[2:] = 100


# In[42]:


arr


# In[46]:


arr = np.arange(50).reshape((5, 10))


# In[47]:


arr


# In[48]:


arr.shape


# In[49]:


arr[:3][:]


# In[51]:


arr2 = arr[:3]


# In[52]:


arr2[:] = 100


# In[53]:


arr


# In[54]:


arr2 = arr[:3].copy()


# In[55]:


arr2[:] = 10


# In[57]:


arr2


# In[59]:


arr[1:4, 5:]


# In[62]:


bol = arr > 50


# In[63]:


arr[bol]


# In[68]:


array = np.linspace(0, 100, 30)


# In[70]:


array.shape


# In[71]:


array = array.reshape(3, 10)


# In[72]:


array


# In[73]:


array[0:2, 2]


# In[ ]:




