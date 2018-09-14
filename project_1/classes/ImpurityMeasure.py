from math import log2

class ImpurityMeasure(object):
            
    def count_values(self,y): 
        result = {} 
        for value in y: 
            if value not in result: result[value] = 1
            else: result[value]+=1
        return result
   
    def entropy(self,y):
        result = self.count_values(y)
        e = 0
        for val in result.values(): 
            p = float(val/len(y)) 
            e = e -p*log2(p)
        return e
    
    def gini(self,y): 
        result = self.count_values(y)
        g = 1
        for val in result.values(): 
            p = float(val/len(y))
            g = g - (p)**2
        return g

        
        
        
        
        