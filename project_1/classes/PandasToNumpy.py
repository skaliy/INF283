
# coding: utf-8

# In[ ]:


import pandas as pd 

class PandasToNumpy(object):

    def dataframe_to_numpy(X,y): 
        """Converts the values in the columns in a dataframe to a numpy array with unique int values 
        and returns the new list of X and y."""
        for column in X.columns: 
            X[column] = pd.factorize(X[column])[0]
        X = X.values #numpy array 
        y = pd.factorize(y)[0]
        return X,y

