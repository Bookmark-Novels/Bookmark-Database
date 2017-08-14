from setuptools import setup

setup(
    name='bookmark-database',
    description='Python package for interacting with Bookmark\'s database.',
    author='Bookmark Novels',
    version='1.0.3',
    packages=['bookmark_database'],
    url='https://github.com/Bookmark-Novels/Bookmark-Database',
    license='MIT',
    install_requires=[
        'mysqlclient',
        'SQLAlchemy',
        'locksmith'
    ],
    dependency_links=[
        'git+git://github.com/Bookmark-Novels/Locksmith.git#egg=locksmith'
    ]
)
