import os
import pandas as pd

def make(location, key_word):
    datalist = os.listdir(location)
    csv_list = []

    for csv_name in datalist:
        if key_word in csv_name:
            csv_list.append(csv_name)

    for csv_name in csv_list:
        if 'title' in csv_name:
            title = pd.read_csv('./data/' + csv_name, names=['title'])
        else:
            hate = pd.read_csv('./data/' + csv_name)

    df = pd.concat([title, hate], 1)
    return df
    
