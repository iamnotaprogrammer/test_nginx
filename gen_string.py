import random
# import itertools
# import unittest2
import time


def random_string(string_len, only_digit=False, mixing=False, with_upper_case=False):
    """ Return the random string """
    template_letters = 'abcdefghijklmnopqrstuvwxyz'
    template_digits = '0123456789'
    if with_upper_case and mixing:
        length = len(template_letters)
        template = ''.join(random.sample(template_letters, length)) + template_digits + \
            ''.join(random.sample(template_letters, length)
                    ).upper() + template_digits
    elif only_digit:
        template = template_digits
    elif mixing:
        template = template_digits + template_letters

    else:
        template = ''.join(random.sample(
            template_letters, len(template_letters)))
    result = ''
    i = 0
    while i < string_len:
        i += 1
        result += random.choice(template)
    return result


# class TestGetRandomString(unittest2.TestCase):
#     """ class who test the random_string function"""

#     def test_mode_only_letters(self):
#         """ Testing method   """
#         for el in random_string(30):
#             self.assertTrue(el.islower())
#             self.assertFalse(el.isdigit())

#     def test_isalfa(self):
#         """Testing method"""
#         self.assertEqual(random_string(30).isalpha())

#     def test_mode_mixing(self, mixing=True):
#         """ Testing method   """
#         for el in random_string(30):
#             self.assertTrue(el.islower() or el.isdigit())

#     def test_mode_only_digit(self):
#         """ Testing method   """
#         for el in random_string(30, only_digit=True):
#             self.assertTrue(el.isdigit())

#     def test_mode_with_upper_case(self):
#         """ Testing method """
#         flag = False
#         for el in random_string(30, with_upper_case=True):
#             if el.isupper():
#                 flag = True
#                 break
#         else:
#             self.assertTrue(flag)


    def test_lenth(self):
        """ Test length """
        self.assertEqual(len(random_string(30)), 30)

if __name__ == '__main__':
    # unittest2.main()
    i=0
    while i < 20:
        i+=1
        print(random_string(30, with_upper_case=True))
