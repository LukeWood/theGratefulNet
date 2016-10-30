from parsing.prepare_data import data_manager
from glob import glob
from RNN import RNN
import numpy as np

vocab_size = 2575

dm = data_manager(vocab_size=vocab_size)

for i in glob("../data/*"):
    dm.add_data(i)

word_to_index, index_to_word = dm.get_indices()

model = RNN(word_to_index,index_to_word,word_dim = vocab_size)

model.load("models/model.data.npz")

sentence = []

sentence = model.create_sentence()

for i  in range(50):
    print(" ".join(sentence))
    sentence = model.create_seeded_sentence(sentence[:-1][-2:])
