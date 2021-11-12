#!/usr/bin/env python
# coding: utf-8

# In[106]:


sample_list = [(1, 3, 5), (0, 1, 2), (1, 9, 8)]
op = []
for m in range(len(sample_list)):
    li = [sample_list[m]]
    for n in range(len(sample_list)):
        if (sample_list[m][0] == sample_list[n][0] and
                sample_list[m][2] != sample_list[n][2]):
            li.append(sample_list[n])
    op.append(sorted(li, key=lambda dd: dd[2], reverse=True)[0])
res = list(set(op))


# In[107]:


print(res)


# # Question 0 - Code review warmup [10 points]

# **a. describe the task that the code accomplishes**

# The code selects tuples that the first element is unique from the sample_list.
# 
# When the first element is equal, compare the 3rd element and choose the one with larger element.

# **b. write a short code review**

# 1. It is important to keep an approperiate indent while coding, since the indent caan affect the logical relationship between different commands.
# 
# 2. The number of tuple index begins from zero, to which we should pay attention when coding.
# 
# 3. To make the snippet more efficient, we can store the index of tuples that has already occured instead of using the `set` fuction to delete duplicate.
# 
# 4. Appropriate comments should be added to make the snippet more readable. 
# 
# 5. We can use letter such as `l` to denotes the code `len(sample_list)`, so that the snippet can be more efficient.

# # Question 1 - List of Tuples [20 points]

# In[108]:


import numpy as np


# In[109]:


def lis_tup(n,k=5,low=1,high=5):
    lis = [tuple(np.random.uniform(low, high) for i in range(k)) for j in range(n)]
    return lis


# In[110]:


n=6
k=5
low=1
high=5

ast_lis=lis_tup(n,k,low,high)

# assert the type of the result is list
assert type(ast_lis)==list

# assert the list is composed by tuples
for i in range(len(ast_lis)):
    assert type(ast_lis[i])==tuple


# # Question 2 - Refactor the Snippet [40 points]

# **a. encapsulate the code snippet from the warmup into a function**

# In[111]:


def filter_tuple_a(sample_list, first_cmp, second_cmp):
    
    # make sure first_com and second_com have corresponding elements in the tuples
    assert first_cmp < len(sample_list[0])
    assert second_cmp < len(sample_list[0])
    
    op = []
    
    for m in range(len(sample_list)):
        li = [sample_list[m]]
        for n in range(len(sample_list)):
            if (sample_list[m][first_cmp] == sample_list[n][first_cmp] and
                sample_list[m][second_cmp] != sample_list[n][second_cmp]):
                li.append(sample_list[n])
                
        op.append(sorted(li, key=lambda dd: dd[second_cmp], reverse=True)[0])
        
    res = list(set(op))
    return res


# **b. write an improved version of the function**

# In[112]:


def filter_tuple_b(sample_list, first_cmp, second_cmp):
    
    # make sure first_com and second_com have corresponding elements in the tuples
    assert first_cmp < len(sample_list[0])
    assert second_cmp < len(sample_list[0])
    
    op = []
    appeared_idx = []
    l = len(sample_list)
    
    for m in range(l):
        
        # filter the tuples that have already appeared
        if m in appeared_idx:
            continue
            
        li = [sample_list[m]]
        
        for n in range(l):
            if (sample_list[m][first_cmp] == sample_list[n][first_cmp] and
                sample_list[m][second_cmp] != sample_list[n][second_cmp]):

                appeared_idx.append(n)
                li.append(sample_list[n])
                
        op.append(sorted(li, key=lambda dd: dd[second_cmp], reverse=True)[0])
        
    res = op
    return res


# **c. Write a function from scratch to accomplish the same task as the previous two parts. Your solution should traverse the input list of tuples no more than twice.**

# In[113]:


def filter_tuple_c(sample_list, first_cmp, second_cmp):
    
    # make sure first_com and second_com have corresponding elements in the tuples
    assert first_cmp < len(sample_list[0])
    assert second_cmp < len(sample_list[0])
    
    dic_tup = {}
    
    for tup in sample_list:
        dic_add = {}
        tup_add = True
        
        for key, value in dic_tup.items():
            if key[first_cmp] == tup[first_cmp] and key[second_cmp] != tup[second_cmp]:
                dic_tup[key].append(tup)
                tup_add = False
        
        if tup_add:
            dic_add[tup] = [tup]
        
        dic_tup = {**dic_add, **dic_tup}        
                
    res = set()
    for value in dic_tup.values():
        tup = sorted(value, key=lambda dd: dd[second_cmp], reverse=True)[0] 
        res.add(tup)
        
    res = list(res)
    return res


# **d. Use the function you wrote in question 1 to generate a list of tuples as input(s), run and summarize a small Monte Carlo study comparing the execution times of the three functions above (a-c).**

# In[114]:


import time
import random


# In[115]:


n = 1000
k = 100
low = 0
high = 10000

sample_list = lis_tup(n, k, low, high)

first_cmp=20
second_cmp=80

dic_time={}

start_a=time.time()
filter_tuple_a(sample_list, first_cmp, second_cmp)
end_a=time.time()
dic_time['a'] = end_a - start_a

start_b=time.time()
filter_tuple_b(sample_list, first_cmp, second_cmp)
end_b=time.time()
dic_time['b'] = end_b - start_b

start_c=time.time()
filter_tuple_c(sample_list, first_cmp, second_cmp)
end_c=time.time()
dic_time['c'] = end_c - start_c

print (dic_time)


# In[116]:


#change the value of n

k = 100
low = 0
high = 10000

for i in range(10):
    n = int(random.uniform(1000,10000))
    sample_list = lis_tup(n, k, low, high)
    first_cmp=20
    second_cmp=80
    
    dic_time={}
    start_a=time.time()
    filter_tuple_a(sample_list, first_cmp, second_cmp)
    end_a=time.time()
    dic_time['a'] = end_a - start_a

    start_b=time.time()
    filter_tuple_b(sample_list, first_cmp, second_cmp)
    end_b=time.time()
    dic_time['b'] = end_b - start_b

    start_c=time.time()
    filter_tuple_c(sample_list, first_cmp, second_cmp)
    end_c=time.time()
    dic_time['c'] = end_c - start_c

    print ('n =', n ,dic_time)


# In[117]:


#change the value of k

n=1000
low = 0
high = 10000

for i in range(10):
    k = int(random.uniform(100,1000))
    sample_list = lis_tup(n, k, low, high)
    first_cmp=20
    second_cmp=80
    
    dic_time={}
    start_a=time.time()
    filter_tuple_a(sample_list, first_cmp, second_cmp)
    end_a=time.time()
    dic_time['a'] = end_a - start_a

    start_b=time.time()
    filter_tuple_b(sample_list, first_cmp, second_cmp)
    end_b=time.time()
    dic_time['b'] = end_b - start_b

    start_c=time.time()
    filter_tuple_c(sample_list, first_cmp, second_cmp)
    end_c=time.time()
    dic_time['c'] = end_c - start_c

    print ('k =', k, dic_time)


# In[118]:


#change the value of low

n=1000
k=100
high = 10000

for i in range(10):
    low = int(random.uniform(0,1000))
    sample_list = lis_tup(n, k, low, high)
    first_cmp=20
    second_cmp=80
    
    dic_time={}
    start_a=time.time()
    filter_tuple_a(sample_list, first_cmp, second_cmp)
    end_a=time.time()
    dic_time['a'] = end_a - start_a

    start_b=time.time()
    filter_tuple_b(sample_list, first_cmp, second_cmp)
    end_b=time.time()
    dic_time['b'] = end_b - start_b

    start_c=time.time()
    filter_tuple_c(sample_list, first_cmp, second_cmp)
    end_c=time.time()
    dic_time['c'] = end_c - start_c

    print ('low =', low, dic_time)


# In[119]:


#change the value of high

n=1000
k=100
low = 0

for i in range(10):
    high = int(random.uniform(10000,100000))
    sample_list = lis_tup(n, k, low, high)
    first_cmp=20
    second_cmp=80
    
    dic_time={}
    start_a=time.time()
    filter_tuple_a(sample_list, first_cmp, second_cmp)
    end_a=time.time()
    dic_time['a'] = end_a - start_a

    start_b=time.time()
    filter_tuple_b(sample_list, first_cmp, second_cmp)
    end_b=time.time()
    dic_time['b'] = end_b - start_b

    start_c=time.time()
    filter_tuple_c(sample_list, first_cmp, second_cmp)
    end_c=time.time()
    dic_time['c'] = end_c - start_c

    print ('high =', high, dic_time)


# # Question 3 - [30 points]

# In[120]:


import pandas as pd
import pickle


# **a. read and append the demographic datasets**

# In[121]:


url1 = 'https://wwwn.cdc.gov/Nchs/Nhanes/2011-2012/DEMO_G.XPT'
url2 = 'https://wwwn.cdc.gov/Nchs/Nhanes/2013-2014/DEMO_H.XPT'
url3 = 'https://wwwn.cdc.gov/Nchs/Nhanes/2015-2016/DEMO_I.XPT'
url4 = 'https://wwwn.cdc.gov/Nchs/Nhanes/2017-2018/DEMO_J.XPT'

df11_12 = pd.read_sas(url1)
df11_12 = df11_12[['SEQN', 'RIDAGEYR', 'RIDRETH3', 'DMDEDUC2', 'DMDMARTL', 'RIDSTATR', 'SDMVPSU', 'SDMVSTRA', 'WTMEC2YR', 'WTINT2YR']]
df11_12['year'] = ['2011-2012' for i in range(len(df11_12))]

df13_14 = pd.read_sas(url2)
df13_14 = df13_14[['SEQN', 'RIDAGEYR', 'RIDRETH3', 'DMDEDUC2', 'DMDMARTL', 'RIDSTATR', 'SDMVPSU', 'SDMVSTRA', 'WTMEC2YR', 'WTINT2YR']]
df13_14['year'] = ['2013-2014' for i in range(len(df13_14))]

df15_16 = pd.read_sas(url3)
df15_16 = df15_16[['SEQN', 'RIDAGEYR', 'RIDRETH3', 'DMDEDUC2', 'DMDMARTL', 'RIDSTATR', 'SDMVPSU', 'SDMVSTRA', 'WTMEC2YR', 'WTINT2YR']]
df15_16['year'] = ['2015-2016' for i in range(len(df15_16))]

df17_18 = pd.read_sas(url4)
df17_18 = df17_18[['SEQN', 'RIDAGEYR', 'RIDRETH3', 'DMDEDUC2', 'DMDMARTL', 'RIDSTATR', 'SDMVPSU', 'SDMVSTRA', 'WTMEC2YR', 'WTINT2YR']]
df17_18['year'] = ['2017-2018' for i in range(len(df17_18))]

df = pd.concat([df11_12, df13_14, df15_16, df17_18], axis=0)

df['SEQN'] = df['SEQN'].astype('int')
df['RIDAGEYR'] = df['RIDAGEYR'].astype('int')
df['RIDRETH3'] = df['RIDRETH3'].astype('int')
df['RIDSTATR'] = df['RIDSTATR'].astype('int')

df = df.rename(columns={'SEQN': 'Respondent sequence number',
                   'RIDAGEYR': 'Age in years of the participant at the time of screening.', 
                   'RIDRETH3': 'Recode of reported race and Hispanic origin information, with Non-Hispanic Asian Category',
                   'DMDEDUC2': 'What is the highest grade or level of school {you have/SP has} completed or the highest degree {you have/s/he has} received?',
                   'DMDMARTL': 'Marital status',
                   'RIDSTATR': 'Interview and examination status of the participant.',
                   'SDMVPSU': 'Masked variance unit pseudo-PSU variable for variance estimation',
                   'SDMVSTRA': 'Masked variance unit pseudo-stratum variable for variance estimation',
                   'WTMEC2YR': 'Both interviewed and MEC examined participants.',
                   'WTINT2YR': 'Interviewed participants.'})


f = open('NHANS.pkl', 'wb')

pickle.dump(df, f, -1)


# In[122]:


print(df)


# **b. read and append the oral health and dentition dataset**

# In[123]:


url5 = 'https://wwwn.cdc.gov/Nchs/Nhanes/2011-2012/OHXDEN_G.XPT'
url6 = 'https://wwwn.cdc.gov/Nchs/Nhanes/2013-2014/OHXDEN_H.XPT'
url7 = 'https://wwwn.cdc.gov/Nchs/Nhanes/2015-2016/OHXDEN_I.XPT'
url8 = 'https://wwwn.cdc.gov/Nchs/Nhanes/2017-2018/OHXDEN_J.XPT'

required_columns = ['SEQN', 'OHDDESTS']

df17_18_od = pd.read_sas(url8)
for col in df17_18_od.columns:
    if col.startswith('OHX'):
        if (col.lstrip('OHX').rstrip('TC')).isdigit():
            required_columns.append(col)
        elif (col.lstrip('OHX').rstrip('CTC')).isdigit():
            required_columns.append(col)
df17_18_od = df17_18_od[required_columns]
df17_18_od['year'] = ['2017-2018' for i in range(len(df17_18_od))]

df11_12_od = pd.read_sas(url5)
df11_12_od = df11_12_od[required_columns]
df11_12_od['year'] = ['2011-2012' for i in range(len(df11_12_od))]


df13_14_od = pd.read_sas(url6)
df13_14_od = df13_14_od[required_columns]
df13_14_od['year'] = ['2013-2014' for i in range(len(df13_14_od))]


df15_16_od = pd.read_sas(url7)
df15_16_od = df15_16_od[required_columns]
df15_16_od['year'] = ['2015-2016' for i in range(len(df15_16_od))]

df_od = pd.concat([df11_12_od, df13_14_od, df15_16_od, df17_18_od], axis=0, sort=False)

df_od['SEQN'] = df_od['SEQN'].astype('int')
df_od['OHDDESTS'] = df_od['OHDDESTS'].astype('int')

df_od = df_od.rename(columns={'SEQN': 'Respondent sequence number',
                        'OHDDESTS': 'Dentition Status Code'})

f = open('OHXDEN.pkl', 'wb')

pickle.dump(df_od, f, -1)


# In[124]:


print(df_od)


# **c. report the number of cases**

# In[125]:


df.shape[0], df_od.shape[0]


# In[ ]:




