from parsing.prepare_data import data_manager
from glob import glob
from RNN import RNN

dm = data_manager(vocab_size=2575)

for i in glob("../data/*"):
    dm.add_data(i)
