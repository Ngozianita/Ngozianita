#!/usr/bin/env python
# coding: utf-8

# 
# 
# **Helicopter Escapes!**
# 
# Firstly , I imported a helper function

# In[9]:



from helper import *
import pandas as pd


# Get the Data
# Now, let's get the data from the List of helicopter prison escapes Wikipedia article.

# In[8]:



url = 'https://en.wikipedia.org/wiki/List_of_helicopter_prison_escapes'
data = data_from_url(url)


# printing the first three rows.

# In[37]:


for row in data[:3]:
    print(row)


# **Removing the Details**
# 
# We initialize an index variable with the value of 0. The purpose of this variable is to help us track which row we're modifying.

# In[38]:


index = 0
for row in data:
    data[index] = row[:-1]
    index += 1


# In[39]:


print(data[:3])


# **Extracting the Year**
# 
# In the code cell below, I iterate over data using the iterable variable row and: * With every occurrence of row[0], I refer to the first entry of row, i.e., the date. * Thus, with date = fetch_year(row[0]), I am extracting the year out of the date in row[0] and assiging it to the variable date. * I then replace the value of row[0] with the year that I just extracted.

# In[40]:


for row in data:
    date = fetch_year(row[0])
    row[0] = date


# In[41]:


print(data[:3])


# **Attempts per Year**

# In[42]:


min_year = min(data, key=lambda x: x[0])[0]
max_year = max(data, key=lambda x: x[0])[0]


# Before moving on, let's check what are the earliest and latest dates we have in our dataset.

# In[43]:


print(min_year)
print(max_year)


# Creating a list of all the years ranging from min_year to max_year. My goal is to then determine how many prison break attempts there were for each year. Since years in which there weren't any prison breaks aren't present in the dataset, this will make sure I capture them.

# In[44]:


years = []
for y in range(min_year, max_year + 1):
    years.append(y)


# Taking a look at years to see if it looks like I expected

# In[45]:


print(years)


# Looks good!
# 
# Now I create a list where each element looks like [, 0].

# In[46]:


attempts_per_year = []
for y in years:
    attempts_per_year.append([y, 0])


# And finally I increment the second entry (the one on index 1 which starts out as being 0) by 1 each time a year appears in the data.

# In[47]:


for row in data:
    for ya in attempts_per_year:
        y = ya[0]
        if row[0] == y:
            ya[1] += 1
            
print(attempts_per_year)    


# In[48]:


get_ipython().run_line_magic('matplotlib', 'inline')
barplot(attempts_per_year)


# The years in which the most helicopter prison break attempts occurred were 1986, 2001, 2007 and 2009, with a total of three attempts each.
# 
# **Attempts by Country**

# In[12]:




print_pretty_table


     


# In[14]:


countries_frequency = df.groupby("Country")
print_pretty_table(countries_frequency)


# By and far, the country with the most helicopter prison escape attempts is France.

# In[ ]:




