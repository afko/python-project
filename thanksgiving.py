
# coding: utf-8

# In[2]:


import pandas as pd
data = pd.read_csv("thanksgiving.csv", encoding="Latin-1")
data.head(2)


# In[3]:


data.columns


# In[4]:


data["What is typically the main dish at your Thanksgiving dinner?"].value_counts()
data[["Do you typically have gravy?"]["What is typically the main dish at your Thanksgiving dinner?" == "Tofurkey"]]


# In[5]:


apple_isnull = data["Which type of pie is typically served at your Thanksgiving dinner? Please select all that apply. - Apple"].isnull()
pumpkin_isnull = data["Which type of pie is typically served at your Thanksgiving dinner? Please select all that apply. - Pumpkin"].isnull()
pecan_isnull = data["Which type of pie is typically served at your Thanksgiving dinner? Please select all that apply. - Pecan"].isnull()

ate_pies = apple_isnull & pumpkin_isnull & pecan_isnull # Series를 & 으로 묶어서 3개 다 isnull인 애를 찾을 수 있다.

len(data[ate_pies])


# In[10]:


def age_modi(row):
    if pd.isnull(row):
        row = None
        return row
    else:
        row = row.split(" ")[0]
        row = row.replace("+", "")
        return int(row)
    

data["int_age"] = data["Age"].apply(age_modi)
data["int_age"].describe()


# Is there anything that we should be aware of about the results or our methodology?
# 
# Is this a true depiction of the ages of survey participants?

# In[11]:


def income_modi(row):
    if pd.isnull(row):
        return None
    else:
        row = row.split(" ")[0]
        if row == "Prefer":
            return None
        else:
            row = row.replace("$","")
            row = row.replace(",","")
            return int(row)

data["int_income"] = data["How much total combined money did all members of your HOUSEHOLD earn last year?"].apply(income_modi)
data["int_income"].describe()


# Is there anything that we should be aware of about the results or our methodology?
# 
# Is this a true depiction of the incomes of survey participants?

# In[12]:


under = data[data["int_income"]<150000]["How far will you travel for Thanksgiving?"]
under.value_counts()

over = data[data["int_income"]>150000]["How far will you travel for Thanksgiving?"]
over.value_counts()


# In[13]:


data.pivot_table(index="Have you ever tried to meet up with hometown friends on Thanksgiving night?", columns='Have you ever attended a "Friendsgiving?"', values = "int_age")

data.pivot_table(index="Have you ever tried to meet up with hometown friends on Thanksgiving night?", columns='Have you ever attended a "Friendsgiving?"', values = "int_income")


