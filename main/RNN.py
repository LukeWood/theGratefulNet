
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
        s[-1] = np.zeros(self.hidden_dim)

        o = np.zeros((steps_total, self.word_dim))

        for i in np.arange(steps_total):
            #Numpy .dot is actually matrix multiplication not dot product.

            v1 = s[i-1]

            #self.W = 100x100

            v2 = self.W.dot(v1)

            v3 = self.U[:,x[i]]

            s[i] = np.tanh(v3 + v2)
            o[i] = self.softmax(self.V.dot(s[i]))

        return [o, s]

    # loss function represents total errors
    def calculate_total_loss(self, x, y):
        L = 0
        for i in np.arange(len(y)):
            o, s = self.forward_propogation(x[i])
            correct_words = o[np.arange(len(y[i])), y[i]]

            L+= -1 * np.sum(np.log(correct_words))
        return L

    def calculate_loss(self, x, y):
        N = np.sum((len(y_i) for y_i in y))
        return self.calculate_total_loss(x,y)/N

    # this just returns softmax

    def softmax(self,w, t = 1.0):
        e = np.exp(np.array(w) / t)
        dist = e / np.sum(e)
        return dist

    # Take the most likely outcome, our RNN only creates probabilities.  We simply take the best
    def predict(self, x):
        o, s = self.forward_propogation(x)
        return np.argmax(o, axis=1)

    #I'm defining this instead of using numpy's implementation so that we can try different nonlinear functions more easily.
    def nonlin(x):
        #tanh(x) = (e^x - e^-x)/(e^x +e^-x)
        #np.exp = e^x
        return (exp(x) - exp(-x))/(np.exp(x) + np.exp(-x))


    def bptt(self, x, y):
        T = len(y)

        o,s = self.forward_propogation(x)

        dLdU = np.zeros(self.U.shape)
        dLdV = np.zeros(self.V.shape)
        dLdW = np.zeros(self.W.shape)

        delta_o = o
        delta_o[np.arange(len(y)),y] -= 1

        for t in np.arange(T)[::-1]:
            dLdV = np.outer(delta_o[t], s[t].T)

            delta_t = self.V.T.dot(delta_o[t]) * (1 - (s[t] **2))

            for bptt_step in np.arange(max(0, t-self.bptt_depth),t+1)[::-1]:
                dLdW += np.outer(delta_t, s[bptt_step-1])
                dLdU[:,x[bptt_step]] += delta_t
                delta_t = self.W.T.dot(delta_t) * (1 - s[bptt_step-1] ** 2)
        return [dLdU, dLdV, dLdW]

    def train(self,x,y,iterations = 1000):
        for i in range(iterations):
            du,dv,dw = self.bptt(x,y)
            self.U += du
            self.V +=dv
            self.W+=dw
