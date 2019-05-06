import random

class Perceptron():
	def __init__(self, input, learning_rate=0.05):
		self.data = input
		self.learning_rate = learning_rate
		self.weights = []
		self.epoch = 1
		self.errors = 0

	def init_weights(self, value):
		#value is an array of initial values
		#for each of the 3 LPs initialize the weight vectors to 0s
		if len(self.data)==0:
			return
		for x in range(len(self.data)):
			example_weights = []
			for y in range(len(self.data[x][0])):
				example_weights = value
			self.weights.append(example_weights)

	def set_weights(self, index, output):
		#alter the weights for corresponding to the given training examples
		for w in range(len(self.weights[index])):
			delta_w = self.learning_rate * (float(self.data[index][1]) - output) * float(self.data[index][0][w])
			self.weights[index][w] = self.weights[index][w] + delta_w
		if output != self.data[index][1]:
			self.errors += 1
		self.epoch += 1

	def compute_output(self, x_vector, w_vector):
        #calculate the summation of w and x values for an example
		output = 0
		for w in range(len(w_vector)):
			output += (float(x_vector[w]) * w_vector[w])
		if output > 0:
			return 1
		else:
			return -1
