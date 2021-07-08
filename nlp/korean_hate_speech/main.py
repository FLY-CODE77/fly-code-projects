import os
import pandas as pd

from module import dataframe
datalist = os.listdir('./data')

# making data frame
dev = dataframe.make('./data', 'dev')
train = dataframe.make('./data', 'train')
test = dataframe.make('./data', 'test')
unlabeled = dataframe.make('./data', 'unlabeled')