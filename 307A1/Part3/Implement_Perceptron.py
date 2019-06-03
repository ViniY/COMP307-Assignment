import numpy as np
np.random.seed(307)


class Feature:
    def __init__(self, row, col, sgn):
        self.row = row
        self.col = col
        self.sgn = sgn

    def __str__(self):
        """ a string representing the Feature"""
        return "(row: {0}, col: {1}, sgn: {2})".format(
        self.row, self.col, self.sgn)


class Image:
    def __init__(self,width,height,label,data):
        self.height = height
        self.width = width
        self.label = label
        self.data = data

    def __str__(self):
        return "width:{0},height:{1},label:{2}".format(self.width,self.height,self.label)


def readFile(path):
    inputfile = open(path)
    data = inputfile.readlines()
    inputfile.close()
    return data


def serialize_as_image(data):
    image_list = []
    # line 0 P1
    # line 1 class label
    # line 2 size
    # line 3&4 0-1 numbers representing the graph
    for index in range(100): # 100 images data
        label = data[index*5 +1]
        size = data[index*5+2]
        width,height = size.split()
        width = int(width)
        height = int(height)
        image_line4 = data[index*5+3]
        image_line5 = data[index*5+4]
        image_data = str(image_line4)+str(image_line5)
        image_c = []
        for i in range(len(image_data)):
            if image_data[i] != '\n':
                image_c.append(int(image_data[i]))
        image_data = image_c

        # print(image_data)
        image = Image(width,height,label,image_data)
        image_list.append(image)
    # a image list that has been serialized
    return image_list


def initial_feature(length):
    counter = 0
    # print("Random features are :")
    features = []
    for i in range(length):
        row = []
        col = []
        sgn = []
        for j in range(4):
            row.append(np.random.randint(0, 10))
            col.append(np.random.randint(0, 10))
            sgn.append(np.random.randint(0, 2))
        feature = Feature(row, col, sgn)
        features.append(feature)
        counter+=1
        print(counter,"th :",feature)
    return features


def intial_weight(length):
    print("Initial weight set is:")
    total = length +1  # plus cuz by the bias
    weight_list = []
    for i in range(total):
        weight_list.append(np.random.uniform(0, 1))
    print(weight_list)
    return weight_list


def construct_vectors(image_list, feature_list):
    feeding_list = []
    for image in image_list:
        width = image.width
        height = image.height
        vector= [1]
        for feature in feature_list:
            value = selector_value(image,feature)
            vector.append(value)
            # print(type(image.label))
            if "#X" in image.label:
                # print("enter if")
                y = 1
            else:
                y = 0
        feeding_list.append((vector, y))

    return feeding_list


# check three of the four pixels, if we get three correct then return 1 else return 0 which will be used as the input
def selector_value(image,feature):
    summation = 0
    for index in range(4):
        a = feature.row[index]
        b = feature.col[index]
        index_in_image = a * image.width + b
        if int(image.data[index_in_image]) == feature.sgn[index]:
            summation += 1
    if summation >= 3:
        value = 1
    else:
        value = 0
    return value


def simple_perceptron(input_list, weight_list, m):
    k = 0
    hits = 0
    while k < m and hits < 100:
        hits = 0
        for vector in input_list:
            true_label = vector[1]
            summation = 0
            for i in range(51):
                summation += vector[0][i] * weight_list[i]

            if summation > 0:
                predict = 1
            else:
                predict = 0
            # print(predict)
            #
            # print(true_label)
            # print("-------------------------------------")
            if predict == true_label:
                hits += 1
                # print(hits)
            else:
                for i in range(51):
                    # change the weights for each nodes and bias
                    weight_list[i] += (vector[1] - predict) * vector[0][i]
        k += 1

    print("After {} times learning, the matched number of image is {}:".format(k, hits))
    print("Final weight set is:")
    print(weight_list)



def main():
    data_path = "image.data"
    data = readFile(data_path)
    length_features = 50
    # print(type(data))
    # print(len(data))
    image_list = serialize_as_image(data)


    # print("************************************")
    # print(len(image_list[0].data))
    list_weight = intial_weight(length_features)
    list_feature = initial_feature(length_features)
    feed_list = construct_vectors(image_list,list_feature)
    m = 250
    simple_perceptron(feed_list, list_weight, m)

if __name__ == '__main__':
    main()
