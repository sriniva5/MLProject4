import perceptron
def main():
	irisDat = fileread()
	ann = createann()
	ann = initann(ann)
	bpa(ann, irisDat)
