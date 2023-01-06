import unittest
from ibm_cloud_sdk_core.api_exception import ApiException

from translator import english_to_french, french_to_english

class TestEnglishToFrench(unittest.TestCase): 
    def test1(self): 
        self.assertRaises(ApiException , english_to_french, "")
        self.assertEqual(english_to_french("Hello"), "Bonjour")  # test when "Hello" is given as input the output is "Bonjour".
        

class TestFrenchToEnglish(unittest.TestCase): 
    def test1(self): 
        self.assertRaises(ApiException , french_to_english, "")
        self.assertEqual(french_to_english("Bonjour"), "Hello") # test when "Bonjour" is given as input the output is "Hello".
        
unittest.main()
