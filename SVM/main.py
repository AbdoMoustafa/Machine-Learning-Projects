import sklearn
from sklearn import datasets
from sklearn import svm
from sklearn import metrics

cancer = datasets.load_breast_cancer()  # Loading in data

x = cancer.data
y = cancer.target  # Data to be predicted : ['malignant', 'benign'] based on x

x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(x, y, test_size=0.2)  # Training with
# random 20% of data

classifier = svm.SVC(kernel="linear", C=2)  # Creating our SVM classifier w/ a linear kernel and a soft margin of 2
classifier.fit(x_train, y_train)

prediction = classifier.predict(x_test)  # Predicting based on our x_test (20% of the data)
accuracy = metrics.accuracy_score(y_test, prediction)  # Accuracy is prediction vs actual result

print(accuracy)
