#!/usr/bin/env python
# -*- coding: UTF-8 -*-


#HOW INSTALL AND USE THIS PROJECT:
#in the console : sudo python setup.py install
#And all the depencies will be installed with the Project

from setuptools import setup, find_packages

setup(
    name='FR_Template',
    version="1.13.73",
    author='Franck Rochat',
    author_email='rochat.franck@gmail.com',
    description='The Starter Pack.',
    url='https://github.com/Franck1333/FR_Template',
    license='lgpl',
    packages=find_packages(),
    include_package_data=True,
    install_requires=["Unidecode","Unirest","urllib3","requests","pydub","pyserial","Cython","kivy"], #Get the Dependencies from Pypi (pip install)
    #dependency_links=[''], #Get the Dependencies via HTTP(s)
)
