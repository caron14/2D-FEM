###=========================================================###
###                                                         ###
###    Calculate Reaction Force(RF)                         ###
###                                                         ###
###    NOTE: [RF] = [K][U]
###                                                         ###
###=========================================================###
##-- Import library
import numpy as np
#from scipy import linalg

def make_RF(K, U):

    RF = np.dot(K, U)

    return RF



