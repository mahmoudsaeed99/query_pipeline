# -*- coding: utf-8 -*-
"""
Created on Thu Apr 27 00:43:45 2023

@author: Mahmoud Saeed
"""
from Extract import Extract
from Transform import Transform
from Load import Load

def pipeline():
    try:
        weather = Extract().extract_csv()
        
        weather , date = Transform().transform(weather)
        # weather.to_csv("weather.csv")
        # date.to_csv("date.csv")
        Load().load_date(date)
        Load().load_weather(weather)
        # print(weather)
            
    except Exception as e:
        print("error ",e)
        
pipeline()       