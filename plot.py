import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats

if __name__ == "__main__":
    file = "./weight0/setosa0.txt"
    type = "setosa"
    weight_type = "weights = 0"

    data = pd.read_csv(file, sep=",", header=None)
    data.columns = ["epoch", "errors", "w0", "w1", "w2", "w3", "w4"]
    slope, intercept, r_value, p_value, std_err = stats.linregress(data['epoch'], data['errors'])
    bf = (data['epoch'].values)*slope + intercept

    plt.plot(data['epoch'].values, data['errors'].values, 'ro')
    plt.plot(data['epoch'].values, bf)
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
    slope, intercept, r_value, p_value, std_err = stats.linregress(data['epoch'], data['errors'])
    bf = (data['epoch'].values)*slope + intercept

    plt.plot(data['epoch'].values, data['errors'].values, 'ro')
    plt.plot(data['epoch'].values, bf)
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
    slope, intercept, r_value, p_value, std_err = stats.linregress(data['epoch'], data['errors'])
    bf = (data['epoch'].values)*slope + intercept

    plt.plot(data['epoch'].values, data['errors'].values, 'ro')
    plt.plot(data['epoch'].values, bf)
    plt.xlabel('Epoch #')
    plt.ylabel('# of Errors in Learning')
    plt.title('Number of Learning Errors made per Epoch (' + type + ', ' + weight_type + ')')
    plt.savefig(file[0:-4]+".pdf", bbox_inches="tight")
    plt.clf()

    file = "./weight1/setosa1.txt"
    type = "setosa"
    weight_type = "weights = 1"

    data = pd.read_csv(file, sep=",", header=None)
    data.columns = ["epoch", "errors", "w0", "w1", "w2", "w3", "w4"]
    slope, intercept, r_value, p_value, std_err = stats.linregress(data['epoch'], data['errors'])
    bf = (data['epoch'].values)*slope + intercept

    plt.plot(data['epoch'].values, data['errors'].values, 'ro')
    plt.plot(data['epoch'].values, bf)
    plt.xlabel('Epoch #')
    plt.ylabel('# of Errors in Learning')
    plt.title('Number of Learning Errors made per Epoch (' + type + ', ' + weight_type + ')')
    plt.savefig(file[0:-4]+".pdf", bbox_inches="tight")
    plt.clf()

    file = "./weight1/versicolor1.txt"
    type = "versicolor"
    weight_type = "weights = 1"

    data = pd.read_csv(file, sep=",", header=None)
    data.columns = ["epoch", "errors", "w0", "w1", "w2", "w3", "w4"]
    slope, intercept, r_value, p_value, std_err = stats.linregress(data['epoch'], data['errors'])
    bf = (data['epoch'].values)*slope + intercept

    plt.plot(data['epoch'].values, data['errors'].values, 'ro')
    plt.plot(data['epoch'].values, bf)
    plt.xlabel('Epoch #')
    plt.ylabel('# of Errors in Learning')
    plt.title('Number of Learning Errors made per Epoch (' + type + ', ' + weight_type + ')')
    plt.savefig(file[0:-4]+".pdf", bbox_inches="tight")
    plt.clf()

    file = "./weight1/virginica1.txt"
    type = "virginica"
    weight_type = "weights = 1"

    data = pd.read_csv(file, sep=",", header=None)
    data.columns = ["epoch", "errors", "w0", "w1", "w2", "w3", "w4"]
    slope, intercept, r_value, p_value, std_err = stats.linregress(data['epoch'], data['errors'])
    bf = (data['epoch'].values)*slope + intercept

    plt.plot(data['epoch'].values, data['errors'].values, 'ro')
    plt.plot(data['epoch'].values, bf)
    plt.xlabel('Epoch #')
    plt.ylabel('# of Errors in Learning')
    plt.title('Number of Learning Errors made per Epoch (' + type + ', ' + weight_type + ')')
    plt.savefig(file[0:-4]+".pdf", bbox_inches="tight")
    plt.clf()

    file = "./weightrand0/setosarand0.txt"
    type = "setosa"
    weight_type = "random weights"

    data = pd.read_csv(file, sep=",", header=None)
    data.columns = ["epoch", "errors", "w0", "w1", "w2", "w3", "w4"]
    slope, intercept, r_value, p_value, std_err = stats.linregress(data['epoch'], data['errors'])
    bf = (data['epoch'].values)*slope + intercept

    plt.plot(data['epoch'].values, data['errors'].values, 'ro')
    plt.plot(data['epoch'].values, bf)
    plt.xlabel('Epoch #')
    plt.ylabel('# of Errors in Learning')
    plt.title('Number of Learning Errors made per Epoch (' + type + ', ' + weight_type + ')')
    plt.savefig(file[0:-4]+".pdf", bbox_inches="tight")
    plt.clf()

    file = "./weightrand0/versicolorrand0.txt"
    type = "versicolor"
    weight_type = "random weights"

    data = pd.read_csv(file, sep=",", header=None)
    data.columns = ["epoch", "errors", "w0", "w1", "w2", "w3", "w4"]
    slope, intercept, r_value, p_value, std_err = stats.linregress(data['epoch'], data['errors'])
    bf = (data['epoch'].values)*slope + intercept

    plt.plot(data['epoch'].values, data['errors'].values, 'ro')
    plt.plot(data['epoch'].values, bf)
    plt.xlabel('Epoch #')
    plt.ylabel('# of Errors in Learning')
    plt.title('Number of Learning Errors made per Epoch (' + type + ', ' + weight_type + ')')
    plt.savefig(file[0:-4]+".pdf", bbox_inches="tight")
    plt.clf()

    file = "./weightrand0/virginicarand0.txt"
    type = "virginica"
    weight_type = "random weights"

    data = pd.read_csv(file, sep=",", header=None)
    data.columns = ["epoch", "errors", "w0", "w1", "w2", "w3", "w4"]
    slope, intercept, r_value, p_value, std_err = stats.linregress(data['epoch'], data['errors'])
    bf = (data['epoch'].values)*slope + intercept

    plt.plot(data['epoch'].values, data['errors'].values, 'ro')
    plt.plot(data['epoch'].values, bf)
    plt.xlabel('Epoch #')
    plt.ylabel('# of Errors in Learning')
    plt.title('Number of Learning Errors made per Epoch (' + type + ', ' + weight_type + ')')
    plt.savefig(file[0:-4]+".pdf", bbox_inches="tight")
    plt.clf()

    file = "./weightrand1/setosarand1.txt"
    type = "setosa"
    weight_type = "random weights"

    data = pd.read_csv(file, sep=",", header=None)
    data.columns = ["epoch", "errors", "w0", "w1", "w2", "w3", "w4"]
    slope, intercept, r_value, p_value, std_err = stats.linregress(data['epoch'], data['errors'])
    bf = (data['epoch'].values)*slope + intercept

    plt.plot(data['epoch'].values, data['errors'].values, 'ro')
    plt.plot(data['epoch'].values, bf)
    plt.xlabel('Epoch #')
    plt.ylabel('# of Errors in Learning')
    plt.title('Number of Learning Errors made per Epoch (' + type + ', ' + weight_type + ')')
    plt.savefig(file[0:-4]+".pdf", bbox_inches="tight")
    plt.clf()

    file = "./weightrand1/versicolorrand1.txt"
    type = "versicolor"
    weight_type = "random weights"

    data = pd.read_csv(file, sep=",", header=None)
    data.columns = ["epoch", "errors", "w0", "w1", "w2", "w3", "w4"]
    slope, intercept, r_value, p_value, std_err = stats.linregress(data['epoch'], data['errors'])
    bf = (data['epoch'].values)*slope + intercept

    plt.plot(data['epoch'].values, data['errors'].values, 'ro')
    plt.plot(data['epoch'].values, bf)
    plt.xlabel('Epoch #')
    plt.ylabel('# of Errors in Learning')
    plt.title('Number of Learning Errors made per Epoch (' + type + ', ' + weight_type + ')')
    plt.savefig(file[0:-4]+".pdf", bbox_inches="tight")
    plt.clf()

    file = "./weightrand1/virginicarand1.txt"
    type = "virginica"
    weight_type = "random weights"

    data = pd.read_csv(file, sep=",", header=None)
    data.columns = ["epoch", "errors", "w0", "w1", "w2", "w3", "w4"]
    slope, intercept, r_value, p_value, std_err = stats.linregress(data['epoch'], data['errors'])
    bf = (data['epoch'].values)*slope + intercept

    plt.plot(data['epoch'].values, data['errors'].values, 'ro')
    plt.plot(data['epoch'].values, bf)
    plt.xlabel('Epoch #')
    plt.ylabel('# of Errors in Learning')
    plt.title('Number of Learning Errors made per Epoch (' + type + ', ' + weight_type + ')')
    plt.savefig(file[0:-4]+".pdf", bbox_inches="tight")
    plt.clf()

    file = "./shuff0/setosashuff0.txt"
    type = "setosa"
    weight_type = "shuffled dataset"

    data = pd.read_csv(file, sep=",", header=None)
    data.columns = ["epoch", "errors", "w0", "w1", "w2", "w3", "w4"]
    slope, intercept, r_value, p_value, std_err = stats.linregress(data['epoch'], data['errors'])
    bf = (data['epoch'].values)*slope + intercept

    plt.plot(data['epoch'].values, data['errors'].values, 'ro')
    plt.plot(data['epoch'].values, bf)
    plt.xlabel('Epoch #')
    plt.ylabel('# of Errors in Learning')
    plt.title('Number of Learning Errors made per Epoch (' + type + ', ' + weight_type + ')')
    plt.savefig(file[0:-4]+".pdf", bbox_inches="tight")
    plt.clf()

    file = "./shuff0/versicolorshuff0.txt"
    type = "versicolor"
    weight_type = "shuffled dataset"

    data = pd.read_csv(file, sep=",", header=None)
    data.columns = ["epoch", "errors", "w0", "w1", "w2", "w3", "w4"]
    slope, intercept, r_value, p_value, std_err = stats.linregress(data['epoch'], data['errors'])
    bf = (data['epoch'].values)*slope + intercept

    plt.plot(data['epoch'].values, data['errors'].values, 'ro')
    plt.plot(data['epoch'].values, bf)
    plt.xlabel('Epoch #')
    plt.ylabel('# of Errors in Learning')
    plt.title('Number of Learning Errors made per Epoch (' + type + ', ' + weight_type + ')')
    plt.savefig(file[0:-4]+".pdf", bbox_inches="tight")
    plt.clf()

    file = "./shuff0/virginicashuff0.txt"
    type = "virginica"
    weight_type = "shuffled dataset"

    data = pd.read_csv(file, sep=",", header=None)
    data.columns = ["epoch", "errors", "w0", "w1", "w2", "w3", "w4"]
    slope, intercept, r_value, p_value, std_err = stats.linregress(data['epoch'], data['errors'])
    bf = (data['epoch'].values)*slope + intercept

    plt.plot(data['epoch'].values, data['errors'].values, 'ro')
    plt.plot(data['epoch'].values, bf)
    plt.xlabel('Epoch #')
    plt.ylabel('# of Errors in Learning')
    plt.title('Number of Learning Errors made per Epoch (' + type + ', ' + weight_type + ')')
    plt.savefig(file[0:-4]+".pdf", bbox_inches="tight")
    plt.clf()

    file = "./shuff1/setosashuff1.txt"
    type = "setosa"
    weight_type = "shuffled dataset"

    data = pd.read_csv(file, sep=",", header=None)
    data.columns = ["epoch", "errors", "w0", "w1", "w2", "w3", "w4"]
    slope, intercept, r_value, p_value, std_err = stats.linregress(data['epoch'], data['errors'])
    bf = (data['epoch'].values)*slope + intercept

    plt.plot(data['epoch'].values, data['errors'].values, 'ro')
    plt.plot(data['epoch'].values, bf)
    plt.xlabel('Epoch #')
    plt.ylabel('# of Errors in Learning')
    plt.title('Number of Learning Errors made per Epoch (' + type + ', ' + weight_type + ')')
    plt.savefig(file[0:-4]+".pdf", bbox_inches="tight")
    plt.clf()

    file = "./shuff1/versicolorshuff1.txt"
    type = "versicolor"
    weight_type = "shuffled dataset"

    data = pd.read_csv(file, sep=",", header=None)
    data.columns = ["epoch", "errors", "w0", "w1", "w2", "w3", "w4"]
    slope, intercept, r_value, p_value, std_err = stats.linregress(data['epoch'], data['errors'])
    bf = (data['epoch'].values)*slope + intercept

    plt.plot(data['epoch'].values, data['errors'].values, 'ro')
    plt.plot(data['epoch'].values, bf)
    plt.xlabel('Epoch #')
    plt.ylabel('# of Errors in Learning')
    plt.title('Number of Learning Errors made per Epoch (' + type + ', ' + weight_type + ')')
    plt.savefig(file[0:-4]+".pdf", bbox_inches="tight")
    plt.clf()

    file = "./shuff1/virginicashuff1.txt"
    type = "virginica"
    weight_type = "shuffled dataset"

    data = pd.read_csv(file, sep=",", header=None)
    data.columns = ["epoch", "errors", "w0", "w1", "w2", "w3", "w4"]
    slope, intercept, r_value, p_value, std_err = stats.linregress(data['epoch'], data['errors'])
    bf = (data['epoch'].values)*slope + intercept

    plt.plot(data['epoch'].values, data['errors'].values, 'ro')
    plt.plot(data['epoch'].values, bf)
    plt.xlabel('Epoch #')
    plt.ylabel('# of Errors in Learning')
    plt.title('Number of Learning Errors made per Epoch (' + type + ', ' + weight_type + ')')
    plt.savefig(file[0:-4]+".pdf", bbox_inches="tight")
    plt.clf()
