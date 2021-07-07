import requests, os
import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from sqlalchemy import create_engine
import plotly.graph_objects as go

#Database creation
def createDatabase(database_name, filename):
  os.system('mysql -u root -pcodio -e "CREATE DATABASE IF NOT EXISTS '+database_name+';"')
  os.system("mysql -u root -pcodio "+database_name+" < " + filename)
  engine = create_engine('mysql://root:codio@localhost/'+database_name+'?charset=utf8', encoding='utf-8')
  return engine

#Parsing json
def buildUrl(base_url, start_date, end_date):
  response = requests.get(base_url + 'timeseries?start_date=' + str(start_date) + '&end_date=' +
                         end_date)
  data = response.json()
  return data

#Building panda dataframe
def buildDataframe(data, currency):
  col_names = ["Day", "Rate"]
  df = pd.DataFrame(columns = col_names)
  for key, value in data['rates'].items():
      df.loc[len(df.index)] = [key, value[currency.upper()]]
  return df

#Line plot
def linePlot(df, currency, start_date, end_date):
  fig = go.Figure([go.Scatter(x=df['Day'], y=df['Rate'])])
  fig.update_layout(title = f'Change in {currency} rates from {start_date} to {end_date}') 
  fig.write_html("line.html")
  

#Saving data into database
def savetoDatabase(engine, table_name, database_name):
  df.to_sql(table_name, con=engine, if_exists='replace', index=False)
  os.system('mysqldump -u root -pcodio '+database_name+' > '+ filename)

#The main function
def main():
  database_name = "history"
  filename = "time_series.sql"
  table_name = 'currency_history'
  engine = createDatabase(database_name, filename)
  base_url = 'https://api.exchangerate.host/'
  start_date = input("Please enter the start date in the format, YYYY-MM-DD: \n")
  end_date = input("Please enter the end date in the format, YYYY-MM-DD: \n")
  currency = input("Please enter the currency you would like to view the history of its rates: \n")
  data = buildUrl(base_url, start_date, end_date)
  df = buildDataframe(data, currency)
  linePlot(df, currency, start_date, end_date)
  
main()