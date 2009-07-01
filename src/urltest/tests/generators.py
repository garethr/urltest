#!/usr/bin/env python

"These tests check the test generator in urltest"

# standard library
import unittest

# module under test
from urltest import test_generator

class GeneratorTests(unittest.TestCase):
    
    def test_method_generator_returns_callable(self):
        item = {'url':"/", 'code':200}
        test_method = test_generator(item)
        assert hasattr(test_method, '__call__')

if __name__ == "__main__":
    unittest.main()