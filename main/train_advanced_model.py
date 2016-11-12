from parsing.prepare_data import data_manager
from glob import glob
from RNN import RNN
import numpy as np

vocab_size = 2575

dm = data_manager(vocab_size=vocab_size)

for i in glob("../data/*"):
    dm.add_data(i)

word_to_index, index_to_word = dm.get_indices()

model = RNN(word_to_index,index_to_word,word_dim = vocab_size,fname="models/model.data")

x_train, y_train = dm.get_training_data()
# This is with a random loss

model.train_with_sgd(x_train,y_train,nepoch=100000, learning_rate=.005)


sentence = model.create_sentence()

print(" ".join(sentence))
