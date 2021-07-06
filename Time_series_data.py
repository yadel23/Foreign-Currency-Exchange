import requests, os
import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from sqlalchemy import create_engine

database_name = "history"
filename = "time_series.sql"
table_name = 'currency_history'

#Database creation
os.system('mysql -u root -pcodio -e "CREATE DATABASE IF NOT EXISTS '+database_name+';"')
os.system("mysql -u root -pcodio "+database_name+" < " + filename)
engine = create_engine('mysql://root:codio@localhost/'+database_name+'?charset=utf8', encoding='utf-8')

base_url = 'https://api.exchangerate.host/'

start_date = input("Please enter the start date in the format, YYYY-MM-DD: \n")
end_date = input("Please enter the end date in the format, YYYY-MM-DD: \n")
currency = input("Please enter the currency you would like to view the history of its rates: \n")

response = requests.get(base_url + 'timeseries?start_date=' + str(start_date) + '&end_date=' +
                       end_date)
data = response.json()
#print(data)

col_names = ["Day", "Rate"]
df = pd.DataFrame(columns = col_names)
for key, value in data['rates'].items():
    df.loc[len(df.index)] = [key, value[currency.upper()]]

df.to_sql(table_name, con=engine, if_exists='replace', index=False)
os.system('mysqldump -u root -pcodio '+database_name+' > '+ filename)

#print(df)

