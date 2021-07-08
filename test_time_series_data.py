import unittest
from Time_series_data import buildUrl, buildDataframe, gatherInput

data = symbols_json()
symb_dict = symbols_dic(data)
from_cur, to_cur, amt = currency_lookup(symb_dict)
data_2 = convertion_json(from_cur, to_cur)
    
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
          
        self.assertEqual(type(from_cur), str)
        self.assertEqual(type(to_cur), str)
        self.assertNotEqual(type(amt), str)
        
        self.assertTrue(is_num)
        
        self.assertIsNotNone(from_cur)
        self.assertIsNotNone(to_cur)
        self.assertIsNotNone(amt)
        
        self.assertEqual(len(from_cur), 3)
        self.assertEqual(len(to_cur), 3)
     
    #testing if it returns a dictionary
    def test_function4(self):
        
        self.assertEqual(type(data_2), dict)
        self.assertIsNotNone(data_2)
        
#     def test_function5(self):
#         final_amont = final_cal(data_2, amt, to_cur)
#         self.assertIsNone(final_amont)
        
        
        
      
        