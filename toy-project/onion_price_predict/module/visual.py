import matplotlib.pyplot as plt

def plot_history(history_data):
    
    hist = history_data
    
    plt.figure(figsize=(8,12))
    plt.subplot(2,1,1)
    plt.title("MAE plot")
    plt.xlabel('Epoch')
    plt.ylabel('Mean Abs Error [price]')
    plt.plot(hist['epoch'], hist['mae'],
            label='Train Error')
    plt.plot(hist['epoch'], hist['val_mae'],
            label = 'Test Error')

    plt.subplot(2,1,2)
    plt.title("MSE plot")
    plt.xlabel('Epoch')
    plt.ylabel('Mean Square Error [$price^2$]')
    plt.plot(hist['epoch'], hist['mse'],
            label='Train Error')
    plt.plot(hist['epoch'], hist['val_mse'],
            label = 'Test Error') 
    plt.savefig('./plt/plot_history.png')    # 이미지 저장
    plt.show()

def plot_error(test_predictions, y_test_data):

    plt.figure(figsize=(8,12))
    plt.subplot(2,1,1)
    plt.title("True vs Predictions")
    plt.scatter(y_test_data, test_predictions)
    plt.xlabel('True Values [price]')
    plt.ylabel('Predictions [price]')
    plt.axis('equal')
    plt.axis('square')

    plt.subplot(2,1,2)
    plt.title("prediction - real data")
    error = test_predictions - y_test_data
    plt.hist(error, bins = 25)
    plt.xlabel("Prediction Error [price]")
    plt.ylabel("Count")
    plt.savefig('./plt/plot_error.png')      # 이미지 저장
    plt.show()