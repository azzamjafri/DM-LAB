DATASET = [
    ['Rainy', 'Hot', 'High', 'FALSE', 'No'],
    ['Rainy', 'Hot', 'High', 'TRUE', 'No'],
    ['Overcast', 'Hot', 'High', 'FALSE', 'Yes'],
    ['Sunny', 'Mild', 'High', 'FALSE', 'Yes'],
    ['Sunny', 'Cool', 'Normal', 'FALSE', 'Yes'],
    ['Rainy', 'Mild', 'Normal', 'TRUE', 'Yes'],
    ['Overcast', 'Mild', 'High', 'TRUE', 'Yes'],
    ['Overcast', 'Hot', 'Normal', 'FALSE', 'Yes'],
    ['Sunny', 'Mild', 'High', 'TRUE', 'No'],
]

TEST = [
    ['Sunny', 'Cool', 'Normal', 'TRUE'],
    ['Overcast', 'Cool', 'Normal', 'TRUE'],
    ['Rainy', 'Mild', 'High', 'FALSE'],
    ['Rainy', 'Cool', 'Normal', 'FALSE'],
    ['Sunny', 'Mild', 'Normal', 'FALSE'],
]

TEST_RESULT = [
    'No',
    'Yes',
    'No',
    'Yes',
    'Yes',
]


def count_y_labels(dataset, count_var):
    """
    Counts the number of Y labels in the given dataset
    """
    count_var['total_data'] = len(dataset)
    for row in dataset:
        if(row[-1] in count_var):
            count_var[row[-1]] += 1
        else:
            count_var[row[-1]] = 1
    # print(count_var)


def count_x_labels(dataset, count_var):
    """
    Counts the X labels per y labels
    """
    for row in dataset:
        if(row[-1] not in count_var):
            count_var[row[-1]] = {}
        for data in row[0:-1]:
            if(data not in count_var[row[-1]]):
                count_var[row[-1]][data] = 1
            else:
                count_var[row[-1]][data] += 1

    # print(count_var)


def runModel(y_count, x_count, test_data):
    result_set = []

    # calculate probabilities for each class
    for row in test_data:
        interim_results = {}

        # get the initial probability for every class
        for x in y_count.keys():
            if(x == 'total_data'):
                continue
            interim_results[x] = [
                y_count[x] / y_count['total_data']]

            for data in row:
                # missing key
                if(data not in x_count[x]):
                    interim_results[x].append(0)
                    continue
                interim_results[x].append(
                    x_count[x][data]/y_count[x])

        # print(interim_results)
        final_result = {}
        for data in interim_results.keys():
            final_result[data] = 1
            for arr in interim_results[data]:
                final_result[data] *= arr
         ## END

        print(final_result)
        tempValue = 0
        answer_class = ''
        for x in final_result.keys():
            if(final_result[x] > tempValue):
                tempValue = final_result[x]
                answer_class = x

        result_set.append(answer_class)

    return result_set

    # for row in test_data:


y_count = {}
x_count = {}

count_y_labels(DATASET, y_count)
count_x_labels(DATASET, x_count)
test_result = runModel(y_count, x_count, TEST)

accuracy = 0
for i in range(0, len(test_result)):
    if(TEST_RESULT[i] == test_result[i]):
        accuracy += 1
accuracy /= len(test_result)

print("Model op:" + str(test_result))
print("Actual op:" + str(TEST_RESULT))
print("Accuracy: "+ str(accuracy))