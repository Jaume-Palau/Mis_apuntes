import numpy as np

class Optimizer_SDG():

    '''Modifica los pesos usando los gradientes calculados en el backward.'''

    def __init__(self, learning_rate=1.0,decay=0,momentum=0):

        # El learning rate controla cuanto cambian los pesos en cada paso
        self.learning_rate = learning_rate
        self.current_learning_rate = learning_rate
        self.decay = decay
        self.iterations = 0
        self.momentum = momentum
    def pre_update_params(self):

        if self.decay:
            self.current_learning_rate = self.learning_rate * (1./(1.+self.decay*self.iterations))

    def update_params(self,layer):

        if self.momentum:
            if not hasattr(layer,'weight_momentums'):
                layer.weight_momentums = np.zeros_like(layer.weights)
                layer.bias_momentums = np.zeros_like(layer.bias)

            weight_update = self.momentum * layer.weight_momentums - self.current_learning_rate * layer.dweights
            layer.weight_momentums = weight_update

            bias_update = self.momentum * layer.bias_momentums - self.current_learning_rate * layer.dbias
            layer.bias_momentums = bias_update
        
        else:

            weight_update = -self.current_learning_rate * layer.dweights
            bias_update = -self.current_learning_rate * layer.dbias

        layer.weights += weight_update
        layer.bias+= bias_update

    def post_update_params(self):
        self.iterations += 1
