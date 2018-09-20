
# coding: utf-8

# In[1]:


import numpy as np

class ModelSelection(object):
    
    def train_test_split(X,y, size=0.2): 
        """Split the values into two subsets. This method can also be used to split the trainingset into training and pruning set.
        Arguments:
            size= default values is 0.2
        Returns: 
            Two subsets for X and y.
        """
        random_selection = np.random.randint(len(y), size=int(len(y)*size))
        X_test, y_test = X[random_selection],  y[random_selection]
        X_train, y_train = np.delete(X, (random_selection), axis=0), np.delete(y, (random_selection), axis=0)
        return X_train, X_test, y_train, y_test

