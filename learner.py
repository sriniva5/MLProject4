import perceptron as prc

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
	irisData = fileRead("Iris-setosa")

	#initialize the perceptron and set random weights
	p = prc.Perceptron(irisData, 0.05)
	p.init_weights()

	#for each example alter the weights based on the classification
	for f in range(len(p.data)):
		output = p.compute_output(p.data[f][0], p.weights[f])
		p.set_weights(f,output)
