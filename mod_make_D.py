###========================================================###
###                                                        ###
###    Create Stress-Strain Matrix                         ###
###                                                        ###
###========================================================###
##-- Import library
import numpy as np
##-- Import module
from mod_base_class import Variable

##-- Plane-strain-element type
def make_D(num_comp, young, poisson):
    ##-- D[a, b]
    ##-- a: stress
    ##-- b: strain
    D = np.zeros([num_comp.data, num_comp.data])

    coef = young.data / ( (1.-2.*poisson.data)*(1.+poisson.data) )
    coef = Variable(np.array(coef))

    D[0, 0] = coef.data*(1. - poisson.data)
    D[0, 1] = coef.data*poisson.data
    D[0, 2] = 0.
    D[1, 0] = D[0, 1]
    D[1, 1] = coef.data*(1. - poisson.data)
    D[1, 2] = 0.
    D[2, 0] = D[0, 2]
    D[2, 1] = D[1, 2]
    D[2, 2] = 0.5*coef.data*(1. - 2.*poisson.data)

    return D



