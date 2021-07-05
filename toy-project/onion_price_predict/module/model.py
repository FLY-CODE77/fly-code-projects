import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers

class mlplinear():
    '''
    class for MLP-Linear
    .build() for build MLP layers
    .prediction() for prediction
    '''
    def __init__(self, dim, epochs, x_data, y_data, learning_rate=0.01, validation_split=0.2, batch_size=32):
        self.learning_rate = learning_rate
        self.dim = dim
        self.epochs = epochs
        self.batch_size = batch_size
        self.validation_split = validation_split
        self.x_data = x_data
        self.y_data = y_data

    def build(self):
        model = keras.Sequential([
        
        layers.Dense(64, activation='relu', input_shape=[self.dim]),
        layers.Dropout(0.25),
        
        layers.Dense(64, activation='relu'),
        layers.Dropout(0.25),
        
        layers.Dense(32, activation='relu'),
        layers.Dropout(0.25),
        
        layers.Dense(1)
    ])

        optimizer = tf.keras.optimizers.RMSprop(self.learning_rate)

        model.compile(loss='mse',
                        optimizer=optimizer,
                        metrics=['mae', 'mse'])
        model.summary()
        return model

    def prediction(self, model):
        
        early_stop = keras.callbacks.EarlyStopping(monitor='val_loss', patience=4999)
        history = model.fit(
        self.x_data, self.y_data, batch_size=self.batch_size,
        epochs=self.epochs, validation_split = self.validation_split, verbose=1, callbacks=[early_stop]
         )
        
        return history
    

       