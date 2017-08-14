from setuptools import setup

setup(
    name='bookmark-database',
    description='Python package for interacting with Bookmark\'s database.',
    author='Bookmark Novels',
    version='1.0.5',
    packages=['bookmark_database'],
    url='https://github.com/Bookmark-Novels/Bookmark-Database',
    license='MIT',
    install_requires=[
        'mysqlclient',
        'SQLAlchemy'
    ]
)
