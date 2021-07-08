import os
import pandas as pd

def make(location, key_word):
    '''
    location = data path
    key_word = key_word of csv_files

    if you insert params make function
    this function make list of csv_file in data path 
    1st filter with key_word 
    2nd filter with title or not 

    finally concat title and other frame to one dataframe
    and return
    '''
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
    
