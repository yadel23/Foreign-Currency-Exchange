import unittest
from convert_currency import symbols_json, symbols_dic, currency_lookup

class TestFileName(unittest.TestCase):
    #testing if it returns a dictionary
    def test_function1(self):
        is_json = symbols_json()
        self.assertTrue(type(is_json), dict)
       
    #testing if it returns a dictionary
    def test_function2(self):
        data = symbols_json()
        is_dict = symbols_dic(data)
        self.assertTrue(type(is_dict), dict)
        
    def test_function3(self):
        data = symbols_json()
        symb_dict = symbols_dic(data)
        from_cur, to_cur, amt = currency_lookup(symb_dict)
        
#         print(f'\n\n\n {from_cur}, {to_cur}, {type(amt)}')
#         self.assertTrue(type(from_cur), str)
#         self.assertTrue(type(to_cur), str)
#         self.assertTrue(type(amt), str)
        
        
        
        
      
        