import perceptron

def fileread():
	with open("iris.data", "r") as f:
		lines = f.read().splitlines()
		attributes = lines[0].split(",")[0:-1]
		target_attribute = lines[0].split(",")[-1]

	training_data = []

	for line in lines[0:-1]:
		training_data.append(line.split(","))

	return training_data 

def main():
	irisDat = fileread()
	print(irisDat)
	#ann = createann()
	#ann = initann(ann)
	#bpa(ann, irisDat)

main()
