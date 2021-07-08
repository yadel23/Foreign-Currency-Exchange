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
    start_date = input("\nPlease enter the start date in the format, YYYY-MM-DD: \n")
    isValidDate = True
    isValidFormat = True
    try:
      datetime.datetime.strptime(start_date, '%Y-%m-%d')
    except ValueError:
        isValidFormat = False
    if isValidFormat:
      s_date = start_date.split("-", 3)
      year = s_date[0]
      month = s_date[1]
      day = s_date[2]
      if year.isnumeric() and month.isnumeric() and day.isnumeric():
        try:
          d1 = datetime.datetime(int(year), int(month), int(day))
        except ValueError:
          isValidDate = False
        if isValidDate:
          break
    else:
      print("Invalid input, please try again. \n")
      continue
      
  while True:
    end_date = input("\nPlease enter the end date in the format, YYYY-MM-DD: \n")
    isValidDate1 = True
    isValidFormat1 = True
    try:
      datetime.datetime.strptime(end_date, '%Y-%m-%d')
    except ValueError:
        isValidFormat1 = False
    if isValidFormat1:
      s_date1 = end_date.split("-", 3)
      year1 = s_date1[0]
      month1 = s_date1[1]
      day1 = s_date1[2]
      if year1.isnumeric() and month1.isnumeric() and day1.isnumeric():
        try:
          d2 = datetime.datetime(int(year1), int(month1), int(day1))
        except ValueError:
          isValidDate1 = False
        if isValidDate1 and d2 > d1:
            break
        else:
          print("Invalid input, please try again. \n")
          continue
    else:
      print("Invalid input, please try again. \n")
      continue
  
  while True:
    currency_list = []
    isValid = True
    try:
      cur_number = eval(input("How many currency(ies) would you like to compare rates (from 1 to 5): \n"))
    except:
      isValid = False 
    if isValid:
      if type(cur_number) == int and cur_number >=1 and cur_number <= 5 or type(cur_number) == float:
        break
      else:
        print("Invalid input, please try again. \n")
        continue
    else:
      print("Invalid input, please try again. \n")
      continue
    
  i = 1
  while i <= cur_number:
    currency = input(f'\n{i}. Enter a currency to compare: ') 
    if type(currency) == str and currency.upper() in symbols.keys() and currency not in currency_list:
      currency_list.append(currency)
      i += 1
      continue
    else:
      print("Invalid input, please try again. \n")
      continue
    
        
  print(currency_list)
      
  return start_date, end_date, currency_list

#Database creation
def createDatabase(database_name, filetable_name):
  os.system('mysql -u root -pcodio -e "CREATE DATABASE IF NOT EXISTS '+database_name+';"')
  os.system("mysql -u root -pcodio "+database_name+" < " + filetable_name)
  engine = create_engine('mysql://root:codio@localhost/'+database_name+'?charset=utf8', encoding='utf-8')
  return engine

#Parsing json 
def buildUrl(base_url, start_date, end_date):
  response = requests.get(base_url + 'timeseries?start_date=' + str(start_date) + '&end_date=' +
                         end_date)
  data = response.json()
  return data

#Building panda dataframe
def buildDataframe(data, currency_list):
  for currency in currency_list:
    col_names = [currency, "Day", "Rate"]
    df = pd.DataFrame(columns = col_names)
    for key, value in data['rates'].items():
      df.loc[len(df.index)] = [currency, key, value[currency.upper()]]
  print(df)         
  return df

#Line plot
def linePlot(df, currency_list, start_date, end_date):
  fig = go.Figure([go.Scatter(x=df['Day'], y=df['Rate'])])
  fig.update_layout(title = f'Change in {currency_list} rates from {start_date} to {end_date}') 
  fig.write_html("line.html")
  

#Saving data into database
def savetoDatabase(df, engine, filetable_name, table_name, database_name):
  df.to_sql(table_name, con=engine, if_exists='replace', index=False)
  os.system('mysqldump -u root -pcodio '+database_name+' > '+ filetable_name)

#The main function
def main():
  database_name = "history"
  filetable_name = "time_series.sql"
  table_name = 'currency_history'
  base_url = 'https://api.exchangerate.host/'
  symbols_data = symbols_json()
  symbols = symbols_dic(symbols_data)
  start_date, end_date, currency_list, = gatherInput(symbols)
  engine = createDatabase(database_name, filetable_name)
  data = buildUrl(base_url, start_date, end_date)
  df = buildDataframe(data, currency_list)
  #linePlot(df, currency_list, start_date, end_date)
  savetoDatabase(df, engine, filetable_name, table_name, database_name)
  
main()