from parsing.prepare_data import data_manager
from glob import glob
from RNN import RNN

vocab_size = 2575

dm = data_manager(vocab_size=vocab_size)

for i in glob("../data/*"):
    dm.add_data(i)

model = RNN(word_dim = vocab_size)

o, s = model.forward_propogation(dm.get_training_data()[0])
