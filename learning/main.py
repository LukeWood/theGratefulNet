from prepare_data import data_manager

dm = data_manager()
dm.add_data("files.txt")
print(dm.get_raw_data())
