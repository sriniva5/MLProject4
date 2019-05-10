import perceptron as prc
import random
import sys

#Reads in the data file and returns an array of training examples
#The training examples consist of tuples, where each tuple is a vector and target value
def fileRead(file, target):
	training_data = []

	with open(file, "r") as f:
		lines = f.read().splitlines()

	for line in lines[0:-1]:
		l = line.split(',')
		if l[4] == target:
			training_data.append((l[0:4], 1))
		else:
			training_data.append((l[0:4], -1))

	#print(training_data)
	return training_data

if __name__ == "__main__":
	#read data file and mark corresponding target with 1
	#Target values: "Iris-setosa", "Iris-versicolor", "Iris-virginica"
	file_val = sys.argv[1]
	target_val = sys.argv[2]
	weight_option = sys.argv[3]

	irisData = fileRead(file_val, target_val)
	pre_error = 151
	sys.stdout = open("output.txt", "w")
	#initialize the perceptron and set random weights
	#initialize error list
	p = prc.Perceptron(irisData, 0.05)
	p.init_weights([0.0,0.0,0.0,0.0,0.0])

	if weight_option == 0:
		p.init_weights([0.0,0.0,0.0,0.0,0.0])
	elif weight_option == 1:
		p.init_weights([1.0,1.0,1.0,1.0,1.0])
	elif weight_option == "r":
		p.init_weights([random.uniform(0,1),random.uniform(0,1),random.uniform(0,1),random.uniform(0,1),random.uniform(0,1)])

	# variables for window of epochs
	preErrorsInWindow = 151
	errorsInWindow = 0

	#Repeat process until errors are minimized
	while True:
		#for each example alter the weights based on the classification
		for f in range(len(p.data)):
			#print(p.weights)
			output = p.compute_output(p.data[f][0], p.weights)
			#print(output)
			p.set_weights(f, output)
		p.epoch += 1
		errorsInWindow += p.errors
		print(p.epoch,",",p.errors,",",p.weights,'\n')
		# for i,weight in enumerate(p.weights):
		# 	prevWeights[i]+=float(weight)
		if p.errors == 0:
			break
		if p.epoch%10 == 0 and preErrorsInWindow <= errorsInWindow:
			break
		elif p.epoch%10 == 0:
			preErrorsInWindow = errorsInWindow
			errorsInWindow = 0
		p.errors = 0
