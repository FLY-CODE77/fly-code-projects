class normalization():

    '''
    this class use for normalization, and denormalization(dataset, y_val) 
    '''
    def __init__(self, dataset):
        self.dataset = dataset
        self.stats = dataset.describe().T

    def forward(self):
        return (self.dataset - self.stats["mean"]) / self.stats["std"]
    
    def backward(self):
        return (self.dataset * self.stats["std"]) + self.stats["mean"]

    def y_backward(self, y_value):
        return (y_value * (self.stats.loc["avgPrice","std"]) )+ (self.stats.loc["avgPrice", "mean"] )

        

