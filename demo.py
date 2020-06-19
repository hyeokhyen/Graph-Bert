from code.DatasetLoader import DatasetLoader
import numpy as np
import scipy.sparse as sp

'''
To learn how data is loaded and passed to WL.
Also, how WL process the data and returns the output.
'''

if 0:
  adj = np.random.randint(2, size=(5,5))
  print (adj)
  adj = sp.coo_matrix(adj)
  print (adj)
  _adj_T = adj.T.multiply(adj.T > adj)
  _adj = adj.multiply(adj.T > adj)
  print(_adj_T.toarray())
  print (_adj.toarray())
  adj2 = adj + _adj_T - _adj
  print(adj2.toarray())
  assert False


dataset_name = 'cora'

data_obj = DatasetLoader()
data_obj.dataset_source_folder_path = './data/' + dataset_name + '/'
data_obj.dataset_name = dataset_name
data_obj.load()
