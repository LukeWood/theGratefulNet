from prepare_data import data_manager
from glob import glob

dm = data_manager()

for i in glob("../data/nwa/*"):
    dm.add_data(i)

print(dm.get_training_data())
