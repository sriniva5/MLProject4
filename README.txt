Ananya Srinivasan, Javier Piraneque, Chris Weeden, Kevin Ackerman
CSC 470 - Machine Learning 
Project 4
5/10/19

====Project Contents====
- iris.data: The original training data
-shuffle.py: Shuffles the original dataset, iris.data, and outputs the new dataset into the irisShuffle.data file
	- irisShuffle.data: Data file of shuffled dataset
- perceptron.py: The class used to initialize the perceptron, compute the output, and update its weights based on the classification.  
- PTR.py: Reads in the iris.data file or the irisShuffle.data file based on the command line argument, and the target value (Iris-setosa, Iris-versicolor, or Iris-virginica) for the corresponding learning problem. One condition when learning is stopped is when the number of learning errors is zero. To handle cases where the learning process may not converge to no errors, the current epoch and the preErrorsInWindow variable is used to determine when to terminate the learning process. The preErrorsInWindow is initially set to 151 (one more than the number of training data). If the preErrorsInWindow is less than or equal to errorsInWindow (which is an accumulation of the errors over epochs) and the epoch is a multiple of 10, then learning is stopped. 
	- output.txt: The resulting stats file (epoch, errors, and adjusted weights) produced for the learning problem
- plot.py: [Requires Python 3 or higher] The plotting file which uses matplotlib and pandas to plot the graphs for learning problems.
- Statistics folders:
	- weight0: Folder containing the stats files for the three learning problems (txt) and their plots (pdf) when the initial weights are set to zero. (T2)
	- weight1: Folder containing the stats files for the three learning problems (txt) and their plots (pdf) when the initial weights are set to one. (T3.1)
	- weightrand0: Folder containing the stats files for the three learning problems (txt) and their plots (pdf) when the initial weights are set to random values between 0 and 1. (T3.2)
	- weightrand1: Folder containing the stats files for the three learning problems (txt) and their plots (pdf) when the initial weights are set to different random values between 0 and 1 from those of weightrand0. (T3.3)
	- shuff0: Folder containing the stats files for the three learning problems (txt) and their plots (pdf) when the initial weights are set to zero and the dataset is shuffled in a random order. (T4.1)
	- shuff1: Folder containing the stats files for the three learning problems (txt) and their plots (pdf) when the initial weights are set to zero and the dataset is shuffled in a random order different from that of shuff0. (T4.2)
- MLProject4Writeup.pdf: A report of our findings, answers to the T2 question, and D6. 

====To Run====
To run our program:

	python PTR.py [datafile] [target] [weight-option]

where datafile can be iris.data or irisShuffle.data, target is Iris-setosa, Iris-versicolor, or Iris-virginica, and weight-option can be 0 (all zeros), 1 (all 1s) or r (random). You can find the stats in the output.txt file.

For example, run:

	python PTR.py iris.data Iris-virginica r

to get results for the Iris-virginica examples, where the initial weights are random, and the data set is in the original order.

Another example of the command line arguments:

 	python PTR.py irisShuffle.data Iris-setosa 1

which produces stats for the Iris-setosa, where the initial weights are all 1 and the data set is shuffled. 

To randomize the irisShuffle.data file again, run:

	python shuffle.py
