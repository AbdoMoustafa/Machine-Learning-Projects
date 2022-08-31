import pandas as pd
import numpy as np
import sklearn
from sklearn import linear_model
import matplotlib.pyplot as pyplot
from matplotlib import style
import pickle


def main():
    data = pd.read_csv('student-mat.csv', sep=';')  # Delimiter to separate data
    data = data[["G1", "G2", "G3", "studytime", "failures", "absences", "freetime"]]  # Collecting useful data from file

    predict = "G3"  # G3 = Final Grade, the variable we're trying to predict

    x = np.array(data.drop([predict], 1))  # All data that will be trained to predict G3
    y = np.array(data[predict])  # Data to be predicted

    x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(x, y,
                                                                                test_size=0.20)  # Training with
    # random 20% of data

    most_accurate = 0

    for _ in range(1000):
        x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(x, y, test_size=0.20)

        linear = linear_model.LinearRegression()
        linear.fit(x_train, y_train)

        accuracy = linear.score(x_test,
                                y_test)  # Comparing predictions w/ actual results to get the accuracy of our model

        if accuracy > most_accurate:  # Saving the most accurate model to a file
            most_accurate = accuracy
            with open("linear-model.pickle", "wb") as f:
                pickle.dump(linear, f)
                print(f"Accuracy of predictions (%) : {most_accurate}")

    file_data = open("linear-model.pickle", "rb")
    linear = pickle.load(file_data)

    predictions = linear.predict(x_test)
    for x in range(len(predictions)):  # Representing predictions vs actual results
        print(f"Input Data : {x_test[x]}    Predicted Grade : {predictions[x]}      Actual Grade : {y_test[x]}")

    x_axis = 'G1'  # Plotting predictions against G1
    plot(data, x_axis, predict)


# Illustration via scatter plot
def plot(data, x_axis, predict):
    style.use("ggplot")
    pyplot.scatter(data[x_axis], data[predict])
    pyplot.xlabel(x_axis)
    pyplot.ylabel("Final Grade")
    pyplot.show()


# Code inspired by Tech With Tim on YouTube

if __name__ == '__main__':
    main()
