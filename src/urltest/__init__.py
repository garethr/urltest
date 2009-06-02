#!/usr/bin/env python

"""
A wrapper around WebTest which provides a nice domain specific language for
testing URLs in WSGI applications. The following example demonstrates usage:

#!/usr/bin/env python

from example_app import application
from urltest import verify_urls
                
if __name__ == "__main__":
    urls = (
        {'url':"/", 'code':200},
        {'url':"/bob", 'code':200},
        {'url':"/jim", 'code':404},
        {'url':"/jim", 'method': "POST", 'code':405},
    )    
    verify_urls(urls, application)
"""

# standard library
import unittest

# external module
from webtest import TestApp

# so we can simply state the numeric code without having
# to know the description we have a lookup table
# http://www.faqs.org/rfcs/rfc2616.html
CODES = {
    100: "Continue", 
    101: "Switching Protocols", 
    200: "OK", 
    201: "Created", 
    202: "Accepted", 
    203: "Non-Authoritative Information", 
    204: "No Content", 
    205: "Reset Content", 
    206: "Partial Content", 
    300: "Multiple Choices", 
    301: "Moved Permanently", 
    302: "Found", 
    303: "See Other", 
    304: "Not Modified", 
    305: "Use Proxy", 
    307: "Temporary Redirect", 
    400: "Bad Request", 
    401: "Unauthorized", 
    402: "Payment Required", 
    403: "Forbidden", 
    404: "Not Found", 
    405: "Method Not Allowed", 
    406: "Not Acceptable",
    407: "Proxy Authentication Required", 
    408: "Request Time-out", 
    409: "Conflict", 
    410: "Gone", 
    411: "Length Required", 
    412: "Precondition Failed", 
    413: "Request Entity Too Large", 
    414: "Request-URI Too Large", 
    415: "Unsupported Media Type", 
    416: "Requested range not satisfiable", 
    417: "Expectation Failed", 
    500: "Internal Server Error", 
    501: "Not Implemented", 
    502: "Bad Gateway", 
    503: "Service Unavailable", 
    504: "Gateway Time-out", 
    505: "HTTP Version not supported",
}

def _get_method(item):
    "Get the HTTP method from the passed data, defaulting to GET"
    try:
        # we lowercase everything so you can use whatever
        # capitalisation in your code
        method = item['method'].lower()
    except KeyError:
        # but to make the DSL nicer we default to get
        method = "get"
    # we only support the following methods
    # anything else works just like a get
    # head is not included as it's not supported by WebTest
    # I don't think
    if method not in ("get", "post", "delete", "put"):
        method = "get"
    return method

def _get_test_name(item):
    "Create a user friendly name for the test"
    return 'test_%s_request_of_%s_returns_%d' % (
        _get_method(item), item['url'], item['code'])
    

def test_generator(data):
    """
    This function returns a dynamically created test method
    which can be added to a unitest test class
    """
    def test(self):
        "A test dynamically generated test method"
        # first we need to establish the method
        method = _get_method(data)
        # depending on the method we want to make a different request
        # of the WSGI application. We set expect_errors to True as we want to 
        # deal with the status code, not have it throw an exception
        # if it's anything other than a 2xx/3xx code
        if method == "get":
            response = self.app.get(data['url'], expect_errors=True)        
        elif method == "delete":
            response = self.app.delete(data['url'], expect_errors=True)        
        elif method == "post":
            response = self.app.post(data['url'], expect_errors=True)        
        elif method == "put":
            response = self.app.put(data['url'], expect_errors=True)        
        # now assert that the returned response code matches 
        # the one specified in the DSL
        self.assertEquals("%s %s" % (data['code'], CODES[data['code']]), response.status)
    # return the test method
    return test
             
def verify_urls(data, application):
    """
    This is the test runner for the DSL. It creates an empty TestCase, parses
    the DSL and dynamically appends the test methods. It then runs the 
    test suite and prints the results.
    """
    
    class TestSuite(unittest.TestCase):
        "A blank TestCase waiting for test methods"
        def setUp(self):
            "Store the WSGI app for easy access by methods"
            self.app = TestApp(application)                
    
    # loop over the specified urls
    for item in data:
        # again get the method
        method = _get_method(item)
        # get a useful test name
        test_name = _get_test_name(item)
        # then create the test method
        test = test_generator(item)
        # and add it to the TestSuite
        setattr(TestSuite, test_name, test)

    # once all the test methods have been added we can get the full suite
    suite = unittest.TestLoader().loadTestsFromTestCase(TestSuite)
    # and then run the tests via the default TestRunner
    unittest.TextTestRunner().run(suite)
