from pprint import pprint

from django.shortcuts import render
import requests
# Create your views here.
from rest_framework.generics import ListAPIView
from sklearn.linear_model import LinearRegression

from polls.models import Weather
from .serializers import WeatherSerializers
from polls.date import getData, dictionare
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split


def predictii(dataframe, col):
    weather_y = dataframe.pop(col)  # am pus parametrul col pentru a face predictii pe ce coloana se doreste
    # numele coloanei se ia din models.py eg. "airTemperature"
    weather_x = dataframe
    # splituirea datelor in train si test
    train_X, test_X, train_Y, test_Y = train_test_split(weather_x, weather_y, test_size=0.3, random_state=4)

    model = LinearRegression()
    model.fit(train_X, train_Y)
    prediction = model.predict(test_X)

    np.mean((prediction - test_Y) ** 2)
    #am construit resultatul cu predictia pe care l vom afisa mai jos
    result = pd.DataFrame(
        {
            "test": test_Y,
            "prediction": prediction,
            "diferenta": (test_Y - prediction)
        }
    )
    print(result)


class WeatherListView(ListAPIView):
    queryset = Weather.objects.all()
    serializer_class = WeatherSerializers
    # getData()
    #am comentat functia getData pentru a nu mi pune de fiecare data cand rulez cu runserver datele luate in consola
    dictionarylist = []
    for i in queryset:
        dictionarylist.append(i.dictionar())#am creat un dictionar pentru date
    dataframe = pd.DataFrame(dictionarylist)
    print(dataframe)#afisam tabelul cu datele
    predictii(dataframe, "airTemperature")#afisam tabelul cu predictiile
