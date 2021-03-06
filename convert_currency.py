import requests

def symbols_json():
    url_symbols = 'https://api.exchangerate.host/symbols'
    response = requests.get(url_symbols)
    data = response.json()
    return data


def symbols_dic(data):
    symbols ={}
    for key, value in data['symbols'].items():
          symbols[value['code'].upper()] = value['description'].lower()
          
    return symbols


def test_input1(amountt):
      if type(amountt) == int or type(amountt) == float and amountt > 0:
         return True
      else:
         return False
      
def test_input2(from_currencyy, symbols):
      if from_currencyy.upper() in symbols.keys():
         return True
      else:
         return False
      
def test_input3(from_currencyy, to_currencyy, symbols):
      if to_currencyy.upper() in symbols.keys():
         if not from_currencyy == to_currencyy:
            return True
      else:
         return False         


def currency_lookup(symbols):
    
    print('''\n
      %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
      %        WELCOME TO THE CURRENCY CONVERSION PROGRAM          %
      %                                                            %
      %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
      \n''')
    

    while True:
      isValid = True
      try:
        amount = eval(input("\nplease enter the amount you would like to convert?\n"))
      except:
        isValid = False 
      if isValid:
        if type(amount) == int or type(amount) == float and amount > 0:
          break
        else:
          print("Invalid input, please try again. \n")
          continue
      else:
        print("Invalid input, please try again. \n")
        continue
        
    while True:
      from_currency = input('\nplease enter the currency you have?\n')
      if not from_currency.upper() in symbols.keys():
        print('Invalid input or not included in database please try again!')
        continue
      else:
        from_currency.upper()
        break
        
    while True:
      to_currency = input('\nPlease enter the currency you would like to exchange to?\n')
      if not to_currency.upper() in symbols.keys():
        print('Invalid input or not included in database please try again!\n')
        continue
      if from_currency == to_currency:
        print('Invalid input: please enter another currency to convert to!\n')
        continue
      else:
        to_currency.upper()
        break              
          
    return from_currency.upper(), to_currency.upper(), amount
         
          
def convertion_json(from_currency, to_currency):
    base_url = 'https://api.exchangerate.host/'

    full_url = base_url + 'convert?from=' + from_currency + '&to=' + to_currency
    response_2 = requests.get(full_url)
    data_2 = response_2.json()
    return data_2



def final_cal(data_2, amount, to_currency):
    final_amount = 0
    rate = 0
    for key, value in data_2['info'].items():
        rate = value
        
    final_amount = float(rate) * float(amount)
    print(f'\nYour final amount is  {final_amount}  {to_currency}\n')
    
    print('''\n
      %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
      %                                                            %
      %        THANK YOU FOR USING OUR CONVERSION PROGRAM          %
      %                                                            %
      %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
      \n''')
    
    
def view_currencies():
    url_symbols = 'https://api.exchangerate.host/symbols'
    response = requests.get(url_symbols)
    data = response.json()

    symbols ={}
    for key, value in data['symbols'].items():
        symbols[value['code'].upper()] = value['description'].lower()
        
    for x in symbols.keys():
      print(x + ' => ' + symbols[x])
    
    
def convert_curr_program():
    symbols_data = symbols_json()
    symbols_dictionary = symbols_dic(symbols_data)    
    from_cur, to_cur, amt  = currency_lookup(symbols_dictionary)
    rate_data = convertion_json(from_cur, to_cur)
    final_cal(rate_data, amt, to_cur)
    
#     ## delete out later
#     rate_data = convertion_json('USD', 'EUR')
#     final_cal(rate_data, 80, 'EUR')
    
    
# if __name__ == "__main__":
#     main()

# convert_curr_program()
 







