from setuptools import setup, find_packages

setup(
    name = 'poker_lib',
    version = '0.1',
    packages = find_packages(exclude=['tests*']),
    # license='MIT',
    description = 'An example python package',
    long_description = open('README.txt').read(),
    install_requires = ["pandas", "numpy"],
    url = "https://github.com/martindub87/poker",
    # author = 'martindub87',
    # author_email='myemail@example.com'
)
