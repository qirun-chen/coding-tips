import numpy as np


class MLP(object):
    def __init__(self, n_in, n_hidden, n_out, max_epochs=4000, verbose=2, learning_rate=0.03, activation='sigmoid'):
        """Initialize the MLP
        :param n_in: the number of input units
        :param n_hidden: the number of hidden units
        :param n_out: the number of output units
        :param max_epochs: the maximum epochs
        :param verbose: how much detailed the output should be
        :param learning_rate: the learning rate
        :param activation: the activation function
        """
        self.n_in = n_in
        self.n_hidden = n_hidden
        self.n_out = n_out
        self.max_epochs = max_epochs
        self.learning_rate = learning_rate

        if verbose == 0:
            self.epoch_output = 1
        elif verbose == 1:
            self.epoch_output = 10
        elif verbose == 2:
            self.epoch_output = 100
        elif verbose == 3:
            self.epoch_output = 500

        # Default activation function is logistic function
        if activation is 'sigmoid':
            self.activation = lambda a: 1. / (1. + np.exp(-a))
            # The derivative of sigmoid function
            self.derivative = lambda o: o * (1. - o)

        if activation is 'tanh':
            self.activation = lambda a: np.tanh(a)
            self.derivative = lambda o: 1. - o ** 2

        if activation is 'relu':
            self.activation = lambda a: a * (a > 0)
            self.derivative = lambda o: 1. * (o > 0)

        # Initialize the network
        # self.network = network
        self.network = self.__initialize_network()

    def __initialize_network(self):
        """I consider each unit as a dictionary, since units have many properties.
        Use one key to denote one property like weights, error signal, input, output
        :return: the initialized network - a list
        """
        network = list()
        # lower layer initialization
        # each hidden unit has a batch of weights, the last one for bias
        w_lower_layer = \
            [{'weights': [np.random.uniform(-1, 1) for _ in range(0, self.n_in+1)]} for _ in range(0, self.n_hidden)]
        network.append(w_lower_layer)
        # upper layer initialization
        w_upper_layer = \
            [{'weights': [np.random.uniform(-1, 1) for _ in range(0, self.n_hidden+1)]} for _ in range(0, self.n_out)]
        network.append(w_upper_layer)
        return network

    def __forward(self, network, inputs):
        """Forward propagation the inputs of a train example and to produce the output
        :param network: the current network list
        :param inputs: an example of training set
        :return: the output of the output layer (the upper layer)
        """
        layer_inputs = inputs
        for l_i, layer in enumerate(network):
            # use a temporary variable to receive the input,
            # since the output from the last layer is the input for the next layer
            new_layer_input = []
            for unit in layer:
                unit['input'] = self.__activate(unit['weights'], layer_inputs, l_i)
                unit['output'] = self.activation(unit['input'])
                new_layer_input.append(unit['output'])
            layer_inputs = new_layer_input
        return layer_inputs

    def __activate(self, weights, inputs, layer_index):
        """combine the weights and the inputs for each unit
        :param weights: the weight for the unit
        :param inputs: the input connecting to the unit
        :param layer_index: the layer index of the unit. To identify the first layer, need to add the bias.
        :return: the input for the activation function
        """
        activation = 0.0
        for i, w in enumerate(weights[:-1]):
            activation += w * inputs[i]
        # if layer_index is 0, then the bias with a fixed weight 1 is added to the activation
        # activation += weights[-1] * inputs[-1] if layer_index != 0 else weights[-1]
        activation += weights[-1]
        return activation

    def __backwards(self, network, y):
        """Back propagate the error signal. The error signal is stored in the dict as the key 'delta'
        :param network: the MLP network
        :param y: the expected values -- should be in one hot encoding
        """
        total_error = 0.
        for l_i in reversed(range(len(network))):
            layer = network[l_i]
            if l_i == len(network) - 1:  # the upper layer
                for index, unit in enumerate(layer):
                    unit['delta'] = (y[index] - unit['output']) * self.derivative(unit['output'])
                    total_error += unit['delta']
            else:  # the lower layer
                for index, unit in enumerate(layer):
                    delta = 0.
                    for pre_u in network[l_i + 1]:  # the previous layer for the current layer
                        delta += pre_u['weights'][index] * pre_u['delta'] * self.derivative(unit['output'])
                    unit['delta'] = delta
                    total_error += delta
        return total_error

    def __update_weights(self, network, x, alpha):
        """Update weights
        :param network: the MLP network
        :param x: the input of current example. Used to update the lower layer
        :param alpha: the learning rate. should be passed every time, since it may be changed during the training
        """
        for i_l, layer in enumerate(network):
            if i_l != 0:  # for the upper layer, the input is the output of previous layer
                inputs = [unit['output'] for unit in network[i_l - 1]]
            else:  # for the lower layer, the input is the training example
                inputs = x
            for unit in layer:
                for index, i in enumerate(inputs):
                    unit['weights'][index] += alpha * unit['delta'] * i
                unit['weights'][-1] += alpha * unit['delta']  # for the bias

    def fit(self, inputs, label):
        """Perform training
        :param training_set: the training set containing of labels
        :return: self
        """
        for e in range(self.max_epochs):
            sum_error = 0.
            for i, row in enumerate(inputs):
                output = self.__forward(self.network, row)
                y = np.zeros(self.n_out)
                if self.n_out == 1:
                    y[0] = label[0]
                else:
                    # classification => one hot encoding
                    y[int(label[i])-1] = 1
                sum_error += sum([0.5 * ((output[i] - v) ** 2) for i, v in enumerate(y)])  # square error
                self.__backwards(self.network, y)
                # sum_error += self.__backwards(self.network, y)
                self.__update_weights(self.network, row, self.learning_rate)
            if e % self.epoch_output == 0:
                print('epoch=%d, learning_rate=%.3f, error=%.3f, output=%.3f' % \
                    (e, self.learning_rate, sum_error, (output[0] if self.n_out == 1 else output.index(max(output)))))
        return self

    def predict(self, X):
        """Predict according a given input example.
        For classification, the output could be considered as the probability of being each class.
        return the index of the max values(most probable) output
        :param X: the given example
        :return: the index of max values in outputs
        """
        output = self.__forward(self.network, X)
        if self.n_out == 1:
            return output[0]
        else:
            return output.index(max(output))


