###=========================================================###
###                                                         ###
###    Solver Matrix(K*U = F)                               ###
###                                                         ###
###=========================================================###
##-- Import library
import numpy as np
from scipy.sparse.linalg import spsolve
from scipy.sparse import csr_matrix

def solver(Kcal, F):
    ##-- Solve by Numpy method
    #U = np.linalg.solve(Kcal, F)

    ##-- Sparse-matrix Solver by Scipy method
    U = spsolve( csr_matrix(Kcal), F, use_umfpack=True)

    return U



