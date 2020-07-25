###========================================================###
###                                                        ###
###    Create "Strain-Displacement Matrix(B)"              ###
###                                                        ###
###========================================================###
##-- Import library
import numpy as np
##-- Import module
from mod_base_class import Variable

##-- For 1-st triangle elements
def make_B(x, y, connectivity, num_ele, num_comp, dof_tria3):
    ##-- Define "B matrix"
    B = np.zeros([num_ele.data, num_comp.data, dof_tria3.data])
    ##-- Define "Area of element"
    area_ele = Variable(np.array( np.zeros(num_ele.data) ))
    for i in range(num_ele.data):
        #-- Set dummy variable for triangle element
        x1, y1 = x[ connectivity[i,0] ], y[ connectivity[i,0] ]
        x2, y2 = x[ connectivity[i,1] ], y[ connectivity[i,1] ]
        x3, y3 = x[ connectivity[i,2] ], y[ connectivity[i,2] ]

        #-- Calculate the are of an element
        area_ele.data[i] = 0.5*( x1*y2 - x1*y3 + x2*y3 - x2*y1 + x3*y1 - x3*y2 )
        #-- Commonn coefficient
        coef = Variable(np.array( 0.5 / area_ele.data[i] )) #-- Ref. 1.0 / area_ele[i] / 2.0

        #-- Create B matrix
        B[i, 0, 0] = coef.data*(y2 - y3)
        B[i, 0, 1] = 0.
        B[i, 0, 2] = coef.data*(y3 - y1)
        B[i, 0, 3] = 0.
        B[i, 0, 4] = coef.data*(y1 - y2)
        B[i, 0, 5] = 0.

        B[i, 1, 0] = 0.
        B[i, 1, 1] = coef.data*(x3 - x2)
        B[i, 1, 2] = 0.
        B[i, 1, 3] = coef.data*(x1 - x3)
        B[i, 1, 4] = 0.
        B[i, 1, 5] = coef.data*(x2 - x1)

        B[i, 2, 0] = B[i, 1, 1]
        B[i, 2, 1] = B[i, 0, 0]
        B[i, 2, 2] = B[i, 1, 3]
        B[i, 2, 3] = B[i, 0, 2]
        B[i, 2, 4] = B[i, 1, 5]
        B[i, 2, 5] = B[i, 0, 4]


    return B, area_ele



