from convert_currency import convert_curr_program, view_currencies
from Time_series_data import time_series_program

def menu():
    print('''
          %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
          %                                                            %
          %  HELLO WELCOME TO FOREIGN CURRENCY & CRYPTOCURRENCY RATES  %
          %                                                            %
          %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
          ''')
    print('''\n
          1) View currencies and symbols available 
          2) Convert your currency
          3) View history of currencies in a line graph
          4) Exit program
          \n''')


def option_handler(option):
    try:
      return int(option)
    except:
      return -1

menu()
option = option_handler(input('Enter your optoins: [1, 2, 3, 4]\n'))

while option != 4:
    if option == 1:
      view_currencies()
      print('''\n
          1) View currencies and symbols available 
          2) Convert your currency
          3) View history of currencies in a line graph
          4) Exit program
          \n''')
    elif option == 2:
      convert_curr_program()
      print('''\n
          1) View currencies and symbols available 
          2) Convert your currency
          3) View history of currencies in a line graph
          4) Exit program
          \n''')
    elif option == 3:
      time_series_program()
      print('''\n
          1) View currencies and symbols available 
          2) Convert your currency
          3) View history of currencies in a line graph
          4) Exit program
          \n''')
    
    #menu()
    option = option_handler(input('\nEnter your optoins: [1, 2, 3, 4]\n'))

print('''
      %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
      %                                                            %
      %    Thank YOU FOR USING OUR PROGRAM, COME AGAIN LATER:)     %
      %                                                            %
      %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
      ''')
    