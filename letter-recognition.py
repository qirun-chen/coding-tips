from mlp import MLP
import numpy as np
import csv


def to_c(n):
    char_delta = ord('A')
    return chr(int(n) + char_delta)


dataset = list()
with open('/Users/ryan/Documents/GitHub/advanced-machine-learning/MLP/letter-recognition.csv', newline='') as data_file:
    reader = csv.reader(data_file, delimiter=',')
    for row in reader:
        row[0] = ord(row[0]) - ord('A')
        dataset.append(row)

training_split = int(len(dataset) * 0.8)

training_set = np.array(dataset[:training_split], dtype=np.int)
X = training_set[:, 1:]
y = training_set[:, 0]
test_set = np.array(dataset[training_split:], dtype=np.int)

# find a proper configuration
mlp = MLP(16, 10, 26, activation='sigmoid', learning_rate=0.3, max_epochs=1000, verbose=2)
mlp.fit(X, y)

accuracy = 0
# on test set
for row in test_set:
    prediction = mlp.predict(row[1:])
    print('Expected= %s, Output= %s' % (to_c(row[0]), to_c(prediction)))
    if int(row[0]) == int(prediction):
        accuracy += 1

print("==" * 20)
# calculate the accuracy
print("Accuracy = %.3f " % (accuracy / len(test_set)))
