#!/usr/bin/env python
# coding: utf-8

# In[63]:


# Helping link
# https://www.datacamp.com/community/tutorials/svm-classification-scikit-learn-python
    # used tutorial code for training/test split, predictions, svm model, accuracy scores.
    # however, wrote own algorithm for dot product.

#Import scikit-learn dataset library
from sklearn import datasets
#Import svm model
from sklearn import svm
# Import train_test_split function
from sklearn.model_selection import train_test_split
#Import scikit-learn metrics module for accuracy calculation
from sklearn import metrics
# data manipulation
import pandas as pd
import math

#let me see the whole dataset when I was using Juypter Notebook
pd.set_option("display.max_rows", None, "display.max_columns", None)

#Load dataset
path = "/Users/DavidAarhus/Documents/CPSC_393/Iris.csv"
iris = pd.read_csv(path)
#drop Id number, won't need it for dot product calculation
del iris['Id']
del iris['Species']

# This forloop iterates through each row and calculates the dot product for each tuple
    # by squaring each feature and adding it to a sum which then is sqrt'd and added to the iris_dot_product list
    # which will be attached to the iris dataset, corresponding each dot_product with its correct tuple.
iris_dot_product = []
dot_sum = 0
num = 0
for i,j in iris.iterrows():
    num = j[0]
    dot_sum += num**2
    num = j[1]
    dot_sum += num**2
    num = j[2]
    dot_sum += num**2
    num = j[3]
    dot_sum += num**2
    dot_sum = math.sqrt(dot_sum)
    iris_dot_product.append(dot_sum)
#print(iris_dot_product)

# addes a new column to the dataset that lists the dot_product of
    # the "SepalLengthCm","SepalWidthCm","PetalLengthCm", and "PetalWidthCm"
    # for each tuple
iris['Dot Product'] = iris_dot_product

# changing the labels from "Iris-setosa" and "Not-Iris-setosa" to "1" and "0"
yes = 1
no = 0
for i,j in iris.iterrows():
    label = iris.at[i, "Dot Product"]
    if label < 8.0:
        iris.at[i, "Dot Product"] = "1"
    elif label > 8.0:
        iris.at[i, "Dot Product"] = "0"

# data excluding the classifying column
data = iris[["SepalLengthCm","SepalWidthCm","PetalLengthCm","PetalWidthCm"]]

# training set and test set
X_train, X_test, y_train, y_test = train_test_split(data, iris["Dot Product"], test_size=0.3,random_state=109) # 70% training and 30% test

#Create a svm Classifier
clf = svm.SVC(kernel='linear') # Linear Kernel

#Train the model using the training sets
clf.fit(X_train, y_train)

#Predict the response for test dataset
y_pred = clf.predict(X_test)

# Model Accuracy: how often is the classifier correct?
print("Accuracy:",metrics.accuracy_score(y_test, y_pred))

# Model Precision: what percentage of positive tuples are labeled as such?
print("Precision:",metrics.precision_score(y_test, y_pred))
 # Model Recall: what percentage of positive tuples are labelled as such?
print("Recall:",metrics.recall_score(y_test, y_pred))


# In[ ]:


# probably had a error in my calculation because my Precison was 1.0
    # but overall happy with what I did to classify the dataset
