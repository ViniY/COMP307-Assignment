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
        return train_set, test_set, number_of_attributes
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


def likelihoodTable(train_data,spam,nonspam,number_of_attri):
    total_instance = spam+nonspam
    likelihood_table=[]
    prob_table = []

    for i in range(number_of_attri):
        c0i0 = 0    # the number of class 0 and this attribute is 0
        c0i1 = 0    # the number of class 0 and this attribute is 1
        c1i0 = 0    # the number of class is 1 and this attribute is 0
        c1i1 = 0    # the number of class is 1 and this attribute is 1
        zeros = 0   # used to check if there is a consequence never happens
        for instance in train_data:
            if instance[1] == 0 and instance[0][i] == 0:
                c0i0 +=1
            if instance[1] == 0 and instance[0][i] == 1:
                c0i1 +=1
            if instance[1] == 1 and instance[0][i] == 0:
                c1i0 +=1
            if instance[1] == 1 and instance[0][i] == 1:
                c1i1 +=1
        likelihood_table.append([c0i0,c0i1,c1i0,c1i1])
        if c0i0 == 0 or c0i1 == 0 or c1i0 == 0 or c1i1 == 0:  # if a sequence never happens
            zeros += 1

    if zeros > 0:
        spam += 1
        nonspam += 1
        new_likehood_table = []
        for i in likelihood_table:
            i[0] += 1
            i[1] += 1
            i[2] += 1
            i[3] += 1
            new_likehood_table.append([i[0], i[1], i[2], i[3]])
        likelihood_table = new_likehood_table
    for i in likelihood_table:
        prob_table.append([float(i[0])/nonspam, float(i[1])/nonspam, float(i[2])/spam, float(i[3])/spam])

    for i in range(number_of_attri):
        print("P(F{} = 1| C = 1) = {}".format(i, prob_table[i][0]))
        print("P(F{} = 0| C = 1) = {}".format(i, prob_table[i][1]))
        print("P(F{} = 1| C = 0) = {}".format(i, prob_table[i][2]))
        print("P(F{} = 0| C = 0) = {}".format(i, prob_table[i][3]))
        print("\n")
    return likelihood_table,prob_table,spam , nonspam


def classifier(test_data, prob_table, spam, nospam):
    for instance in test_data:
        a = float(spam) / (spam + nospam)
        b = float(nospam) / (spam + nospam)
        for i in range(12):
            if instance[i] == '1':
                a *= prob_table[i][0]
                b *= prob_table[i][2]
            else:
                a *= prob_table[i][1]
                b *= prob_table[i][3]
        if a > b:
            print('Score(spam) is {}, Score(non-spam) is {}.'.format(a, b))
            print(instance, 'spam')
        else:
            print('Score(spam) is {}, Score(non-spam) is {}.'.format(a, b))
            print(instance, 'nospam')


def main():
    path_labeled = 'spamLabelled.dat'
    path_unlabeled = 'spamUnlabelled.dat'
    train_data, test_data, number_of_attri = data_reader(path_labeled,path_unlabeled)
    spam_number,nonspam_number = counter_spam(train_data)
    # visualise(train_data)
    print(spam_number)
    print(nonspam_number)
    likelihood_table,prob_table,spam,nonspam = likelihoodTable(train_data,spam_number,nonspam_number,number_of_attri)
    spam_number = spam
    nonspam_number = nonspam
    print(spam_number)
    print(nonspam_number)
    classifier(test_data,prob_table, spam, nonspam)


if __name__ == '__main__':
    main()