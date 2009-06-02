#!/usr/bin/env python

"These tests check some of the helper functions in urltest"

# standard library
import unittest

# module under test
from urltest import _get_method, _get_test_name

class GetMethodTests(unittest.TestCase):
        
    def test_method_defaults_to_get(self):
        item = {'url':"/", 'code':200}
        method = _get_method(item)
        self.assertEqual(method, "get")

    def test_method_can_be_post(self):
        item = {'url':"/", 'method': "post", 'code':200}
        method = _get_method(item)
        self.assertEqual(method, "post")

    def test_method_capitalisation_doesnt_matter(self):
        item = {'url':"/", 'method': "POST", 'code':200}
        method = _get_method(item)
        self.assertEqual(method, "post")
        item = {'url':"/", 'method': "PoSt", 'code':200}
        method = _get_method(item)
        self.assertEqual(method, "post")

    def test_invalid_method_defaults_to_get(self):
        item = {'url':"/", 'method': "Foo", 'code':200}
        method = _get_method(item)
        self.assertEqual(method, "get")

class NameTests(unittest.TestCase):
    
    def test_get_request_to_root_with_200_code(self):
        item = {'url':"/", 'code':200}
        test_name = _get_test_name(item)
        self.assertEqual(test_name, "test_get_request_of_/_returns_200")

    def test_longer_url_with_404(self):
        item = {'url':"/foo/bar", 'code':404}
        test_name = _get_test_name(item)
        self.assertEqual(test_name, "test_get_request_of_/foo/bar_returns_404")

    def test_method_name_is_reflected_in_test_name(self):
        item = {'url':"/foo/bar", 'method': 'delete', 'code':405}
        test_name = _get_test_name(item)
        self.assertEqual(test_name, "test_delete_request_of_/foo/bar_returns_405")

if __name__ == "__main__":
    unittest.main()