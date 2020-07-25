###=========================================================###
###                                                         ###
###    Create "Element-Stiffnes Matrix(Ke)"                 ###
###                                                         ###
###=========================================================###
##-- Import library
import numpy as np
#from numpy.linalg import multi_dot
##-- Import module
from mod_base_class import Variable

##--
def make_Ke(D, B, thickness_ele, area_ele):
    ##-- Ke[a, b, c]
    ##-- a: index of elements
    ##-- b: index of nodes
    ##-- c: index of nodes

    ##-- [Ke] = (thichness of element) * [B]^T * [D]^T * [B]
    D = D.reshape(1, D.shape[0], D.shape[1])
    ##-- Data-axis transpose
    B = B.transpose( (0, 2, 1) )
    #print("B", B.shape, "D", D.shape)
    Ke = thickness_ele.data \
            *np.matmul( np.matmul(B, D), B.transpose( (0, 2, 1) ) ) \
            *area_ele.data.reshape(area_ele.data.shape[0],1,1)

    return Ke



