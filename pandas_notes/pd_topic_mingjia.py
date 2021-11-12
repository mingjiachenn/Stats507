
# ## Pivot Table in pandas (Mingjia Chen, mingjia@umich.edu)
# 
# - A pivot table is a table format that allows data to be dynamically arranged and summarized in categories.
# - Pivot tables are flexible, allowing you to customize your analytical calculations and making it easy for users to understand the data.
# - Use the following example to illustrate how a pivot table works.

# In[2]:

import pandas as pd
df = pd.DataFrame({"A": [1, 2, 3, 4, 5],
                   "B": [0, 1, 0, 1, 0],
                   "C": [1, 2, 2, 3, 3],
                   "D": [2, 4, 5, 5, 6],
                   "E": [2, 2, 4, 4, 6]})
print(df)


# ## Index
# 
# - The simplest pivot table must have a data frame and an index.
# - In addition, you can also have multiple indexes.
# - Try to swap the order of the two indexes, the data results are the same.

# In[3]:


tab1 = pd.pivot_table(df,index=["A"])
tab2 = pd.pivot_table(df,index=["A", "B"])
tab3 = pd.pivot_table(df,index=["B", "A"])
print(tab1)
print(tab2)
print(tab3)


# ## Values 
# - Change the values parameter can filter the data for the desired calculation.

# In[4]:


pd.pivot_table(df,index=["B", "A"], values=["C", "D"])


# ## Aggfunc
# 
# - The aggfunc parameter sets the function that we perform when aggregating data.
# - When we do not set aggfunc, it defaults aggfunc='mean' to calculate the mean value.
#   - When we also want to get the sum of the data under indexes:

# In[5]:


pd.pivot_table(df,index=["B", "A"], values=["C", "D"], aggfunc=[np.sum,np.mean])


# ## Columns
# 
# - columns like index can set the column hierarchy field, it is not a required parameter, as an optional way to split the data.
# 
# - fill_value fills empty values, margins=True for aggregation

# In[6]:


pd.pivot_table(df,index=["B"],columns=["E"], values=["C", "D"], aggfunc=[np.sum], fill_value=0, margins=1)
