from parsing.prepare_data import data_manager
from glob import glob
from RNN import RNN
import numpy as np

import json

vocab_size = 2575

dm = data_manager(vocab_size=vocab_size)

for i in glob("../data/*"):
    dm.add_data(i)

word_to_index, index_to_word = dm.get_indices()

model = RNN(word_to_index,index_to_word,word_dim = vocab_size)

model.load("models/model.data.npz")

sentence = []

all_sents = []
for i  in range(100):
    sentence = model.create_sentence()
    all_sents.append(" ".join(sentence).replace(".",".</br>").replace(",",",</br>"))

jsobj=  dict()
jsobj["text"] = " ".join(all_sents)

print(json.dumps(jsobj))

