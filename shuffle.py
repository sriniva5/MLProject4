import sys
import random


def fileRead():
	training_data = []

	with open("iris.data", "r") as f:
		lines = f.read().splitlines()

	for line in lines[0:-1]:
		l = line.split(',')
		training_data.append((l[0],l[1],l[2],l[3], l[4]))

	#print(training_data)
	return training_data

if __name__ == "__main__":
	#read data file and mark corresponding target with 1
	#Target values: "Iris-setosa", "Iris-versicolor", "Iris-virginica"
	sys.stdout = open("irisShuffle.data", "w")
	irisData = fileRead()
	irisData = random.sample(irisData, len(irisData))
	for dataline in irisData:
		print(dataline[0],",",dataline[1],",",dataline[2],",",dataline[3],",",dataline[4])