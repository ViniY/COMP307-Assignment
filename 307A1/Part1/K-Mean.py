import pandas as pd
import random
random.seed(307)
# from keras import preprocessing


def read_file(path):
    file_path = path
    iris_data_f = pd.read_csv(file_path, header=None, sep="\s+",
                              names=["sepal_length", "sepal_width", "petal_length", "petal_width", "class_label"])
    return iris_data_f


def pre_processing_data(data):
    # normalize the data before feed to the model
    x = data[["sepal_length", "sepal_width", "petal_length", "petal_width"]]
    y = data[["class_label"]]
    # x_normalized = preprocessing.normalize(x)
    x_normalized = x
    return x_normalized, y


def clusters(data_list, rangs, center_cluster_1, center_cluster_2, center_cluster_3, count):
    count += 1
    data_list = cluster_method(data_list, center_cluster_1,center_cluster_2,center_cluster_3,rangs)
    newcenter1, newcenter2, newcenter3 = calculate_center(data_list)
    if (newcenter1, newcenter2, newcenter3) == (center_cluster_1, center_cluster_2, center_cluster_3):
        print("The results after {} times and after {} times are same, so the final center is:".format(count - 1, count))
        print("Center of cluster 1 : ", center_cluster_1)
        print("Center of cluster 2 : ", center_cluster_2)
        print("Center of cluster 3 : ", center_cluster_3)
        for instance in data_list:
            print(instance)
        return center_cluster_1, center_cluster_2, center_cluster_3
    else:
        print("results after {} times".format(count))
        print("Center of cluster 1 : ", newcenter1)
        print("Center of cluster 2 : ", newcenter2)
        print("Center of cluster 3 : ", newcenter3)
        clusters(data_list, rangs, newcenter1, newcenter2, newcenter3, count)


def cluster_method(data_list, clustercenter1, clustercenter2, clustercenter3, ranging):
    """give cluster for each instance"""
    for data in data_list:
        d_cluster1 = distance_measure(data, clustercenter1, ranging[0], ranging[1], ranging[2], ranging[3])
        d_cluster2 = distance_measure(data, clustercenter2, ranging[0], ranging[1], ranging[2], ranging[3])
        d_cluster3 = distance_measure(data, clustercenter3, ranging[0], ranging[1], ranging[2], ranging[3])
        temp = min(d_cluster1, d_cluster2, d_cluster3)
        if temp == d_cluster1:
            # print("length of data :", len(data))
            data[4] = 100
        elif temp == d_cluster2:
            data[4] = 200
        else:
            data[4] = 300
    return data_list


def calculate_center(data_list):
    """calculate centers of three clusters"""
    cluster1 = []
    cluster2 = []
    cluster3 = []
    for data in data_list:
        if data[4] == 100:
            cluster1.append(data)
        elif data[4] == 200:
            cluster2.append(data)
        else:
            cluster3.append(data)
    clustercenter1 = calculate_mean(cluster1)
    # print("-----------------------")
    # print(len(cluster1))
    # print(len(cluster2))
    # print(len(cluster3))
    clustercenter2 = calculate_mean(cluster2)
    clustercenter3 = calculate_mean(cluster3)
    return clustercenter1, clustercenter2, clustercenter3


def calculate_mean(cluster):
    a, b, c, d = 0, 0, 0, 0
    total = len(cluster)
    # print(total)
    for data in cluster:
        a += data[0]
        b += data[1]
        c += data[2]
        d += data[3]
    new_center = [a / total, b / total, c / total, d / total]
    return new_center


def distance_measure(data, cluster, r1, r2, r3, r4):
    # print("=======================================")
    # print(data)
    distance = (((data[0] - cluster[0])/r1)**2 +  ((data[1] - cluster[1])/r2)**2 + ((data[2] - cluster[2])/r3)**2 + ((data[3] - cluster[3])/r4)**2) ** 0.5
    return distance




def main():
    training_path = "iris-training.txt"
    df = read_file(training_path)
    testing_path = "iris-test.txt"
    x_training, y_training = pre_processing_data(df)
    df_testing = read_file(testing_path)
    x_testing, y_testing = pre_processing_data(df_testing)
    x = x_training.append(x_testing,ignore_index= True)
    k = 3
    number_of_data = 150

    # cluster_center_list = random.sample(x,k)
    cluster_center_1 = [5.1,  3.5,  1.4,  0.2]
    cluster_center_2 = [7.0,  3.2,  4.7,  1.4]
    cluster_center_3 = [6.3,  3.3,  6.0,  2.5]
    count = 0
    # convert datafrmae into a list
    k  = x.loc[0:].values.tolist()
    data_list = k

    for elem in data_list:
        # print("type of element : ", type(elem))
        elem.append(0)
    # print("++++++++++++++++++")
    # print(len(data_list[0]))
    ranges = []
    range1 = x['sepal_length'].max() - x['sepal_length'].min()
    # print(range1)
    range2 = x['sepal_width'].max() - x['sepal_width'].min()
    range3 = x['petal_length'].max() - x['petal_length'].min()
    range4 = x['petal_width'].max() - x['petal_width'].min()
    ranges.append(range1)
    ranges.append(range2)
    ranges.append(range3)
    ranges.append(range4)


    clusters(data_list, ranges, cluster_center_1, cluster_center_2,cluster_center_3, count)


if __name__ == '__main__':
    main()