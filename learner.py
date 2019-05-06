from perceptron import Perceptron
import sys
import os
import copy

def fileRead():
	with open("iris.data", "r") as f:
		lines = f.read().splitlines()
		attributes = lines[0].split(",")[0:-1]
		target_attribute = lines[0].split(",")[-1]
	training_data = []
	for line in lines[0:-1]:
		training_data.append(line.split(","))
	return training_data

def createAnn():
	ann = Perceptron()
	child1 = Perceptron()
	child2 = Perceptron()
	child3 = Perceptron()
	child4 = Perceptron()
	childs = [child1, child2, child3, child4]
	ann.add_child(childs)
	initInput = [0,0,0,0]
	for child in ann.children:
		child.add_child(initInput)
	return ann

def initAnn(ann):
	ann.init_weights()
	for child in ann.children:
		child.init_weights()
	return ann

def runAnn(ann, le):
	# initialize inputs
	for i, child in enumerate(ann.children):
		child.add_child = le[i]
	# calc outputs of hidden level
	for child in ann.children:
		child.calc_output_hidden()
	# calc output of top level
	ann.calc_output()
	return ann.data

def updateWeights(ann, desiredOut):
	ann.calc_error(desiredOut)
	for child in ann.children:
		child.calc_error(desiredOut)

def printWeights(children):
	weights = []
	for child in children:
		weights.append(child.child_weights)
	return weights

def pta(ann, irisDat):
	sys.stdout = open("output.txt", "w")
	incorrect = 1
	epoch = 0
	while incorrect != 0:
		incorrect = 0
		print(incorrect)
		for x in irisDat:
			#3. input data into lowest level of ann and run ann
			output = runAnn(ann, x)
			#4. calc error from output units
			teAns = 1 if x[4] == "Iris-setosa" else 0
			#5. update weights
			if teAns != ann.data:
				incorrect += 1
				updateWeights(ann, teans)
		#7. end for loop
		epoch += 1
		printChildWeights = printWeights(ann.children)
		print(epoch+","+incorrect+","+ann.data+","+printChildWeights)
	#8. check stopping criterion
	#9. return completed network

def main():
	print("run")
	irisDat = fileRead()
	ann = createAnn()
	initAnn(ann)
	pta(ann, irisDat)

main()
