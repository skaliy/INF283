from Tree import * 
from math import log2

class Decision_tree(object):
    def __init__(self):
        #super(Decision_tree, self).__init__()
            
    #TODO flytte denne ut
    def count_values(self,y): 
        result = {} 
        for value in y: 
            if value not in class_count: class_count[value] = 1
            else: class_count[value]+=1
        return result
    
      
    def entropy(self,dataset):
        result = self.count_class_objects(dataset)
        e = 0
        for class_name, class_numb in result.items(): 
            p = float(class_numb/len(dataset)) 
            e = e -p*log2(p)
        return e
    
    def learn(self,X, y, impurity_measure='entropy'):
        dummy_data = [1,2,1,2,1,2]
        
        impurity_measure_method = getattr(self, impurity_measure) #bør vi kontrollere feil? 
        result = impurity_measure_method(dummy_data)
        return result

        
        
        
        