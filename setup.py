from distutils.core import setup

setup(
    name = 'Killbill',
    version = '0.1dev',
    packages = ['killbill',],
    author = 'Killbilling team',
    author_email = 'killbilling-dev@googlegroups.com',
    url = 'https://github.com/killbilling/killbill-client-python',
    license = 'Apache License 2.0',
    long_description = open('README.txt').read(),
    classifiers = [
        'Development Status :: 1 - Planning',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.2',
        'Topic :: Software Development :: Libraries',
    ]
)
