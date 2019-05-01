import random
class Perceptron():
	def __init__(self):
		self.data = NULL
		self.children = []
		self.parent = []
		self.child_weights = []
	def printNice(self, level=0):
		print("\t"*level+self.data)
		for child in self.children:
			child.printNice(level+1)
	def calc_output(self):
		output = self.child_weights[0]
		for i, x in enumerate(children):
			output+=x.data*self.child_weights[i]
		self.data = output
	def add_child(self, obj):
		self.children.append(obj)
	def add_parent(self, obj):
		self.parent.append(obj)
	def set_weights(self, weights):
		self.child_weights = weights.copy()
	def init_weights(self):
		if len(children)<=0:
			return
		for x in range(len(children)+1):
			self.child_weights.append(random.range(-0.05,0.05))
