###=========================================================###
###                                                         ###
###    Create Boundary Condition(BC)                        ###
###                                                         ###
###=========================================================###
##-- Import library
import numpy as np

##-- F: Force
##-- U: Displacement
##-- Um: boolean index, i.e., 0-->x, 1-->y
##-- Kcal: [K] designed for solving matrix
def set_BC(K, node_BC, node_F, num_node, load):
    ##-- Copy of K for post calculation
    Kcal = K.copy()

    ##-- node_BC: index of nodes, imposed of BC.
    U = np.zeros(2*num_node.data)

    Um = np.zeros(2*num_node.data, dtype="int64") + 1
    Um[node_BC] = 0
    Um = ( Um == 0 )
    #print(Um)

    ##-- node_F: index of nodes, imposed of Load
    F = np.zeros(2*num_node.data)
    F[node_F] = load.data
    #print(F)

    ##-- Prepare Matrix(K), considering BC
    for i in node_BC:
        Kcal[i, :] = 0.
        Kcal[:, i] = 0.
        Kcal[i, i] = 1.


    return F, U, Um, Kcal



