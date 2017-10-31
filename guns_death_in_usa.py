
# coding: utf-8

# In[2]:


import csv

f = open ("guns.csv", "r")
f_reader = csv.reader(f)

data = []

for row in f_reader:
    data.append(row)
    
for row in data[0:5]:
    print (row)    


# In[3]:


headers = data[0]
data = data[1:]

print (headers)
for row in data[0:5]:
    print (row)


# In[4]:


years = [row[1] for row in data]

year_counts = {}

for item in years:
    if item not in year_counts:
        year_counts[item] = 1
    elif item in year_counts:
        year_counts[item] += 1

print (year_counts)


# In[5]:


import datetime

dates = [datetime.datetime(year = int(row[1]), month = int(row[2]), day = 1)         for row in data]

print (dates[0:5])

date_counts = {}

for date in dates:
    if date not in date_counts:
        date_counts[date] = 1
    elif date in date_counts:
        date_counts[date] += 1

print(date_counts)


# In[8]:


sex_counts = {}
race_counts = {}

for row in data:
    if row[5] not in sex_counts :
        sex_counts[row[5]] = 1
    elif row[5] in sex_counts:
        sex_counts[row[5]] += 1

for row in data:
    if row[7] not in race_counts :
        race_counts[row[7]] = 1
    elif row[7] in race_counts:
        race_counts[row[7]] += 1 
        
print (sex_counts)        
print (race_counts)


# In[9]:


import csv

file = open("census.csv", "r")
file_reader = csv.reader(file)

census = []

for row in file_reader:
    census.append(row)

print(census)
    
    


# In[10]:


mapping = {"Asian/Pacific Islander": 15834141, "Black": 40250635, 
           "Native American/Native Alaskan": 3739506, "Hispanic": 44618105, 
          "White":197318956}

race_per_hundredk = {}

for item in race_counts:
    if item in mapping:
        a = (race_counts[item] / mapping[item]) * 100000 
        race_per_hundredk[item] = a
        
print(race_per_hundredk)


# In[16]:


intents = [row[3] for row in data]
races = [row[7] for row in data]

homicide_race_counts = {}
for i, race in enumerate(races):
    if intents[i] == "Homicide": 
        if race not in homicide_race_counts:
            homicide_race_counts[race] = 1
        elif race in homicide_race_counts:
            homicide_race_counts[race] += 1

homicide_race_per_hundredk = {}

for item in homicide_race_counts:
    if item in mapping:
        homicide_race_per_hundredk[item] =         (homicide_race_counts[item] / mapping[item]) * 100000
        
            
print(homicide_race_per_hundredk)

