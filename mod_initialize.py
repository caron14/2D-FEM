###========================================================###
###                                                        ###
###    Initialize "Connectivity" and "Nodes"               ###
###                                                        ###
###========================================================###
##-- Import library
import numpy as np

def initialize(num_ele, num_tria3_node, num_node):
    ##-- Set connectivity
    ##-- connectivity[a, b]: nodal index
    ##-- a: index of elements
    ##-- b: nodal index in elementi(meaning just order), e.g. 1->2->3
    connectivity = np.zeros([num_ele.data, num_tria3_node.data])

    connectivity[0, 0] = 0
    connectivity[0, 1] = 1
    connectivity[0, 2] = 4

    connectivity[1, 0] = 1
    connectivity[1, 1] = 2
    connectivity[1, 2] = 3

    connectivity[2, 0] = 1
    connectivity[2, 1] = 3
    connectivity[2, 2] = 4

    connectivity[3, 0] = 0
    connectivity[3, 1] = 4
    connectivity[3, 2] = 5

    ##-- Set Nodes
    x, y = np.zeros(num_node.data), np.zeros(num_node.data)

    x[0], y[0] = 0., 0.
    x[1], y[1] = 1., 0.
    x[2], y[2] = 2., 0.
    x[3], y[3] = 2., 1.
    x[4], y[4] = 1., 1.
    x[5], y[5] = 0., 1.

    return connectivity.astype(np.int64), x, y







