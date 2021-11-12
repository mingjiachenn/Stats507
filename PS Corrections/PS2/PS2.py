# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:light
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.13.1
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# ## GSI comments
#
# Overall: -2 for imports not collected at top.
#
# -4 for missing docstring in all functions. 
#
# -2 if inconsistent spacing around assignment =. 
#
# Q1: -5 for incorrect output. (uniform would not return integer but float) 
#
# Q2: -6 for incorrect MC study and no formatted table or description. 
#
# Q3: -1 for long variable name.

# ## Imports

# **Corrections for PS6 Q3**
#
# -2 for imports not collected at top.

import numpy as np
import random
import pandas as pd
import pickle
from timeit import Timer
from collections import defaultdict

# # Question 0 - Code review warmup [10 points]

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

print(res)


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

# **Corrections for PS6 Q3**
#
# -4 for missing docstring in all functions.
#
# Q1: -5 for incorrect output. (uniform would not return integer but float)

def lis_tup(n, k=5, low=1, high=5):
    """
    Generate a random list of n k-tuples containing integers ranging from low to high.

    Parameters
    ----------
    n : integer
        The number of tuples in the list.
    k: integer, optional
        The length of the tuples created. The default is 5.
    low : integer, optional
        The low end of the range to generate integers from. The default is 1.
    high : integer, optional
        The high end of hte range to generate integers from. The default is 5.
    
    Returns
    -------
    A list of length `n` with tuples of size `tup_size` consting of uniform
    random integers in [low, high).
    """
    lis = [tuple(np.random.randint(low, high) for i in range(k)) for j in range(n)]
    return lis



# **Corrections for PS6 Q3**
#
# -2 if inconsistent spacing around assignment =.

# +
n = 6
k = 5
low = 1
high = 5

ast_lis = lis_tup(n, k, low, high)

# assert the type of the result is list
assert type(ast_lis) == list

# assert the list is composed by tuples
for i in range(len(ast_lis)):
    assert type(ast_lis[i]) == tuple


# -

# # Question 2 - Refactor the Snippet [40 points]

# **a. encapsulate the code snippet from the warmup into a function**

# **Corrections for PS6 Q3**
#
# -4 for missing docstring in all functions.

def filter_tuple_a(sample_list, first_cmp=0, second_cmp=2):
    
    """
    Find tuples with maximum value in one position by unique value in another.
    
    ----------
    sample_list : list of tuples
        The list of tuples to organize as described above.
    first_cmp : int
        The position to determine whether the element is unique. The default is 0.
    second_cmp : int
        The position to compare when the element in the first position is not unique. 
        The default is 2.

    Returns
    -------
    A list of all tuples, in which the element on the first position is unique. 
    When it is not equal, chose the tuple with the largest element on the second position. 
    """
    
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

# **Corrections for PS6 Q3**
#
# -4 for missing docstring in all functions.

def filter_tuple_b(sample_list, first_cmp=0, second_cmp=2):
    
    """
    Find tuples with maximum value in one position by unique value in another.
    
    ----------
    sample_list : list of tuples
        The list of tuples to organize as described above.
    first_cmp : int
        The position to determine whether the element is unique. The default is 0.
    second_cmp : int
        The position to compare when the element in the first position is not unique.
        The default is 2.

    Returns
    -------
    A list of all tuples, in which the element on the first position is unique. 
    When it is not equal, chose the tuple with the largest element on the second position. 
    """
    
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

# **Corrections for PS6 Q3**
#
# **-4 for missing docstring in all functions.**

def filter_tuple_c(sample_list, first_cmp=0, second_cmp=2):
    
    """
    Find tuples with maximum value in one position by unique value in another.
    
    ----------
    sample_list : list of tuples
        The list of tuples to organize as described above.
    first_cmp : int
        The position to determine whether the element is unique. The default is 0.
    second_cmp : int
        The position to compare when the element in the first position is not unique.
        The default is 2.

    Returns
    -------
    A list of all tuples, in which the element on the first position is unique. 
    When it is not equal, chose the tuple with the largest element on the second position. 
    """
    
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

# **Corrections for PS6 Q3**
#
# -2 if inconsistent spacing around assignment =.
#
# Q2: -6 for incorrect MC study and no formatted table or description.

# +
sample_list = lis_tup(n=1000, k=5, low=0, high=1000)

time = defaultdict(list)

for f in [filter_tuple_a, filter_tuple_b, filter_tuple_c]:
    t = Timer('f(n)', globals={'f': f, 'n': sample_list})
    tm = t.repeat(repeat=100, number=1)
    time["Function"].append(f.__name__)
    time["mean time"].append(np.mean(tm))
    
tab1 = pd.DataFrame(time)

print(tab1)
# -

# The execution times of the `filter_tuple_a`, `filter_tuple_b` and `filter_tuple_c` functions decrease one by one.
# To be more specific, the execution time of `filter_tuple_c` is only $\frac{1}{3}$ of that of `filter_tuple_a`.

# # Question 3 - [30 points]

# **a. read and append the demographic datasets**

# **Corrections for PS6 Q3**
#
# Q3: -1 for long variable name.

# +
url1 = 'https://wwwn.cdc.gov/Nchs/Nhanes/2011-2012/DEMO_G.XPT'
url2 = 'https://wwwn.cdc.gov/Nchs/Nhanes/2013-2014/DEMO_H.XPT'
url3 = 'https://wwwn.cdc.gov/Nchs/Nhanes/2015-2016/DEMO_I.XPT'
url4 = 'https://wwwn.cdc.gov/Nchs/Nhanes/2017-2018/DEMO_J.XPT'

df11_12 = pd.read_sas(url1)
df11_12 = df11_12[['SEQN', 'RIDAGEYR', 'RIDRETH3', 'DMDEDUC2', 'DMDMARTL', 
                   'RIDSTATR', 'SDMVPSU', 'SDMVSTRA', 'WTMEC2YR', 'WTINT2YR']]
df11_12['year'] = ['2011-2012' for i in range(len(df11_12))]

df13_14 = pd.read_sas(url2)
df13_14 = df13_14[['SEQN', 'RIDAGEYR', 'RIDRETH3', 'DMDEDUC2', 'DMDMARTL', 
                   'RIDSTATR', 'SDMVPSU', 'SDMVSTRA', 'WTMEC2YR', 'WTINT2YR']]
df13_14['year'] = ['2013-2014' for i in range(len(df13_14))]

df15_16 = pd.read_sas(url3)
df15_16 = df15_16[['SEQN', 'RIDAGEYR', 'RIDRETH3', 'DMDEDUC2', 'DMDMARTL', 
                   'RIDSTATR', 'SDMVPSU', 'SDMVSTRA', 'WTMEC2YR', 'WTINT2YR']]
df15_16['year'] = ['2015-2016' for i in range(len(df15_16))]

df17_18 = pd.read_sas(url4)
df17_18 = df17_18[['SEQN', 'RIDAGEYR', 'RIDRETH3', 'DMDEDUC2', 'DMDMARTL', 
                   'RIDSTATR', 'SDMVPSU', 'SDMVSTRA', 'WTMEC2YR', 'WTINT2YR']]
df17_18['year'] = ['2017-2018' for i in range(len(df17_18))]

df = pd.concat([df11_12, df13_14, df15_16, df17_18], axis=0)

df['SEQN'] = df['SEQN'].astype('int')
df['RIDAGEYR'] = df['RIDAGEYR'].astype('int')
df['RIDRETH3'] = df['RIDRETH3'].astype('int')
df['RIDSTATR'] = df['RIDSTATR'].astype('int')

df = df.rename(columns = {'SEQN': 'sequence number',
                         'RIDAGEYR': 'Age', 
                         'RIDRETH3': 'Race',
                         'DMDEDUC2': 'Education level',
                         'DMDMARTL': 'Marital status',
                         'RIDSTATR': 'examination status',
                         'SDMVPSU': 'pseudo-PSU variable',
                         'SDMVSTRA': 'pseudo-stratum variable',
                         'WTMEC2YR': 'Interviewed and MEC examined participants.',
                         'WTINT2YR': 'Interviewed participants.'})


f = open('NHANS.pkl', 'wb')

pickle.dump(df, f, -1)
# -

print(df)

# **b. read and append the oral health and dentition dataset**

# **Corrections for PS6 Q3**
#
# Q3: -1 for long variable name.

# +
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

df_od = df_od.rename(columns = {'SEQN': 'Sequence number',
                                'OHDDESTS': 'Dentition Status'})

f = open('OHXDEN.pkl', 'wb')

pickle.dump(df_od, f, -1)
# -

print(df_od)

# **c. report the number of cases**

df.shape[0], df_od.shape[0]


