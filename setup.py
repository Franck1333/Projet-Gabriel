#!/usr/bin/env python
# -*- coding: UTF-8 -*-


#HOW INSTALL AND USE THIS PROJECT:
#in the console : sudo python setup.py install
#And all the depencies will be installed with the Project

from setuptools import setup, find_packages

setup(
    name='Projet Gabriel',
    version="0.13",
    author='Franck Rochat',
    author_email='rochat.franck@gmail.com',
    description="Projet d'agrégation d'actualité via mots clés.",
    url='https://github.com/Franck1333/Projet-Gabriel',
    license='lgpl',
    packages=find_packages(),
    include_package_data=True,
    install_requires=["psutil","setuptools","feedparser","reportlab"], #Get the Dependencies from Pypi (pip install)
    #dependency_links=[''], #Get the Dependencies via HTTP(s)
)
