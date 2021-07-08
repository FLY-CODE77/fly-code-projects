import os
import pandas as pd

datalist = os.listdir('./data')

# making dev frame
dev_hate = pd.read_csv("./data/" + datalist[0])
dev_title = pd.read_csv("./data/" + datalist[1], names=['title'])
dev = pd.concat([dev_title, dev_hate], 1)
