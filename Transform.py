# -*- coding: utf-8 -*-
"""
Created on Wed Apr 26 20:33:47 2023

@author: Mahmoud Saeed
"""

import requests
import pandas as pd

class Transform:
    
    def transform_date(self , df):
        df['date'] = pd.to_datetime(df['date'])
        # print(type(df))
        df['year'] = df['date'].dt.year
        df['month'] = df['date'].dt.month_name()
        df['quarter'] = df['date'].dt.quarter
        df['day'] = df['date'].dt.day_name()
        df['hour'] = df['date'].dt.hour
        df['minute'] = df['date'].dt.minute
        return df
    
    def transform(self , data):
        city = []
        # region = []
        # country = []
        # lat = []
        # long = []
        last_update = []
        temp_c = []
        condition = []
        wind_degree = []
        wind_dir = []
        vis_miles = []
        humidity = []
        # print("1")
        for i in data:
            city.append(i['location']['name'])
            # region.append(i['location']['region'])
            # country.append(i['location']['country'])
            # lat.append(i['location']['lat'])
            # long.append(i['location']['long'])
            last_update.append(i['current']['last_updated'])
            temp_c.append(i['current']['temp_c'])
            wind_degree.append(i['current']['wind_degree'])
            wind_dir.append(i['current']['wind_dir'])
            humidity.append(i['current']['humidity'])
            vis_miles.append(i['current']['vis_miles'])
            condition.append(i['current']['condition']['text'])
            
        # print(2)
        weather_data = pd.DataFrame({'city':city,"date":last_update,'condition':condition,'temp_c':temp_c,
                                     'wind_degree':wind_degree,'vis_miles':vis_miles,
                                     'wind_dir':wind_dir,'humidity':humidity})  
        # print(type(weather_data))
        last_update = list(set(last_update))
        # print(4)
        date_data = pd.DataFrame({"date":last_update})
        # print(type(date_data))
        date_data = self.transform_date(date_data)
        # print(weather_data.head(1))
        # print(date_data.head(1))
        return weather_data , date_data
        
            
            