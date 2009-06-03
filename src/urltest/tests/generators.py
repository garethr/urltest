#!/usr/bin/env python

"These tests check the test generator in urltest"

# standard library
import unittest

# module under test
from urltest import test_generator

class GeneratorTests(unittest.TestCase):
    
    def test_get_request_to_root_with_200_code(self):
        item = {'url':"/", 'code':200}
        test_method = test_generator(item)
        # check this is actually a function        

if __name__ == "__main__":
    unittest.main()