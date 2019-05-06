import random
class Perceptron():
	def __init__(self):
		self.data = "NULL"
		self.children = []
		self.parent = []
		self.child_weights = []
	def printNice(self, level=0):
		print("\t"*level+self.data)
		for child in self.children:
			child.printNice(level+1)
	def calc_output(self):
		output = 0
		for i, x in enumerate(self.children):
			output+=x.data*self.child_weights[i]
		if output <= 0:
			output = -1
		else:
			output = 1
		self.data = output
	#for building
	def add_child(self, obj):
		for x in obj:
			self.children.append(x)
	#for changing inputs
	def set_child(self, obj):
		for i,x in enumerate(obj):
			self.children[i] = x
	def add_parent(self, obj):
		for x in obj:
			self.parent.append(x)
	def set_weights(self, weights):
		self.child_weights = weights.copy()
	def calc_error(self, desiredOut):
		for i, weight in enumerate(self.child_weights):
			xi = self.children[i].data
			weight = weight + 0.05(desiredOut-self.data)*xi
	def init_weights(self):
		if len(self.children)<=0:
			return
		for x in range(len(self.children)):
			self.child_weights.append(0)
			#self.child_weights.append(random.range(-0.05,0.05))
