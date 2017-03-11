import unittest
from newsolution import process_words

class TestCases(unittest.TestCase):
    
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_empty_string(self):
        """Tests that empty string should come back as empty """
        self.assertEqual(process_words(None),None) 

    def test_one_character_string(self):
        """ Tests that a string with single alphabet should come back untouched """
        self.assertEqual(process_words("a"), "a")

    def test_string_with_only_spaces(self):
        """ Tests that a string with only empty spaces should come back with same number of empty spaces """
        #send a string with 3 spaces in it
        self.assertEqual(process_words('   '),'   ')
    
    def test_string_with_only_numbers(self):
        """ Tests a string with only numbers """
        self.assertEqual(process_words('1234'), '1234')

    def test_string_with_numbers_special_characters(self):
        """ Test a string with special characters and numbers """
        self.assertEqual(process_words('123,34!'),'123,34!')

    def test_string_with_two_alphabets(self):
        """ Test a two character string """
        self.assertEqual(process_words('Ab'), 'A0b')

    def test_string_with_three_alphabets(self):
        """ Test a three character string """
        self.assertEqual(process_words('ABC'), 'A1C')

    def test_string_with_three_alphabets_numbers_at_end(self):
        """" Tests a string with 3 alphabets first and then number at end ABC123 """
        self.assertEqual(process_words('ABC123'),'A1C123')

    def test_string_wtih_numbers_and_special_character_in_the_middle(self):
        """" Tests a string with numbers in the middle of a string along with special characeters """
        self.assertEqual(process_words('ABCD1@#$BCDEFG AB'), 'A2D1@#$B4G A0B')

    def test_string_starting_numbers_and_alphabets_in_the_end(self):
        """" Tests a string with numbers in the begining and alphabets at the end """
        self.assertEqual(process_words('1234ABCDEFG') ,'1234A5G')

    def test_string_with_spaces_and_alphabets(self):
        """" Tests a string with spaces """
        self.assertEqual(process_words('ABCDE   HIJK') ,'A3E   H2K')

    def test_string_with_same_alphabets(self):
        """ Tests a string with same alphabets """
        self.assertEqual(process_words('AAAA AAA AAAAA AAAAAAAA AAAaaAAAAA aaaaAA') ,'A1A A1A A1A A1A A1A a1A')

    def test_string_with_same_alphabets_mixed_cases(self):
        """ Tests a string with mixed case same alphabets """
        self.assertEqual(process_words('AaAa'), 'A1a')
    
    def test_string_with_mixed_white_spaces(self):
        """" Tests a string with mixed whitespaces tabs and white spaces """
        self.assertEqual(process_words('  Cox     Automotive') ,'  C1x     A6e')

if __name__ == "__main__":
    unittest.main()
