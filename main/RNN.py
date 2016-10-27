
import numpy as np
from numpy import exp
def RNN:
    def __init__(self):
        return

    #I'm defining this instead of using numpy's implementation so that we can try different nonlinear functions more easily.
    def nonlin(x):
        #tanh(x) = (e^x - e^-x)/(e^x +e^-x)
        #np.exp = e^x
        return (exp(x) - exp(-x))/(np.exp(x) + np.exp(-x))
