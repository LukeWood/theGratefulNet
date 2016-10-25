from prepare_data import data_manager

dm = data_manager()
dm.add_data("files.txt")
dm.remove_uncommon()
print(dm.get_training_data())
