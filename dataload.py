"""
Description 
***********
    Data Load module

Developed by 
    Nishant Baheti
"""
import pandas as pd


class DataLoader:
    """Data Loader Class

    Args: 
        path (str) : complete path to file
        fileExt (str) : Extention of file

    """

    def __init__(self, path, fileExt):
        """Constructor 
        """
        self.path = path
        self.fileExt = fileExt

    def getDataFrame(self):
        """Load Data file to Dataframe 

        Returns:
            df (pandas.core.frame.DataFrame) : dataframe with data 

        Raises:
            ValueError : Value error


        """
        if self.fileExt.lower() == "csv":
            df = pd.read_csv(self.path)
            return df
        elif self.fileExt.lower() in ['xlsx', 'xls', 'excel']:
            df = pd.read_excel(self.path)
            return df
        else:
            raise ValueError(f"{self.fileExt} is not recognizable.")
