#!/usr/bin/env python

from setuptools import setup, find_packages

setup(
    name = "urltest",
    version = "0.2.3",
    author = "Gareth Rushgrove",
    author_email = "gareth@morethanseven.net",    
    url = "http://github.com/garethr/urltest",
    packages = find_packages('src'),
    package_dir = {'':'src'},
    test_suite = "urltest.tests",
    install_requires = [
        "WebTest>=1.2",
    ],
    licence = "MIT License",
    keywords = "wsgi testing urls",
    description = "A wrapper around WebTest which provides a nice domain specific language for testing URLs in WSGI applications",
    long_description = '''\
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
''',
    classifiers = [
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Topic :: Internet :: WWW/HTTP :: WSGI",
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Testing',
    ]
)
