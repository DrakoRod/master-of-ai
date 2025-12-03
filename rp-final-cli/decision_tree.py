import kagglehub
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from io import StringIO
from IPython.display import Image
from sklearn.tree import export_graphviz
import pydotplus


def train_decision_tree():
    data_path = kagglehub.dataset_download("uciml/pima-indians-diabetes-database")
    print(f"Training decision tree model with data from: {data_path}")

    print("\n-------------- Data Info -----------\n")
    df = pd.read_csv(f'{data_path}/diabetes.csv')
    df.info()
    print("\n-------------- Data Info -----------\n")

    df.shape
    df.describe()

    df['Outcome'].value_counts()

    df.groupby('Outcome').mean()

    X=df.drop(columns='Outcome',axis=1)
    Y=df['Outcome']
    print(X)

    features= ['Pregnancies','Glucose','BloodPressure','SkinThickness', 'Insulin','BMI','DiabetesPedigreeFunction', 'Age']

    #data standardization
    scaler= StandardScaler()
    scaler.fit(X)
    standardized_data=scaler.transform(X)
    X=standardized_data
    print(X)

    #data test and train
    X_train,X_test,Y_train,Y_test=train_test_split(X,Y,test_size=0.2,stratify=Y,random_state=2)

    print(X.shape,X_train.shape,X_test.shape)

    ## Training the model
    classifier=DecisionTreeClassifier(criterion="entropy", max_depth=4)
    classifier.fit(X_train,Y_train)
    #model evaluation
    predicted_value=classifier.predict(X_train)
    train_accuracy=accuracy_score(predicted_value,Y_train)

    print("Decision Tree Train Accuracy: ")
    print(train_accuracy)

    test_predicted_value=classifier.predict(X_test)
    test_accuracy=accuracy_score(test_predicted_value,Y_test)

    #decision tree
    print("Decision Tree Test Accuracy: ")
    print(test_accuracy)

    dot_data = StringIO()
    export_graphviz(classifier,out_file=dot_data,filled=True, rounded=True,special_characters=True, feature_names = features,class_names=['0','1'])
    graph = pydotplus.graph_from_dot_data(dot_data.getvalue())
    Image(graph.create_png())
    graph.write_png("diabetes_decision_tree.png")
    print("Decision tree saved as 'diabetes_decision_tree.png'")