import numpy as np

class Optimizer_AdaGrad():

    def __init__(self,learning_rate=1.,decay=0.,epsilon=1e-7):

        self.learning_rate = learning_rate
        self.current_learning_rate = learning_rate
        self.decay = decay
        self.iteration = 0
        self.epsilon = epsilon

    
    def pre_update_params(self):

        if self.decay:
            self.current_learningrate = self.learning_rate * (1./ (1+self.decay*self.iteration))
        

    def update_params(self,layer):

        if not hasattr(layer,'weight_cache'):
            layer.weight_cache = np.zeros_like(layer.weights)
            layer.bias_cache = np.zeros_like(layer.bias)
        
        # Calcula el acumulado del cache
        layer.weight_cache += layer.dweights**2
        layer.bias_cache += layer.dbias**2
        
        layer.weigths += -self.current_learningrate * layer.dweights / (np.sqrt(layer.weight_cache)) + self.epsilon
        layer.bias += -self.current_learningrate * layer.dbias / (np.sqrt(layer.bias_cache)+ self.epsilon) 

    
    def post_update_params(self):

        self.iteration += 1