"""
   Import Library 
"""
##-- Numpy
import numpy as np

"""
   Base Class 
"""
class Variable:
    def __init__(self, data):
        if data is not None:
            if np.isscalar(data):
                data = np.array(data)

        self.data = data


class Function:
    def __call__(self, input):
        x = input.data
        y = self.forward(x)
        output = Variable(y)
        
        return output

    def forward(self, x):
        raise NotImplementedError()
