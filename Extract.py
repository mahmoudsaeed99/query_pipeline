# -*- coding: utf-8 -*-
"""
Created on Wed Apr 26 01:09:46 2023

@author: Mahmoud Saeed
"""
import pandas as pd
import requests


# url = "https://weatherapi-com.p.rapidapi.com/current.json"

# querystring = {"q":"30.0444,31.2358"}

# headers = {
# 	"content-type": "application/octet-stream",
# 	"X-RapidAPI-Key": "###################################",
# 	"X-RapidAPI-Host": "weatherapi-com.p.rapidapi.com"
# }

# response = requests.get(url, headers=headers, params=querystring)

# print(response.json())


class Extract :
    url = "https://weatherapi-com.p.rapidapi.com/current.json"

    # __querystring = {"q":"53.1,-0.13"}

    headers = {
    	"content-type": "application/octet-stream",
    	"X-RapidAPI-Key": "#######################################################",
    	"X-RapidAPI-Host": "weatherapi-com.p.rapidapi.com"
    }
    
    def extract_csv(self):
        cities = pd.read_csv('cities.csv')
        data_json = []
        # 
        for i in range(cities.shape[0]):
            lat = cities.iloc[i]['lat']
            long = cities.iloc[i]['long']
            query = ""+str(lat)+","+str(long)+""
            query= {"q":query}
            # print(query)
            response = requests.get(self.url,headers=self.headers,
                                    params= query)        
            
            data_json.append(response.json())
        return data_json

      
