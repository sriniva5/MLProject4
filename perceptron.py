import random

class Perceptron():
	def __init__(self, input, learning_rate=0.05):
		self.data = input
		self.learning_rate = learning_rate
		self.weights = []

	#def set_weights(self):
        #self.weights = weights.copy()

	def init_weights(self):
		if len(self.data)==0:
			return
		for x in range(len(self.data)):
			self.weights.append(random.uniform(-0.05,0.05))

	def compute_output(self):
        #calculate the summation of w and x values
		output = 0
		for w in range(self.weights):
			output += (self.weights[w] * self.data[w])

	def learn_perceptron(self):
		for x in range(len(self.data)):
            #compute output
			return
