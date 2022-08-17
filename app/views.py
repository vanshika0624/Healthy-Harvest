from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect,HttpRequest,JsonResponse
from django.urls import reverse
from .models import *
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import accuracy_score
import cv2
from .color_histogram_feature_extraction import *
from  .knn_classifier import *
import os
import os.path
from .color_classification_webcam import *



def index(request):
    return render(request,'index.html',{})



def predictcrop(request):
    data=pd.read_csv('./app/cpdata.csv')
    print(data.head(1))
    label= pd.get_dummies(data.label).iloc[: , 1:]
    data= pd.concat([data,label],axis=1)
    data.drop('label', axis=1,inplace=True)
    print('The data present in one row of the dataset is')
    print(data.head(1))
    print("\n\n\n\n")
    train=data.iloc[:, 0:4].values
    test=data.iloc[: ,4:].values
    X_train,X_test,y_train,y_test=train_test_split(train,test,test_size=0.3)
    sc = StandardScaler()
    X_train = sc.fit_transform(X_train)
    X_test = sc.transform(X_test)
    clf=DecisionTreeRegressor()
    clf.fit(X_train,y_train)
    pred=clf.predict(X_test)
    a=accuracy_score(y_test,pred)
    print("The accuracy of this model is: ", a*100)
    crops=['wheat','mungbean','Tea','millet','maize','lentil','jute','cofee','cotton','ground nut','peas','rubber','sugarcane','tobacco','kidney beans','moth beans','coconut','blackgram','adzuki beans','pigeon peas','chick peas','banana','grapes','apple','mango','muskmelon','orange','papaya','watermelon','pomegranate']
    cr='rice'
    l=[]
    temperature = float(request.GET['temperature'])
    humidity = float(request.GET['humidity'])
    rainfall = float(request.GET['rainfall'])
    pH = float(request.GET['pH'])
    l.append(temperature)
    l.append(humidity)
    l.append(rainfall)
    l.append(pH)
    predictcrop=[l]
    predictions = clf.predict(predictcrop)
    count=0
    for i in range(0,30):
        if(predictions[0][i]==1):
            c=crops[i]
            count=count+1
            break;
        i=i+1
    if(count==0):
        return HttpResponse("0")
    else:
        print(c)
        return HttpResponse(c)


def videoleaf(request):
    startwebcam()
    return HttpResponse()
