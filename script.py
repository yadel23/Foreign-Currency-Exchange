import requests

url_symbols = 'https://api.exchangerate.host/symbols'
response = requests.get(url_symbols)
data = response.json()

symbols ={}
for key, value in data['symbols'].items():
      symbols[value['description'].lower()] = value['code'].upper()

base_url = 'https://api.exchangerate.host/'


amount = input("please enter the amount you would like to exchange?\n")
from_currency = input('please enter the currency?\n')
to_currency = input('Please enter the currency you would like to exchange to?\n')

for key, value in symbols.items():
   if from_currency.upper() == value :
      from_currency = from_currency.upper()     
      
   if to_currency.upper() == value:
      to_currency = to_currency.upper()
        
full_url = base_url + 'convert?from=' + from_currency + '&to=' + to_currency
response_2 = requests.get(full_url)
data_2 = response_2.json()

final_amount = 0
rate = 0
for key, value in data_2['info'].items():
    rate = value
    
final_amount = float(rate) * float(amount)
print(f'Your final amount is  {final_amount}  {to_currency}')

   

   







