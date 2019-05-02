import perceptron
def fileRead():
	with open("iris.data", "r") as f:
		lines = f.read().splitlines()
		attributes = lines[0].split(",")[0:-1]
		target_attribute = lines[0].split(",")[-1]
	training_data = []
	for line in lines[0:-1]:
		training_data.append(line.split(","))
	return training_data 
def createann():
	return ann
def initAnn(ann):
	ann.init_weights()
	for child in ann.children
		child.init_weights()
	return ann
def bpa(ann irisDat):
	#1. stopping criterion
		#2. for each input
			#3. input data into lowest level of ann and run ann
			runAnn(ann, irisDat[x])			
			#4. calc error from output units
			outError = ann.calcError()
			#5. calc error from hidden units
			hidError = []
			for child in ann.children:
				hidError.append(child.calcError)
			#6. update weights
			ann.updateWeights(outError)
			for i,child in enumerate(ann.children):
				child.updateWeights(hidError[i])
		#7. end for loop
	#8. check stopping criterion
	#9. return completed network
def main():
	irisDat = fileRead()
	ann = createAnn()
	ann = initAnn(ann)
	bpa(ann, irisDat)
