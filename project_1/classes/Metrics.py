
# coding: utf-8

# In[1]:


class Metrics(object):
    def accuracy(y_true, y_pred): 
        """Accuracy classification score. 
        Arguments:
            y_true: Correct labels.
            y_pred: Predicted labels. 
        Returns: 
            float value with the accuracy 
        """   
        result = 0
        for idx, y_ in enumerate(y_pred): 
            if y_ == y_true[idx]: result+=1
        return (result/len(y_true))

