import unittest
from camelCase import to_camel_case

class TestCamelCase(unittest.TestCase):
    def test_1_1(self):
        str1 = "the_stealth_warrior"
        result = to_camel_case(str1)
        self.assertEqual(result,"theStealthWarrior")
    def test_1_2(self):
        str2 = "The-Stealth-Warrior"
        result = to_camel_case(str2)
        self.assertEqual(result,"TheStealthWarrior")
    def test_1_3(self):
        str3 = ""
        result = to_camel_case(str3)
        self.assertEqual(result,"")
    def test_1_4(self):
        str4 = "A-B-C"
        result = to_camel_case(str4)
        self.assertEqual(result,"ABC")


if __name__ == '__main__':
    unittest.main()



