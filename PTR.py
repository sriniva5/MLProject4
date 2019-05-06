import perceptron as prc
import sys

#Reads in the data file and returns an array of training examples
#The training examples consist of tuples, where each tuple is a vector and target value
def fileRead(target):
	training_data = []

	with open("iris.data", "r") as f:
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
	target_val = sys.argv[1]
	irisData = fileRead(target_val)
	pre_error = 151
	sys.stdout = open("output.txt", "w")
	#initialize the perceptron and set random weights
	#initialize error list
	p = prc.Perceptron(irisData, 0.05)
	p.init_weights([0.0,0.0,0.0,0.0,0.0])
	
	#Repeat process until errors are minimized
	while True:
		#for each example alter the weights based on the classification
		for f in range(len(p.data)):
			#print(p.weights)
			output = p.compute_output(p.data[f][0], p.weights)
			#print(output)
			p.set_weights(f, output)
		p.epoch +=1
		print(p.epoch,",",p.errors,",",p.weights,'\n')
		if p.errors == 0:
			break
#		elif pre_error <= p.errors:
#			break
		pre_error = p.errors
		p.errors = 0
