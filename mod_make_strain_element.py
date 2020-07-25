###=========================================================###
###                                                         ###
###    Calculate Strain in elements                         ###
###                                                         ###
###    NOTE: [strain] = [B][Ue]                             ###
###          strain: strain in element                      ###
###               B: strain-displacement in elements matrix ###
###              Ue: displacement in elements               ###
###                                                         ###
###=========================================================###
##-- Import library
import numpy as np

def make_strain_element(B, U, num_ele, dof_node, \
                        num_tria3_node, connectivity):
    ##-- Make Ue
    ##-- Ue: displacement in elements
    Ue = np.zeros([num_ele.data, dof_node.data*num_tria3_node.data, 1])

    for i in range(num_ele.data):
        for j in range(num_tria3_node.data):
            ##-- node index in an element
            idx_node = connectivity[i, j]
            ##-- u_x for node j
            Ue[i, 2*j, 0] = U[2*idx_node]
            ##-- u_y for node j
            Ue[i, 2*j+1, 0] = U[2*idx_node + 1]
    ##-- Cal.: [strain] = [B][Ue]
    strain_ele = np.matmul(B, Ue)

    return strain_ele



