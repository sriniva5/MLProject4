import pandas as pd
import matplotlib.pyplot as plt

if __name__ == "__main__":
    file = "./weight0/setosa0.txt"
    type = "setosa"
    weight_type = "weights = 0"

    data = pd.read_csv(file, sep=",", header=None)
    data.columns = ["epoch", "errors", "w0", "w1", "w2", "w3", "w4"]

    plt.plot(data['epoch'].values, data['errors'].values, 'ro')
    plt.xlabel('Epoch #')
    plt.ylabel('# of Errors in Learning')
    plt.title('Number of Learning Errors made per Epoch (' + type + ', ' + weight_type + ')')
    plt.savefig(file[0:-4]+".pdf", bbox_inches="tight")
    plt.clf()

    file = "./weight0/versicolor0.txt"
    type = "versicolor"
    weight_type = "weights = 0"

    data = pd.read_csv(file, sep=",", header=None)
    data.columns = ["epoch", "errors", "w0", "w1", "w2", "w3", "w4"]

    plt.plot(data['epoch'].values, data['errors'].values, 'ro')
    plt.xlabel('Epoch #')
    plt.ylabel('# of Errors in Learning')
    plt.title('Number of Learning Errors made per Epoch (' + type + ', ' + weight_type + ')')
    plt.savefig(file[0:-4]+".pdf", bbox_inches="tight")
    plt.clf()

    file = "./weight0/virginica0.txt"
    type = "virginica"
    weight_type = "weights = 0"

    data = pd.read_csv(file, sep=",", header=None)
    data.columns = ["epoch", "errors", "w0", "w1", "w2", "w3", "w4"]

    plt.plot(data['epoch'].values, data['errors'].values, 'ro')
    plt.xlabel('Epoch #')
    plt.ylabel('# of Errors in Learning')
    plt.title('Number of Learning Errors made per Epoch (' + type + ', ' + weight_type + ')')
    plt.savefig(file[0:-4]+".pdf", bbox_inches="tight")
    plt.clf()
