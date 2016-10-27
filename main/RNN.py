
# Note! The basic structure of this neural network was primarily created using a tutorial found in the credits
# This is primarily a research project and I take no claim to the thought process behind the code below.
# I have only (as of now) made minor changes to the code.

import numpy as np
from numpy import exp
class RNN:
    def __init__(self, word_dim=8000, hidden_dim=100, bptt_depth=4):
        self.word_dim = word_dim
        self.hidden_dim = hidden_dim
        self.bptt_depth = bptt_depth

        #Network parameters begin randomly initialized
        self.U = np.random.uniform(-np.sqrt(1./word_dim), np.sqrt(1./word_dim), (hidden_dim, word_dim))
        self.V = np.random.uniform(-np.sqrt(1./hidden_dim), np.sqrt(1./hidden_dim), (word_dim, hidden_dim))
        self.W = np.random.uniform(-np.sqrt(1./hidden_dim), np.sqrt(1./hidden_dim), (hidden_dim, hidden_dim))

    # This is just a fancy word for feeding through the network to get output
    def forward_propogation(self, x):
        steps_total = len(x)

        # We save inside of here so that we will need to recover them after we use them later
        s = np.zeros((steps_total+1,self.hidden_dim))
        s[-1] = np.zeros(self.hidden_dim))

        for i in np.arange(steps_total):
            


    #I'm defining this instead of using numpy's implementation so that we can try different nonlinear functions more easily.
    def nonlin(x):
        #tanh(x) = (e^x - e^-x)/(e^x +e^-x)
        #np.exp = e^x
        return (exp(x) - exp(-x))/(np.exp(x) + np.exp(-x))
