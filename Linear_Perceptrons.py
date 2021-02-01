#!/usr/bin/env python
# coding: utf-8

# In[821]:


# establishes training data and truth data
training_set = [[1,0,0],[1,0,1],[1,1,0],[1,1,1]]
truth_set = [1,1,1,-1]
# set weights
weights = [-0.4,0.4,-0.4]
# learning rate
Learn_rate = 0.01


# In[822]:


def predict(row,true,weights):
    updated_weights = [0,0,0] #updated weight values
    update_val = 0 #update value
    pred_val = 0 # predicted value for this row
    pred_total = 0 # total Dot product of the row
    for i in range(len(row)): #iterates through the selected row, calculates dot product, uses step function
        pred_total = pred_total + weights[i]*row[i] # step function
    if pred_total > 0: #checks to see if prediction total is > or <= 0
        pred_val = 1
    elif pred_total < 0 or pred_total == 0:
        pred_val = -1
    if pred_val != true: # if pred_val is not equal to the true value
        for i in range(len(row)):
            update_val = Learn_rate*((true-pred_val)*row[i]) # calculates delta
            updated_weights[i] = update_val # adds updated values to updated_weight list
            update_val = 0
    return updated_weights #returns updated values to add to weights


# In[823]:


epoch = 0
while epoch < 1:
    for row in range(len(training_set)): #iterates through each row of the training set
        grab_row = training_set[row]
        true = truth_set[row] # true value for this row
        new_weights = predict(grab_row,true,weights) #creates new weights from predict function
        new = []
        for i in range(0, len(new_weights)): #iterates through and addes updated weight values to weight values
            new.append(weights[i] + new_weights[i])
        weights = new
        print("After row one, weights",weights)

    epoch +=1
print("Number of epochs:", epoch)
print("New weights",weights)


# In[ ]:
