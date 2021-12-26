"""Utilities module for Validator"""

import csv

class FileUtils:
    """
    Utility for file relation operations.

    Methods:
    --------

    Static:
        write_file: Writes data into the file
    """

    @staticmethod
    def write_file(file_name, data_dict):
        """
        Writes data into the file

        Parameters
        ----------
            file_name : str
                path of the file
            data_dict : dict
                data to be written into the file

        Returns:
        --------
            dict
                key/value pair for file_name and list_matrix
        """
        list_matrix=[]
        header = ['EventName', 'EventDate', 'EventCount']
        list_matrix.append(header)

        for key, val in data_dict.items():
            for _key, _val in val.items():
                list_matrix.append([key, _key, _val])

        with open(file_name, 'w', encoding='UTF8' , newline='') as file:
            writer = csv.writer(file)
            writer.writerows(list_matrix)