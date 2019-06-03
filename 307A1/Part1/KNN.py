import sklearn
import matplotlib.pyplot as plt
import pandas as pd
from sklearn import preprocessing
from itertools import islice
import numpy as np

# used for using cross validation

# Since this is a lazy learning therefore there is not a training process
# The function below will return the data frame of the current dataset


def read_file(path):
    file_path = path
    iris_data_f = pd.read_csv(file_path, header=None, sep="\s+",
                              names=["sepal_length", "sepal_width", "petal_length", "petal_width", "class_label"])
    return iris_data_f


def visualization(data):
    data = pd.DataFrame(data)
    hist = plt.hist(x=0, data=data, bins=3)
    hist_plot = plt.show()


def pre_processing_data(data):
    # normalize the data before feed to the model
    x = data[["sepal_length", "sepal_width", "petal_length", "petal_width"]]
    y = data[["class_label"]]
    # x_normalized = preprocessing.normalize(x)
    x_normalized = x
    return x_normalized, y


def knn_main_process(df):
    return 0


def compute_euclidean_distance(training_data, test_data):
    distance_list = []
    f_1_max = training_data['sepal_length'].max()
    f_1_min = training_data['sepal_length'].min()
    f_1_range = f_1_max - f_1_min
    f_2_max = training_data['sepal_width'].max()
    f_2_min = training_data['sepal_width'].min()
    f_2_range = f_2_max - f_2_min
    f_3_max = training_data['petal_length'].max()
    f_3_min = training_data['petal_length'].min()
    f_3_range = f_3_max - f_3_min
    f_4_max = training_data['petal_width'].max()
    f_4_min = training_data['petal_width'].min()
    f_4_range = f_4_max - f_4_min
    ranges = []
    ranges.append(f_1_range)
    ranges.append(f_2_range)
    ranges.append(f_3_range)
    ranges.append(f_4_range)
    for index in range(pd.DataFrame(test_data).shape[0]):
        d = {}
        counter = 0
        for row_index in range(training_data.shape[0]):
            counter = counter + 1
            distance = 0
            # for m in range(4):
            for m in range(pd.DataFrame(training_data).shape[1]):
                distance += (pow((pd.DataFrame(training_data).iat[row_index, m] - pd.DataFrame(test_data).iat[index, m]),2)/pow(ranges[m],2))
            distance = np.sqrt(distance)
            d.update({row_index: distance})
        distance_list.append(d)



    return distance_list


def take(n, iterable):
    "Return first n items of the iterable as a list"
    return list(islice(iterable, n))


def find_k_nearst_neighbours(k, sorted_list):
    list = []
    for index in range(len(sorted_list)):
        d = take(k, dict(sorted_list[index]).items())
        list.append(d)
    return list


def sort_distance_matrix(list):
    for index in range(len(list)):
        d_sort = dict(sorted(dict(list[index]).items(), key=lambda kv: kv[1]))
        list[index] = d_sort
    print("values in list is sorted ")
    return list


def check_accuracy(predict_y, test_y):
    test_y = test_y.values.tolist()
    number_elems = len(test_y)
    right = 0
    correctness = []
    for index in range(number_elems):
        if str(predict_y[index]) in str(test_y[index]):
            right = right + 1
            correctness.append("Correct")
        else:
            correctness.append("InCorrect")
    accuracy = float(right )/ number_elems

    return accuracy,correctness


def assign_label(neighbour, y_training):
    list = []
    label = y_training.values.tolist()
    y_training = label
    for index in range(len(neighbour)):
        versicolor = 0
        virginica = 0
        setosa = 0
        for t in neighbour[index] :
            order = tuple(t).__getitem__(0)
            if "versicolor" in str(y_training[order]):
                 versicolor = versicolor + 1
            if "virginica" in str(y_training[order]):
                virginica = virginica + 1
            if "setosa" in str(y_training[order]):
                setosa = setosa + 1
        if versicolor >= setosa and versicolor >= virginica:
            list.append("versicolor")
        elif virginica >= setosa and virginica >= versicolor:
            list.append("virginica")
        else:
            list.append("setosa")
    return list


def write_file(path,my_list,correctness):
    with open(path, 'w') as f:
        for i in range(len(my_list)):
        # for item in my_list:
            if (i % 4) == 0 and i != 0:
                f.write("\n")
            else:
                f.write("%s" % my_list[i])
                f.write("\t")
                f.write("%s" % correctness[i])
                f.write("\t")


def main():
    training_path = "iris-training.txt"
    df = read_file(training_path)
    testing_path = "iris-test.txt"
    x_training, y_training = pre_processing_data(df)
    df_testing = read_file(testing_path)
    x_testing, y_testing = pre_processing_data(df_testing)
    # here we have the map contains the euclidean distance of the points in test set to all the points in the
    # training set
    distance_list = compute_euclidean_distance(x_training, x_testing)
    distance_list_sorted = sort_distance_matrix(distance_list)
    # the function below will return k nearest neighbours
    highest_k = 0
    highest_ac = 0
    acc_list =[]
    for k in range(1,52):
        if k%2!=0:
            neighbour = find_k_nearst_neighbours(k, distance_list_sorted)
            predicted_y = assign_label(neighbour, y_training)
            ac,correctness= check_accuracy(predicted_y, y_testing)
            write_path = "output.txt"
            write_file(write_path, predicted_y, correctness)
            if ac > highest_ac:
                highest_ac =ac
                highest_k = k
            acc_list.append(ac)
    print("best k :", highest_k)
    print("highest accuracy : ", highest_ac)
    """comparing my result with sklearn"""


    number_list = [1,3,5,7,9,11,13,15,17,19,21,23,25,27,29,31,33,35,37,39,41,43,45,47,49,51]
    plt.figure()
    plt.scatter(number_list,acc_list,s=10)
    plt.xlabel('value for K')
    plt.ylabel('Accuracy')
    plt.title('The accuracy against different K value')
    plt.grid(True)
    plt.show()



if __name__ == '__main__':
    main()