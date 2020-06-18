from code.DatasetLoader import DatasetLoader

data_obj = DatasetLoader()
data_obj.dataset_source_folder_path = './data/' + dataset_name + '/'
data_obj.dataset_name = dataset_name
data_obj.load()