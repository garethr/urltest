#!/usr/bin/env python

"These tests check the test runner in urltest"

# standard library
import sys
import unittest
from StringIO import StringIO

# we need some extra assertions
from common import CommonTest

# module under test
from urltest import verify_urls


def demo_app(environ, start_response):
    "this is a very simple WSGI application we use for testing"
    stdout = StringIO()
    print >>stdout, "Hello world!"
    print >>stdout
    start_response("200 OK", [('Content-Type', 'text/plain')])
    return [stdout.getvalue()]


class RunnerTests(CommonTest):

    def setUp(self):
        self.stdout = sys.stdout
        self.stderr = sys.stderr

    def tearDown(self):
        sys.stdout = self.stdout
        sys.stderr = self.stderr

    def capture_verify_urls(self, urls, app):
        sys.stdout = StringIO()
        sys.stderr = StringIO()
        verify_urls(urls, app)
        out = sys.stdout.getvalue()
        err = sys.stderr.getvalue()
        sys.stdout = self.stdout
        sys.stderr = self.stderr
        return out, err

    def capture_verify_urls_err(self, urls, app):
        sys.stderr = StringIO()
        sys.stdout = StringIO()
        verify_urls(urls, app)
        res = sys.stderr.getvalue()
        sys.stderr = self.stderr
        sys.stdout = self.stdout
        return res

    def test_verify_urls_with_no_tests(self):
        output = self.capture_verify_urls((), demo_app)
        self.assert_contains("Ran 0 tests in 0.000s", output[0])

    def test_verify_urls_with_a_single_test(self):
        output = self.capture_verify_urls(({'url': "/", 'code': 200}, ), demo_app)
        self.assert_contains("Ran 1 test in", output[0])

    def test_verify_urls_with_multiple_tests(self):
        output = self.capture_verify_urls(({'url': "/", 'code': 200}, {'url': "/foo", 'code': 200}), demo_app)
        self.assert_contains("Ran 2 tests in", output[0])

    def test_a_failing_test(self):
        output = self.capture_verify_urls(({'url': "/", 'code': 404}, ), demo_app)
        self.assert_contains("FAILED", output[0])

if __name__ == "__main__":
    unittest.main()
