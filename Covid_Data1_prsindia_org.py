#!/usr/bin/env python
# coding: utf-8

# ### The core aim of this project is to retrieve COVID-19 data from a designated website, specifically focusing on important metrics such as the number of affected cases, deaths, recoveries, and active cases within each state division in India. The data extraction process will involve utilizing web scraping methodologies to collect the desired information. We will be utilizing the website 'prsindia.org' as our primary source for this data retrieval task.

# In[1]:


# Install all require library
#!pip install requests
#!pip install bs4


# In[2]:


# Import all require library like request,os,panda,csv and beautiful.
import requests
import os
import pandas as pd
import csv
from bs4 import BeautifulSoup


# In[3]:


# After import all the libraries we need to headers and save it variable.
headers={"User-Agent":"mozilla/5.0"}

# Now we need to save the url in a variable from where the data will download.
url='https://prsindia.org/covid-19/cases'

# Now use requests library to get the url with headers and convert into text and save in a variable.
rqd = requests.get(url,headers=headers).text

# Then use 'panda.read' to read the data in html.
df = pd.read_html(rqd)[0]

# Now save the data in to a variable after convert into a dataframe with the help of 'pd.DataFrame'.
cvd=pd.DataFrame(df)

# We used head() function to see the data first 10 rows.
cvd.head(10)


# In[4]:


# To check how many rows and columns we have in the data.
cvd.shape


# In[5]:


# To check the data type and some more information about data
cvd.info()


# In[6]:


# To check the null value in data. We have found the null value in '#' column and we have to take care of it. As '#' this column is no use of it so we will remove it.
cvd.isna().sum()


# In[7]:


# We need to remove the unwanted colum from the data.
cvd.drop(['#'],axis=1,inplace=True)


# In[8]:


# We hve to rename the columns name as per requirement.
cvd = cvd.rename(columns={'State/UT':'State','Confirmed Cases':'Affected','Cured/Discharged':'Survived/Recover'})


# In[9]:


# We have to remove the last row of this data which is not needed.
cvd.drop(index=cvd.index[-1],axis=0,inplace=True)


# In[10]:


# Check the first five rows of the data.
cvd.head()


# In[11]:


# Check the last five rows of the data.
cvd.tail()


# In[12]:


# Export the data and save into a csv format.
cvd.to_csv (r'C:\Users\Durga\Desktop\Newbieron Technologies\Secend_Project_Covid_Data_Web_Scrap\Data_Prsindia_Org.csv', index = False, header=True)


# # **Analysis**

# In[14]:


# We need to import matplotlib and seaborn library for vizualization the data.
#import matplotlib.pyplot as plt
#import seaborn as sns


# # *Covid Affected People Analysis of each state in India*

# In[15]:


# This is the plot size configaration.
#plt.figure(figsize=(5,10))

# Now we can use plot style but it's not mandatory.
#sns.set_style("whitegrid")

# We used seaborn to making the diagram, Y axis is define 'state' and x axis is define 'Affected' columns and mention the data.
#zx = sns.barplot(y = 'State', x = 'Affected', data = cvd)

# We created this forloop for mention the count on each bar.
#for i in zx.containers:
  #zx.bar_label(i, fmt='%.0f', label_type='edge')

#plt.xlabel("Total Affected") # This is title of x axis.
#plt.ylabel("State") # This is title of Y axis.
#plt.title("Total affected people of each state") # This is Title of Diagram.


# Here we create a diagram on the basis of affected people in covid in each state of India. And we can see the maximum people has been affected in Maharashtra and lowest people has been affected in Andaman and Nicobar islands.

# # *Covid Active Cases Analysis of each state in India*

# In[16]:


# This is the plot size configaration.
#plt.figure(figsize=(5,10))

# Now we can use plot style but it's not needed every time.
#sns.set_style("whitegrid")

# We used seaborn to making the diagram, Y axis is define 'state' and x axis is define 'Active Cases' columns and mention the data.
#zx = sns.barplot(y = 'State', x = 'Active Cases', data = cvd)

# We created this forloop for mention the count on each bar.
#for bars in zx.containers:
#  zx.bar_label(bars, fmt='%.0f', label_type='edge')

#plt.xlabel("Number of Active Cases") # This is label of x axis.
#plt.ylabel("State") # This is label of Y axis.
#plt.title("Total Active Cases of each state in India") # This is Title of Chart.


# Here we create a diagram on the basis of Active cases in covid in each state of India. And we have found the maximum active cases in Kerala and lowest active cases in Nagaland.

# # *Recovery Cases From Covid Analysis of each state in India*

# In[17]:


# This is the plot size configaration.
#plt.figure(figsize=(5,10))

# Now we can use plot style but it's optional.
#sns.set_style("whitegrid")

# We used seaborn to making the diagram, Y axis is define 'state' and x axis is define 'Survived/Recover' columns and mention the data.
#zx = sns.barplot(y = 'State', x = 'Survived/Recover', data = cvd)

# We created this forloop for mention the count on each bar.
#for bars in zx.containers:
#  zx.bar_label(bars, fmt='%.0f', label_type='edge')

#plt.xlabel("Count of Recovery") # Title of x axis.
#plt.ylabel("State") # Title of y axis.
#plt.title("Total number of Recovery case in each state") # Title of this Diagram.


# We have created a chart on the basis of recovery cases in covid in each state of India. As per charts we can see the maximum people has been recovery from covid in state of Maharastra respectively affected case and lowest people has been recovery from covid in state of Andaman and Nicobar Islands respectively affected case.
# 

# # Compare with Survived and Affected Case

# In[27]:


# We can use scatterplot for compare two numerical data.
#sns.scatterplot(x= "Survived/Recover", y= "Affected", data = cvd)

#plt.xlabel("Count of Survived/Recover cases") # Title of x axis.
#plt.ylabel("Number of Affected People") # Title of y axis.
#plt.title("Compare With Survived and Affected Case") # Title of this Diagram.


# After compare with Survived and Affected case we can see the graph is linear regression it means that maximum people has been survived from covid in each state of India. It's true many people died in covid but if you look over all graph in each state 85% people survived.

# 

# # *Covid Death Analysis of each state in India*

# In[18]:


# This is the plot size configaration.
#plt.figure(figsize=(5,12))

# Now we can use plot style but it's optional.
#sns.set_style("whitegrid")

# We used seaborn to making the diagram, Y axis is define 'state' and x axis is define 'Death' columns and mention the data.
#zx = sns.barplot(y = 'State', x = 'Death', data = cvd)

# We created this forloop for mention the count on each bar.
#for bars in zx.containers:
#  zx.bar_label(bars, fmt='%.0f', label_type='edge')

#plt.xlabel("Number of Death") # Label of X axis.
#plt.ylabel("State") # Label Of Y axis.
#plt.title("Total number of Death case in each state") # Title of the Plot.


# We have created a chart on the basis of death cases in covid of each state in India. As per charts we can see the maximum people died in covid in state of Maharastra and lowest people died in covid in state of Dadra and Nagar Haveli and Daman and Diu.
# 
