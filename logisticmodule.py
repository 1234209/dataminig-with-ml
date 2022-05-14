import pandas as pd
from sklearn.linear_model import LogisticRegression
def logistic():
    #taking input
    input("upload a csv file with training data into the folder (press enter to continue)")
    data= pd.read_csv(input("enter name of the file: "))   #data.csv

    #splitting input
    req = input("enter the required attribute: ")   #Purchased
    y=data[req]
    data.drop([req], axis=1, inplace=True)

    #training model
    model = LogisticRegression()
    model.fit(data, y)

    #output

    input("upload a csv file with inputs (press enter to continue)")
    pred = pd.read_csv(input("enter name of the file: "))   #sample.csv
    print(" predicted value of "+req+" is: "+model.predict(pred))

