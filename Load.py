# -*- coding: utf-8 -*-
"""
Created on Thu Apr 27 17:45:13 2023

@author: Mahmoud Saeed
"""
import snowflake.connector
from snowflake.connector.pandas_tools import write_pandas , pd_writer
import pandas as pd
from sqlalchemy import create_engine
from snowflake.sqlalchemy import URL

      # engine = create_engine(URL(
      #     user='*******',
      #         password='******',
      #         account='JVHMOHK-FG31247',
      #         warehouse = 'COMPUTE_WH',
      #         database = 'WEATHERDATA',
      #         schema = 'PUBLIC.DATE',
      #         role = 'ACCOUNTADMIN'
      #     )) 
      # connection = engine.connect()
      
  
class Load:
    def load_date(self, data):
  
        ctx = snowflake.connector.connect(
            user='MAHMOUDSAEED',
            password='0987654321.Ms',
            account='JVHMOHK-FG31247',
            warehouse = 'COMPUTE_WH',
            database = 'WEATHERDATA'
            # table = 'WEATHERDATA.PUBLIC.DATE'
            
            )
        cs = ctx.cursor()
        # data.shape[0]
        for i in range(data.shape[0]):
            cs.execute(" Insert Into WEATHERDATA.PUBLIC.DATE (DATE,YEAR,MONTH,QUARTER,DAY,HOUR,MINUTE)"
                    "VALUES (?,?,?,?,?,?,?) ", (str(data.iloc[i]['date']),
                                                str(data.iloc[i]['year'])
                                              ,str(data.iloc[i]['month']),
                                              str(data.iloc[i]['quarter'])
                                              ,str(data.iloc[i]['day']),
                                              str(data.iloc[i]['hour']),
                                              str(data.iloc[i]['minute'])))
        return
    def load_weather(self, data):
  
        ctx = snowflake.connector.connect(
            user='MAHMOUDSAEED',
            password='0987654321.Ms',
            account='JVHMOHK-FG31247',
            warehouse = 'COMPUTE_WH',
            database = 'WEATHERDATA'
            # table = 'WEATHERDATA.PUBLIC.DATE'
            
            )
        cs = ctx.cursor()
        # data.shape[0]
        for i in range(data.shape[0]):
            cs.execute(" Insert Into WEATHERDATA.PUBLIC.WEATHER (CITY,DATE,CONDITION,TEMP_C,WIND_DEGREE,WIND_DIR,VIS_MILES,HUMIDITY)"
                    "VALUES (?,?,?,?,?,?,?,?) ", (str(data.iloc[i]['city']),
                                                str(data.iloc[i]['date']),
                                              str(data.iloc[i]['condition']),
                                              str(data.iloc[i]['temp_c']),
                                              str(data.iloc[i]['wind_degree']),
                                              str(data.iloc[i]['wind_dir']),
                                              str(data.iloc[i]['vis_miles']),
                                              str(data.iloc[i]['humidity'])))
        return
# Load().load([])        