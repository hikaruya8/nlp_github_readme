# -*- coding: utf-8 -*-

# Learn more: https://github.com/kennethreitz/setup.py

from setuptools import setup, find_packages


with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='nlp_github_readme',
    version='0.1.0',
    description='In development    NLP_GitHub_README -- Calculate the Standard Score of the GitHub user by using Natural Language Processing and Machine Learning',
    long_description=readme,
    author='hikaruya8',
    author_email='h.yamada.bg@gmail.com',
    install_requires=['requests, BeautifulSoup'],
    url='https://github.com/hikaruya8/nlp_github_readme',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)

