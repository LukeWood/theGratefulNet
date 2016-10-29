from parsing.prepare_data import data_manager
from glob import glob
from RNN import RNN
import numpy as np

vocab_size = 50

dm = data_manager(vocab_size=vocab_size)

for i in glob("../data/*"):
    dm.add_data(i)

word_to_index, index_to_word = dm.get_indices()

model = RNN(word_to_index,index_to_word,word_dim = vocab_size)

x_train, y_train = dm.get_training_data()
# This is with a random loss
print("Expected loss: %f" % (np.log(vocab_size)))
print("Actual loss: %f" % (model.calculate_loss(x_train[:1000],y_train[:1000])))

model.train_with_sgd(x_train,y_train,nepoch=100, learning_rate=.005)

model.save("models/model.data")

sentence = model.create_sentence()

print(" ".join(sentence))
