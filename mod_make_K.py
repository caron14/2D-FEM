###=========================================================###
###                                                         ###
###    Create "Globally Assembled Stiffnes Matrix(K)"       ###
###                                                         ###
###=========================================================###
##-- Import library
import numpy as np

##--  r: index of elemental matrix
##-- rt: index of globally assembled stiffness matrix
##-- er: order of an element in the row
##-- mr: binary index, i.e., 0-->x, 1-->y
##-- nr: nodal index
def make_K(num_node, num_ele, dof_node, dof_total, dof_tria3, connectivity, Ke):
    #-- Declare "K"
    K = np.zeros([2*num_node.data, 2*num_node.data])
    #--
    for e in range(num_ele.data):
        for r in range(dof_tria3.data):
            #er = r // dof_node
            #nr = connectivity[e, er]
            #mr = r % dof_node
            #print(er, nr, mr)

            #rt = nr*dof_node + mr
            #print(rt)
            rt = connectivity[e, r // dof_node.data] * dof_node.data + (r % dof_node.data)

            for c in range(dof_tria3.data):
                ct = connectivity[e, c // dof_node.data] *dof_node.data + (c % dof_node.data)

                K[rt, ct] += Ke[e, r, c]


    return K



