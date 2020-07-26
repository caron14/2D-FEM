###=========================================================###
###                                                         ###
###    Stress and Strain cal. based on FEM for 2D system    ###
###                                                         ###
###=========================================================###

##----------------------##
##    import library    ##
##----------------------##
##-- time
import time
##-- Numpy
import numpy as np
##-- Pandas
import pandas as pd

"""
    import modules
"""
from mod_base_class import Variable, Function

##-- Start time
start = time.time()

###----------------------------------------###
###    Preparation of basic information    ###
###----------------------------------------###
##-- Number of nodes
num_node = Variable(np.array(6))
##-- Number of elements
num_ele = Variable(np.array(4))
##-- Number of components for strain and stress
num_comp = Variable(np.array(3))
##-- Number of nodes for 1-st order triangle element
num_tria3_node = Variable(np.array(3))
##-- Nodal degrees of freedom
dof_node = Variable(np.array(2))
##-- Nodal degree of freedom for whole system
dof_total = Variable(np.array(dof_node.data*num_node.data))
##-- Elemental degree of freedom
dof_tria3 = Variable(np.array(dof_node.data*num_tria3_node.data))
##-- Thickness of elements
thickness_ele = Variable(np.array(1.))
##-- Young's modulus [Pa]
young = Variable(np.array(210000.))
##-- Poisson ratio
poisson = Variable(np.array(0.3))
##-- External Load
# load = [-100]
load = Variable(np.array(-100.))

###---------------------------------###
###    Set Nodes and those Order    ###
###---------------------------------###
from mod_initialize import initialize
connectivity, x, y = initialize(num_ele, num_tria3_node, num_node)
#print(connectivity.data)

###--------------------------------------###
###    Create Stress-Strain Matrix(D)    ###
###--------------------------------------###
from mod_make_D import make_D
D = make_D(num_comp, young, poisson)
#print(D.data)

###-------------------------------------###
###    Strain-Displacement Matrix(B)    ###
###-------------------------------------###
from mod_make_B import make_B
B, area_ele = make_B(x, y, connectivity, num_ele, num_comp, dof_tria3)
#print(B.data)

###--------------------------------------------###
###    Define "Element-Stiffness Matrix(Ke)    ###
###--------------------------------------------###
from mod_make_Ke import make_Ke
Ke = make_Ke(D, B, thickness_ele, area_ele)
#print(Ke.data)

###-----------------------------------------------------###
###    Define "Globally Assemled Stiffness Matrix(K)    ###
###-----------------------------------------------------###
from mod_make_K import make_K
K = make_K(num_node, num_ele, \
            dof_node, dof_total, \
            dof_tria3, connectivity, Ke)
#print(K.data)

###----------------------------------------###
###    Define Boundary Condition(BC)       ###
###----------------------------------------###
from mod_set_BC import set_BC
##-- The nodes, which are imposed of BC.
node_BC = [0, 1, 10] #-- fixed
node_F = [7] #-- loaded
F, U, Um, Kcal = set_BC(K, node_BC, node_F, num_node, load)
#print(F.data, U.data, Um.data)
#print(Kcal.data)

###-------------------------------------###
###    Solve Equation([K][U] = [F])     ###
###-------------------------------------###
from mod_solver import solver
U = solver(Kcal, F)
print("Calculated displacement of nodes is following:")
print(U)
print()
print()

###------------------------------------------------###
###    Calculate Reaction Force([RF] = [K][UF]     ###
###------------------------------------------------###
from mod_make_RF import make_RF
RF = make_RF(K, U)
#print(RF.data)

###-----------------------------------------------------------###
###    Calculate Strain in each element([Strain] = [B][U]     ###
###-----------------------------------------------------------###
from mod_make_strain_element import make_strain_element
strain_ele = make_strain_element(B, U, num_ele, dof_node, num_tria3_node, connectivity)
print("Calculated strain of element is following:")
print(strain_ele)
print()
print()

###-----------------------------------------------------------###
###    Calculate Strain in each element([Strain] = [B][U]     ###
###-----------------------------------------------------------###
from mod_make_stress_element import make_stress_element
stress_ele = make_stress_element(D, strain_ele)
print("Calculated stress of element is following:")
print(stress_ele)
print()
print()

end = time.time() - start
print("Calculation time[sec]: ", end)
