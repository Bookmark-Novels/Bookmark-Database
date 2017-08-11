from setuptools import setup

setup(
    name='bookmark-database',
    description='Python package for interacting with Bookmark\'s database.',
    author='Bookmark Novels',
    version='1.0.0',
    packages=['bookmark_database'],
    url='https://github.com/Bookmark-Novels/Bookmark-Database',
    license='MIT',
    install_requires=[
        'mysqlclient==1.3.10',
        'SQLAlchemy==1.1.13',
        'locksmith==1.0.0'
    ],
    dependency_links=[
        'https://github.com/Bookmark-Novels/Locksmith/tarball/v1#egg=locksmith'
    ]
)
