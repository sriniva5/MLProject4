import random

class Perceptron():
	def __init__(self, input, learning_rate=0.05):
		self.data = input
		self.learning_rate = learning_rate
		self.weights = []
		self.epoch = 0
		self.errors = 0

	def shuffle_data(self):
		#Return a shuffled dataset
		self.data = random.sample(self.data, len(self.data))

	def init_weights(self, value):
		#value is an array of initial values
		#for each of the 3 LPs initialize the weight vectors to 0s
		if len(self.data)==0:
			return
		for x in value:
			self.weights.append(x)

	def set_weights(self, index, output):
		#alter the weights corresponding to the given training examples
		delta_w = self.learning_rate * (float(self.data[index][1]) - output) * 1
		self.weights[0] = self.weights[0] + delta_w
		for w in range(len(self.weights)-1):
			inp = self.data[index][0]
			xi = float(inp[w])
			delta_w = self.learning_rate * (float(self.data[index][1]) - output) * xi
			self.weights[w+1] = self.weights[w+1] + delta_w
		#increment errors
		if output != self.data[index][1]:
			self.errors += 1

	def compute_output(self, x_vector, w_vector):
        #calculate the summation of w and x values for an example
		output = 0
		for w in range(len(w_vector)-1):
			output += (float(x_vector[w]) * w_vector[w+1])
		if output > 0:
			return 1
		else:
			return -1
