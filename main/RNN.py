
# Note! The basic structure of this neural network was primarily created using a tutorial found in the credits
# This is primarily a research project and I take no claim to the thought process behind the code below.
# I did change the code a lot to make it object oriented and a bit easier to follow as well as ported it to python 3

import numpy as np
import theano as theano
import theano.tensor as T
import operator
from datetime import datetime
import sys


class RNN:

    def __init__(self,word_to_index,index_to_word, word_dim,fname=None, hidden_dim=100, bptt_truncate=4):
        # Assign instance variables
        self.word_dim = word_dim
        self.hidden_dim = hidden_dim
        self.fname = fname
        self.word_to_index = word_to_index
        self.index_to_word = index_to_word
        self.bptt_truncate = bptt_truncate
        # Randomly initialize the network parameters
        U = np.random.uniform(-np.sqrt(1./word_dim), np.sqrt(1./word_dim), (hidden_dim, word_dim))
        V = np.random.uniform(-np.sqrt(1./hidden_dim), np.sqrt(1./hidden_dim), (word_dim, hidden_dim))
        W = np.random.uniform(-np.sqrt(1./hidden_dim), np.sqrt(1./hidden_dim), (hidden_dim, hidden_dim))
        # Theano: Created shared variables
        self.U = theano.shared(name='U', value=U.astype(theano.config.floatX))
        self.V = theano.shared(name='V', value=V.astype(theano.config.floatX))
        self.W = theano.shared(name='W', value=W.astype(theano.config.floatX))
        # We store the Theano graph here
        self.theano = {}
        self.__theano_build__()
        self.num_examples_seen = 0

    def __theano_build__(self):
        U, V, W = self.U, self.V, self.W
        x = T.ivector('x')
        y = T.ivector('y')
        def forward_prop_step(x_t, s_t_prev, U, V, W):
            s_t = T.tanh(U[:,x_t] + W.dot(s_t_prev))
            o_t = T.nnet.softmax(V.dot(s_t))
            return [o_t[0], s_t]
        [o,s], updates = theano.scan(
            forward_prop_step,
            sequences=x,
            outputs_info=[None, dict(initial=T.zeros(self.hidden_dim))],
            non_sequences=[U, V, W],
            truncate_gradient=self.bptt_truncate,
            strict=True)

        prediction = T.argmax(o, axis=1)
        o_error = T.sum(T.nnet.categorical_crossentropy(o, y))

        # Gradients
        dU = T.grad(o_error, U)
        dV = T.grad(o_error, V)
        dW = T.grad(o_error, W)

        # Assign functions
        self.forward_propagation = theano.function([x], o)
        self.predict = theano.function([x], prediction)
        self.ce_error = theano.function([x, y], o_error)
        self.bptt = theano.function([x, y], [dU, dV, dW])

        # SGD
        learning_rate = T.scalar('learning_rate')
        self.sgd_step = theano.function([x,y,learning_rate], [],
                      updates=[(self.U, self.U - learning_rate * dU),
                              (self.V, self.V - learning_rate * dV),
                              (self.W, self.W - learning_rate * dW)])

    def calculate_total_loss(self, X, Y):
        return np.sum([self.ce_error(x,y) for x,y in zip(X,Y)])

    def calculate_loss(self, X, Y):
        # Divide calculate_loss by the number of words
        num_words = np.sum([len(y) for y in Y])
        return self.calculate_total_loss(X,Y)/float(num_words)

    def train_with_sgd(self, X_train, y_train, learning_rate=0.005, nepoch=1, evaluate_loss_after=5):
        # We keep track of the losses so we can plot them later
        losses = []
        for epoch in range(nepoch):
            # Optionally evaluate the loss
            if (epoch % evaluate_loss_after == 0):
                loss = self.calculate_loss(X_train, y_train)
                losses.append((self.num_examples_seen, loss))
                print("Loss after %d examples: %f" % (self.num_examples_seen, loss) )
                if self.fname is not None:
                    self.save(self.fname)
                # Adjust the learning rate if loss increases
                if (len(losses) > 1 and losses[-1][1] > losses[-2][1]):
                    learning_rate = learning_rate * 0.5
                    print ("Setting learning rate to %f" % learning_rate)
                sys.stdout.flush()
            # For each training example...
            for i in range(len(y_train)):
                # One SGD step
                self.sgd_step(X_train[i], y_train[i], learning_rate)
            self.num_examples_seen += 1

    def save(self,outfile):
        U, V, W = self.U.get_value(), self.V.get_value(), self.W.get_value()
        np.savez(outfile, U=U, V=V, W=W)

    def load(self, path):
        npzfile = np.load(path)
        U, V, W = npzfile["U"], npzfile["V"], npzfile["W"]
        self.hidden_dim = U.shape[0]
        self.word_dim = U.shape[1]
        self.U.set_value(U)
        self.V.set_value(V)
        self.W.set_value(W)

    def create_sentence(self):

        unknown_token = "UNKNOWN_TOKEN"
        sentence_start_token = "SENTENCE_START"
        sentence_end_token = "SENTENCE_END"
        new_sentence = [self.word_to_index[sentence_start_token]]

        while not new_sentence[-1] == self.word_to_index[sentence_end_token]:
            next_word_probs = self.forward_propagation(new_sentence)
            sampled_word = self.word_to_index[unknown_token]

            #while sampled_word == self.word_to_index[unknown_token]:
            samples = np.random.multinomial(1, next_word_probs[-1])
            sampled_word = np.argmax(samples)
            new_sentence.append(sampled_word)
            if(len(new_sentence) > 50):
                return self.create_sentence()
        sentence_str = [self.index_to_word[x] for x in new_sentence[1:-1] if self.index_to_word[x] != sentence_start_token]
        return sentence_str

    def create_seeded_sentence(self, i_seed_sentence):
        unknown_token = "UNKNOWN_TOKEN"
        sentence_start_token = "SENTENCE_START"
        sentence_end_token = "SENTENCE_END"
        seed_sentence = [self.word_to_index[x] for x in i_seed_sentence]
        seed_sentence=[self.word_to_index[sentence_start_token]] + seed_sentence
        new_sentence = [self.word_to_index[sentence_start_token]]

        while not new_sentence[-1] == self.word_to_index[sentence_end_token]:
            next_word_probs = self.forward_propagation(seed_sentence)
            sampled_word = self.word_to_index[unknown_token]

            #while sampled_word == self.word_to_index[unknown_token]:
            samples = np.random.multinomial(1, next_word_probs[-1])
            sampled_word = np.argmax(samples)

            new_sentence.append(sampled_word)
            seed_sentence.append(sampled_word)

            if(len(new_sentence) > 50):
                return self.create_seeded_sentence(i_seed_sentence)

        sentence_str = [self.index_to_word[x] for x in new_sentence[1:-1] if self.index_to_word[x] != sentence_start_token]
        return sentence_str
