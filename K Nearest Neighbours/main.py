import sklearn
from sklearn.utils import shuffle
from sklearn.neighbors import KNeighborsClassifier
from sklearn import linear_model, preprocessing
import pandas as pd
import numpy as np


def main():
    data = pd.read_csv('car.data')

    # As a lot of the data is not numeric,
    # we must convert the string data into some number, so we can use the data to train our model
    word_to_num = preprocessing.LabelEncoder()

    # Taking each column in our file, and returning array of numerical data each
    buying = word_to_num.fit_transform(list(data["buying"]))
    maint = word_to_num.fit_transform(list(data["maint"]))
    door = word_to_num.fit_transform(list(data["door"]))
    persons = word_to_num.fit_transform(list(data["persons"]))
    lug_boot = word_to_num.fit_transform(list(data["lug_boot"]))
    safety = word_to_num.fit_transform(list(data["safety"]))
    clss = word_to_num.fit_transform(list(data["class"]))

    x = list(zip(buying, maint, door, persons, lug_boot, safety))  # Recombining data into a list w/ .zip()
    y = list(clss)  # The variable to be predicted

    x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(x, y, test_size=0.2)  # Training with
    # random 20% of data
    model = KNeighborsClassifier(n_neighbors=7)  # Specifying how many neighbours the model should look for

    model.fit(x_train, y_train)  # Training our model
    accuracy = model.score(x_test, y_test)  # Calculating accuracy of predictions
    print(accuracy)

    # Testing the performance & analysing the accuracy of the model
    predicted = model.predict(x_test)
    names = ["unacc", "acc", "good", "vgood"]

    for x in range(len(predicted)):
        print(f"Data: {x_test[x]}    Actual : {names[y_test[x]]}     Prediction : {names[predicted[x]]}")


# Code inspired by Tech With Tim on YouTube

if __name__ == '__main__':
    main()
