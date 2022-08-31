#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd


# In[4]:


#Reading in data
data = pd.read_csv("train.csv") 
test = pd.read_csv("test.csv")
test_id = test["PassengerId"]

#Removing columns of no use
def clean_data(data):
    data = data.drop(["PassengerId","Cabin", "Name", "Ticket"], axis=1)
 
    #Filling all empty boxes w/ the median of their column
    for empty_col in ["SibSp", "Parch", "Fare", "Age"]:
        data[empty_col].fillna(data[empty_col].median(), inplace=True)
        
    #Fill empty tokens with '?'
    data.Embarked.fillna("?", inplace=True)
    return data

data = clean_data(data)
test = clean_data(test)
    
   


# In[ ]:





# In[7]:


from sklearn import preprocessing
encoder = preprocessing.LabelEncoder() #Converting string values to numbers

for column in ["Sex", "Embarked"]:
    data[column] = encoder.fit_transform(data[column])
    test[column] = encoder.transform(test[column])
    print(encoder.classes_)
    
data.head(5)
    


# In[8]:


from sklearn.linear_model import LogisticRegression 
from sklearn.model_selection import train_test_split

#Training variables to see if passenger survived
y = data["Survived"]
x = data.drop("Survived", axis=1) # Axis = 1 refers to column

x_train, x_val, y_train, y_val = train_test_split(x, y, test_size=0.2, random_state=2) #Training the model
# with a 20% of random data


# In[10]:


clf = LogisticRegression(random_state=0, max_iter=1000).fit(x_train, y_train) #Training model w/ a max of 1000 iterations


# In[11]:


predictions = clf.predict(x_val) 
from sklearn.metrics import accuracy_score

accuracy_score(y_val, predictions) #Obtaining accuracy of predictions


# In[12]:


prediction = clf.predict(test)


# In[13]:


df = pd.DataFrame({"PassendgerId":test_id.values, #Creating a dataframe w/ passenger ID, showing if they survived or not
                    "Survived":prediction})

#Code influenced by Aladdin Persson on Youtube 


# In[14]:


df.head(5)


# In[15]:


df.to_csv("results.csv", index=False)


# In[ ]:




