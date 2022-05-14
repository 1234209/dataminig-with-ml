from logisticmodule import *
from linearregression import *
select=0
while select!='1' and select!='2':
    print("pick a linear model")
    print("1.linear regression model")
    print("2.logistic regression model")
    select=input("enter 1 or 2: ")
    if select!='1' and select!='2':
        print("please select enter 1 or 2")

if select=='1':
    linear()
elif select=='2':
    logistic()


