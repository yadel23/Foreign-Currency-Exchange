import requests

def symbols_json():
    url_symbols = 'https://api.exchangerate.host/symbols'
    response = requests.get(url_symbols)
    data = response.json()
    return data


def symbols_dic(data):
    symbols ={}
    for key, value in data['symbols'].items():
          symbols[value['description'].lower()] = value['code'].upper()
    return symbols


def currency_lookup(symbols):
    
    amount = eval(input("please enter the amount you would like to exchange?\n"))
    from_currency = input('please enter the currency?\n')
    to_currency = input('Please enter the currency you would like to exchange to?\n')
    
    for key, value in symbols.items():
        if from_currency.upper() == value:
          from_currency = from_currency.upper()     

        if to_currency.upper() == value:
          to_currency = to_currency.upper()
          
    return from_currency, to_currency, amount
         
          
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
    print(f'Your final amount is  {final_amount}  {to_currency}')

    
def main():
    symbols_data = symbols_json()
    symbols_dictionary = symbols_dic(symbols_data)
    
#    from_cur, to_cur, amt  = currency_lookup(symbols_dictionary)
#     rate_data = convertion_json(from_cur, to_cur)
#     final_cal(rate_data, amt, to_cur)
    ## comment out later
    rate_data = convertion_json('USD', 'EUR')
    final_cal(rate_data, 80, 'EUR')
    
    
if __name__ == "__main__":
    main()
 







