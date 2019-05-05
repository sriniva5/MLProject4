import perceptron as prc

#Reads in the data file and returns an array of training examples
#The training examples consist of tuples, where each tuple is a vector and target value
def fileRead():
	training_data = []

	with open("iris.data", "r") as f:
		lines = f.read().splitlines()

	for line in lines[0:-1]:
		l = line.split(',')
		training_data.append((l[0:4], l[4]))

	#print(training_data)
	return training_data

if __name__ == "__main__":
	irisData = fileRead()

	#initialize the perceptron and set random weights
	p = prc.Perceptron(irisData, 0.05)
	p.init_weights()

	#for each example determine if the output is greater or less than 0
	for f in range(len(p.data)):
		if p.compute_output(p.data[f][0], p.weights[f]) == -1:
			p.set_weights(f)
