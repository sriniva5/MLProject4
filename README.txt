Ananya Srinivasan, Javier Piraneque, Chris Weeden, Kevin Ackerman
CSC 470 - Machine Learning 
Project 4
5/10/19

====Project Contents====
- iris.data: The original training data
- perceptron.py: The class used to initialize the perceptron, compute the output, and update its weights based on the classification.  
- PTR.py: Reads in the iris.data file or the irisShuffle.data file based on the command line argument, and the target value (Iris-setosa, Iris-versicolor, or Iris-virginica) for the corresponding learning problem. One condition when learning is stopped is when the number of learning errors is zero. To handle cases where the learning process may not converge to no errors, the current epoch and the preErrorsInWindow variable is used to determine when to terminate the learning process. The preErrorsInWindow is initially set to 151 (one more than the number of training data). If the preErrorsInWindow is less than or equal to errorsInWindow (which is an accumulation of the errors over epochs) and the epoch is a multiple of 10, then learning is stopped. 
- 
