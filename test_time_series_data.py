import unittest
from Time_series_data import gatherInput, symbols_json, symbols_dic

data = symbols_json()
symb_dict = symbols_dic(data)
start_date, end_date, currency_list  = gatherInput(symb_dict)

class TestFileName(unittest.TestCase):
 
    #testing if it returns a dictionary
    def test_function1(self):
      
        self.assertEqual(type(data), dict)
        self.assertIsNotNone(data)
       
    #testing if it returns a dictionary
    def test_function2(self):
      
        self.assertEqual(type(symb_dict), dict)
        self.assertIsNotNone(symb_dict)
     
    #testing from currency, to currency, and amount
    def test_function3(self):
      
        is_num = False
        if type(amt) == int or float:
          is_num = True
          
        self.assertEqual(type(start_date), str)
        self.assertEqual(type(end_date), str)
        self.assertNotEqual(type(currency_list), list)
        
        self.assertTrue(is_num)
        
        self.assertIsNotNone(start_date)
        self.assertIsNotNone(end_date)
        self.assertIsNotNone(currency_list)
    
     
      
        