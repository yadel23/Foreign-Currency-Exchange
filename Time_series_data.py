import requests, os
import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from sqlalchemy import create_engine
import plotly.graph_objects as go
import datetime

#Ensuring users take input from accepted symbols
def symbols_json():
    url_symbols = 'https://api.exchangerate.host/symbols'
    response = requests.get(url_symbols)
    data = response.json()
    return data


def symbols_dic(symbols_data):
    symbols ={}
    for key, value in symbols_data['symbols'].items():
          symbols[value['code'].upper()] = value['description'].lower()
    return symbols

#Gathering Input
def gatherInput(symbols):
  
  while True:
    start_date = input("Please enter the start date in the format, YYYY-MM-DD: \n")
    s_date = start_date.split("-", 3)
    if s_date[0].isnumeric() and s_date[1].isnumeric() and s_date[2].isnumeric():
      d1 = datetime.datetime(int(s_date[0]), int(s_date[1]), int(s_date[2]))
    if type(start_date) == str and len(start_date) == 10:
      break
    else:
      print("Invalid input, please try again. \n")
      continue
  
  while True:
    end_date = input("Please enter the end date in the format, YYYY-MM-DD: \n")
    e_date = end_date.split("-", 3)
    d2 = datetime.datetime(int(e_date[0]), int(e_date[1]), int(e_date[2]))
  
    if d2 > d1 and len(end_date) == 10:
      break
    else:
      print("Invalid input, please try again. \n")
      continue
  
  while True:
    currency = input("Please enter the currency you would like to view data on: \n")
    if type(currency) == str and currency.upper() in symbols.keys():
      break
    else:
      print("Invalid input, please try again. \n")
      continue
      
  return start_date, end_date, currency

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
def savetoDatabase(df, engine, filename, table_name, database_name):
  df.to_sql(table_name, con=engine, if_exists='replace', index=False)
  os.system('mysqldump -u root -pcodio '+database_name+' > '+ filename)

#The main function
def main():
  database_name = "history"
  filename = "time_series.sql"
  table_name = 'currency_history'
  base_url = 'https://api.exchangerate.host/'
  symbols_data = symbols_json()
  symbols = symbols_dic(symbols_data)
  start_date, end_date, currency, = gatherInput(symbols)
  engine = createDatabase(database_name, filename)
  data = buildUrl(base_url, start_date, end_date)
  df = buildDataframe(data, currency)
  linePlot(df, currency, start_date, end_date)
  savetoDatabase(df, engine, filetable_name, table_name, database_name)
  
main()