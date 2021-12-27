"""Loader Class"""

import json
from sys import exc_info
from datetime import datetime
from lib.utils import FileUtils


from src.validator import Validator


class Report(Validator):
    """
    Class for generating report against json input file

    Attributes
    ----------
        file_path: input json file path
        logger: logger object

    Methods:
    -------
        GenerateReport: Loads the json file data, sends for record logging and writing into file
        AddEvent: Manages the event records in dictionary with event name, date and count w.r.t date
    """
    def __init__(self, file_path, logger):
        self.logger = logger
        super().__init__(logger=self.logger)
        self.file_path = file_path
        self.file_dir =  self.file_path.split('/input.json')[0]
        self.event_report = {}


    def GenerateReport(self):
        """
        Loads the file line by line to handle the memory issues and then loads json 
        to send for validation and logging purposes
        """
        try:
            with open(self.file_path, 'r') as file:
                for line in file:
                    record = json.loads(line)
                    self.validate(msg=record)
                    self.AddEvent(msg=record)
            
            FileUtils.write_file(file_name=f'{self.file_dir}/report.csv', data_dict=self.event_report)

        except Exception as ex:
            self.logger.error(ex, exc_info=True)


    def AddEvent(self, msg):
        """
        Manages the event records in dictionary with event name, date and count w.r.t date
        """
        try:
            
            if msg['event_text'] not in self.event_report.keys():
                self.event_report[msg['event_text']] = {}

            event_date = datetime.strptime(msg['received_at'], "%Y-%m-%d %H:%M:%S.%f").strftime("%Y-%m-%d")
            if event_date not in self.event_report[msg['event_text']].keys():
                self.event_report[msg['event_text']][event_date] = 0

            self.event_report[msg['event_text']][event_date] += 1
                
        except Exception as ex:
            self.logger.error(ex, exc_info=True)
