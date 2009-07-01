#!/usr/bin/env python

from setuptools import setup, find_packages

setup(
    name = "urltest",
    version = "0.1",
    author = "Gareth Rushgrove",
    author_email = "gareth@morethanseven.net",    
    url = "http://github.com/garethr/urltest",
    packages = find_packages('src'),
    package_dir = {'':'src'},
    test_suite = "urltest.tests",
    install_requires = [
        "WebTest>=1.2",
    ],
    description = "A wrapper around WebTest which provides a nice domain specific language for testing URLs in WSGI applications",
    long_description = """
+++++++
UrlTest
+++++++

A wrapper around WebTest which provides a nice domain specific language for
testing URLs in WSGI applications. The following example demonstrates usage:

Example
=======

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

Files
=====

""",
    classifiers = [
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Topic :: Internet :: WWW/HTTP :: WSGI",
    ]
)
