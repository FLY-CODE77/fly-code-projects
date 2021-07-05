import numpy as np 
import pandas as pd
import sys

import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
from tensorflow.python.util.nest import yield_flat_paths

from module.norm import normalization


dataset = pd.read_csv("./datas/dataset2.csv") 
norm = normalization(dataset)

new_model = keras.models.load_model('./datas/my_model.h5')

user_input = pd.read_csv("./datas/user.csv").loc[0,:]
user_input = (user_input.values - norm.stats["mean"][:-1].values)/norm.stats["std"][:-1] # input value 정규화
user_input = np.array(user_input, dtype=np.float32).reshape(1,5) # flatten input value

yhat = new_model.predict(user_input)

mean_price = dataset["avgPrice"][-30:].mean() 
print(mean_price)
yhat = (norm.y_backward(yhat)) # yhat value denormalization

if yhat <0 :
    print("잘못된 정보를 넣으셨습니다")
    sys.exit()
    
if yhat >0 and mean_price >= yhat:
    print("축하드려요 오늘은 파를 사셔도 됩니다! 금일의 파 예상가격은 {} 입니다.".format(yhat))

else:
    print("참으시죠.... 파 가격이 30일 평균 보다 {} 비쌉니다".format(yhat - mean_price))