"""
Description 
***********
    Main module

Developed by 
    Nishant Baheti
"""
import os
from dataload import DataLoader

# there is still an issue with loading csv file with Sphinx documentation
# TODO : look for a solution
dataLoader = DataLoader(
    path=os.path.join(os.getcwd(), "iris.csv"),
    fileExt="csv"
)


df = dataLoader.getDataFrame()
