###=========================================================###
###                                                         ###
###    Calculate Stress in elements                         ###
###                                                         ###
###    NOTE: [stress] = [D][strain]                         ###
###          stress: stress in element                      ###
###               D: stress-strain in elements matrix       ###
###          strain: strain in elements                     ###
###                                                         ###
###=========================================================###
##-- Import library
import numpy as np

def make_stress_element(D, strain_ele):
    ##-- Cal.: [stress] = [D][strain_ele]
    stress_ele = np.matmul(D, strain_ele)

    return stress_ele



