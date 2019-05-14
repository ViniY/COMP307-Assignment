"""
The code for implementing Naive Bayes
Vincent Yu
"""
from matplotlib.colors import ListedColormap


def data_reader(path_labeled, path_unlabeled):
    try:
        train_file = open(path_labeled,'r')
        training_data = train_file.readlines()
        train_file.close()
        test_file = open(path_unlabeled,'r')
        test_data = test_file.readlines()
        test_file.close()
        # print(training_data[0])
        # print(test_data[0])
        train_set = []
        for line in training_data[:]:
            if line != '\n':
                attri = line.split()
                attributes = []
                number_of_attributes = len(attri)-1
                for i in range(number_of_attributes):
                    attributes.append(attri[i])
                train_set.append([attributes, attri[12]])
        test_set =[]
        for line in test_data[:]:
            if line != '\n':
                attri = line.split()
                attributes = []
                number_of_attributes = len(attri)
                for i in range(number_of_attributes):
                    attributes.append(attri[i])
                test_set.append(attributes)
        # print(len(test_set))
        # print(len(train_set))
        return train_set,test_set,number_of_attributes
    except():
        print("File reading Error")
        pass



def counter_spam(train_data):
    spam = 0
    non_spam = 0
    for instance in train_data:
        if instance[1] == '0':
            non_spam += 1
        else:
            spam += 1
    return spam,non_spam

# def visualise(train_data):
#     # visualize the training set
#     from matplotlib.colors import ListedColormap
#     from matplotlib import pyplot as plt
#     import numpy as np
#     train_x =[]
#     train_y=[]
#     for instance in train_data:
#         train_x.append(instance[0])
#         train_y.append(instance[1])
#     X_set, y_set = train_x,train_y
#     for i, j in enumerate(np.unique(y_set)):
#         plt.scatter(X_set[y_set == j, 0], X_set[y_set == j, 1],
#                     c=ListedColormap(('red', 'green'))(i), label=j, marker='.')
#     plt.title('Training set')
#     plt.legend()
#     plt.show()

def likelihood_table(train_data,spam,nonspam,number_of_attri):
    total_instance = spam+nonspam
    likelihood_table=[]

    for i in range(number_of_attri):
        c0i0 = 0    # the number of class 0 and this attribute is 0
        c0i1 = 0    # the number of class 0 and this attribute is 1
        c1i0 = 0    # the number of class is 1 and this attribute is 0
        c1i1 = 0    # the number of class is 1 and this attribute is 1
        for instance in train_data:
            if instance[1] == 0 and instance[0][i] == 0:
                c0i0 +=1
            if instance[1] == 0 and instance[0][i] == 1:
                c0i1 +=1
            if instance[1] == 1 and instance[0][i] == 0:
                c1i0 +=1
            if instance[1] == 1 and instance[0][i] == 1:
                c1i1 +=1






def main():
    path_labeled = 'spamLabelled.dat'
    path_unlabeled = 'spamUnlabelled.dat'
    train_data, test_data, number_of_attri = data_reader(path_labeled,path_unlabeled)
    spam_number,nonspam_number = counter_spam(train_data)
    # visualise(train_data)
    print(spam_number)
    print(nonspam_number)
    likelihood_table(train_data,spam_number,nonspam_number,number_of_attri)

if __name__ == '__main__':
    main()