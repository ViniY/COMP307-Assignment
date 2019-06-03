import pandas as pd
import numpy as np
import math
from sklearn.tree import DecisionTreeClassifier
import copy
from statistics import mean

# the data we are using is a highly unbalanced dataset
# in this assignment we are dealing with two dataset


global dominate_label
dominate_label = "abcd"
global dominate_prob
global counter_live
global counter_die
counter_live = 0
counter_die = 0

class Node:
    def __init__(self, bestatt, left, right):
        self.bestAtt = bestatt
        self.left = left
        self.right = right

    def report(self, indent):
        print("{}{} = True\n".format(indent, self.bestAtt))
        self.left.report(indent + "    ")
        print("{}{} = False\n".format(indent, self.bestAtt))
        self.right.report(indent + "    ")


class Leaf:
    def __init__(self, label, prob, instance_left):
        self.label = label
        self.prob = str(prob)
        self.instance_left = instance_left

    def report(self, indent):
        print("{}Class {}, prob = {}, instance_left = {}\n".format(indent, self.label, self.prob, self.instance_left))


def read_file(path):
    counter_live = 0
    counter_die = 0
    dominate_update = True
    if path.__contains__("test"):
        dominate_update = False
    with open(path, 'r') as f:
        next(f)  # skip first row
        header = f.readline()
        df = pd.DataFrame(l.rstrip().split() for l in f)
    header = header.split()
    attribs = copy.copy(header)
    header.insert(0, "class_label")  # now is the right named header that we need
    pd.DataFrame(df).columns = header
    # print("Head of the current DF:", df.head())
    # print("------------------")
    # print(df['class_label'])
    label = pd.DataFrame(df)['class_label']

    # del df['class_label'] # drop  the class label  if we dont need
    data_x = df
    data_y = label
    if dominate_update:
        for label in data_y:
            if label == "live":
                counter_live = counter_live+1
            else:
                counter_die = counter_die +1
        # dominate_label=""
        # dominate_prob =""
        if counter_live >= counter_die:
            global dominate_label
            dominate_label= "live"
            global dominate_prob
            dominate_prob = counter_live / len(data_y)

        else:
            dominate_label = "die"
            dominate_prob = counter_die / len(data_y)
    return data_x, data_y,attribs


# this func gonna convert all the true&false into 0 and 1
def pre_processing(df):
    df = df.applymap(lambda x: 1 if x == "true" else x)
    df = df.applymap(lambda x: 0 if x == "false" else x)
    # print(pd.DataFrame(df).head())
    return df


# the input is the current attributes left in the current brunch
def impurity_selection(attributes, list_instance):
    bestAttr = ""
    lowest_impurity = 1000000000000000000000
    left_instances = []
    right_instances =[]
    for attrib in attributes:
        counter_true= 0
        counter_false= 0
        true_instance= []
        false_instance  = []
        for index, row in pd.DataFrame(list_instance).iterrows():
            if row[attrib] == 1:
                true_instance.append(row)
                # print("t")
                counter_true +=1
            else:
                false_instance.append(row)
                # print("F")
                counter_false +=1

        weight_true = float(counter_true)/len(list_instance)
        weight_false = 1 - weight_true
        impurity_left = weight_true * impurity_cal(true_instance)
        impurity_right = weight_false * impurity_cal(false_instance)
        impurity = impurity_left + impurity_right # the weighted impurity that sum up both branches
        if impurity <= lowest_impurity:
            bestAttr = attrib
            lowest_impurity = impurity
            left_instances = true_instance
            right_instances = false_instance
    return bestAttr,left_instances, right_instances,lowest_impurity


def impurity_cal(instance_list):
    # print("-----------------")
    # print(len(instance_list))
    global  counter_live
    global counter_die
    counter_live = 0
    counter_die = 0
    if len(instance_list)==0:
        return 0
    for t in instance_list:
        if t['class_label'] == "live":
            counter_live+=1
        else:
            counter_die+=1
    brunch_impurity = float(counter_live) * float(counter_die) / (len(instance_list)**2)

    return brunch_impurity


def build_tree(instance_list, attri_list):
    if len(instance_list) == 0:
        return Leaf(dominate_label, dominate_prob,len(instance_list))

    if len(attri_list) == 0:
        counter_live = 0
        counter_die = 0
        for ins in instance_list:
            if ins['class_label'] == "live":
                counter_live+=1
            else:
                counter_die+=1
        if counter_live>= counter_die:
            prob = float(counter_live)/len(instance_list)
            return Leaf("live",prob,len(instance_list))
        else:
            prob = float(counter_die)/len(instance_list)
            return Leaf("die",prob,len(instance_list))

    bestAttr, left_instances, right_instances, lowest_impurity = impurity_selection(attri_list, instance_list)

    if lowest_impurity == 0:
        if(len(left_instances))==0:
            return Leaf(pd.DataFrame(right_instances).iloc[0]['class_label'], 1,instance_left=len(right_instances))
        else:
            return Leaf(pd.DataFrame(left_instances).iloc[0]['class_label'],1,instance_left=len(left_instances))
    else:
        new_attr_list = copy.copy(attri_list)
        new_attr_list.remove(bestAttr)
        left = build_tree(left_instances, new_attr_list)
        right = build_tree(right_instances, new_attr_list)
    return Node(bestAttr, left, right)


def classifier(test, tree):
    correct = 0
    baselinecorrect =0
    other_label=""
    # used for the baseline predictions
    if dominate_label == "live":
        other_label = "die"
    else:
        other_label = "live"
    node = tree
    for index,instance in pd.DataFrame(test).iterrows():
        while isinstance(node, Node) :
            if instance[node.bestAtt] == 1:
                node = node.left
            else:
                node = node.right
        if instance['class_label'] == node.label:
            correct += 1
            if node.label == dominate_label:
                baselinecorrect += 1
        node = tree
    accuracy = float(correct) / float(len(test)) * 100
    baseline_accuracy = float(baselinecorrect) / float(len(test)) * 100
    print("Read: {} instances".format(len(test)))
    print("Baseline class is: " + dominate_label)
    count =0
    if dominate_label=="live":
        count = counter_live

    else:
        count = counter_die
        # print("-----------------------_++++++++++++++++-----------")
        # print(count)
    # print("{}: {} correct out of {}".format(dominate_label, baselinecorrect,count))
    # print("{}: {} correct out of {}".format(other_label, correct - baselinecorrect, len(test)-count))
    print("Accuracy: {:.2f}%".format(accuracy))
    # print("Baseline Accuracy: {:.2f}%".format(baseline_accuracy))
    return accuracy


def main():
    number_of_classes = 2  # live or die
    training_path = "hepatitis-training.dat"
    training_x, training_y, attri = read_file(training_path)
    attri_training= list(attri)
    testing_path = "hepatitis-test.dat"
    training_x = pre_processing(training_x)
    # print(len(training_x))
    tree = build_tree(training_x,attri_training)
    tree.report("")
    accuarcy = classifier(pd.DataFrame(training_x), tree)
    print("****accuracy : ", accuarcy)
    test_x, test_y, attri_test = read_file(testing_path)
    baseline_acc =0
    baseline_correct = 0
    for y in test_y:
        if y =="live":
            baseline_correct+=1
    baseline_acc = float(baseline_correct) / len(test_y)
    test_x = pre_processing(test_x)
    test_acc = classifier(pd.DataFrame(test_x),tree)
    print("test Acc : " , test_acc)
    print("baseline ACC :" ,baseline_acc)
    acc_list =[]
    for i in range(1,10):
        print("The index of the dataset pair we are using is :", i)
        train_path = "hepatitis-training-run0" + str(i) + ".dat"
        training_x, training_y, attri = read_file(train_path)
        test_path = "hepatitis-test-run0" + str(i) + ".dat"
        test_x, test_y, attri_test = read_file(test_path)
        training_x = pre_processing(training_x)
        tree = build_tree(training_x, attri_training)
        test_x = pre_processing(test_x)
        test_acc = classifier(pd.DataFrame(test_x), tree)
        acc_list.append(test_acc)
    print("The index of the dataset pair we are using is :", 10)
    train_10 = "hepatitis-training-run10.dat"
    training_x, training_y, attri = read_file(train_10)
    test_10 = "hepatitis-test-run10.dat"
    test_x, test_y, attri_test = read_file(test_10)
    training_x = pre_processing(training_x)
    tree = build_tree(training_x, attri_training)
    test_x = pre_processing(test_x)
    test_acc = classifier(pd.DataFrame(test_x), tree)
    acc_list.append(test_acc)
    print("The averahe of these 10 training-test pairs is : ",mean(acc_list))


if __name__ == '__main__':
    main()
