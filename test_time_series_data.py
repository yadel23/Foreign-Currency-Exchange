import unittest
from Time_series_data import gatherInput, symbols_json, symbols_dic, input_test_1, input_test_2, input_test_3, input_test_4

data = symbols_json()
symb_dict = symbols_dic(data)
#start_date, end_date, currency_list  = gatherInput(symb_dict)

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
      date = input_test_1(2000)
      self.assertEqual(date, False)
      self.assertIsNotNone(date)
      
      e_date = input_test_1("2000-05-22")
      self.assertEqual(e_date, True)
      self.assertIsNotNone(e_date)
      
      cur = input_test_3("cad", {"USD":0.5, "AED":0.6}, ["2000-04-22", "2000-05-22"], ["CAD", "AUD"])
      self.assertEqual(cur, False)
      self.assertIsNotNone(cur)
      
      cur_number = input_test_4(4)
      self.assertEqual(cur_number, True)
      self.assertIsNotNone(cur_number)
      
     
      
        