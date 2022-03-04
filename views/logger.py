import csv
import os
import random
from typing import Type

class Logger:
    def __init__(self,folder, name):
        self.rows = []
        self.name = name
        self.log_folder = folder

    def add_row(self, row: tuple):
        """
        Function to write rows by taking in
        """
        self.rows.append(tuple((str(i) for i in row)))

    def __del__(self):
        """
        Upon destruction of object, log the data to a csv
        """
        with open(self.log_folder + self.name + '.csv', 'w', encoding='utf-8', newline='') as f:
            writer = csv.writer(f)
            for row in self.rows:
                writer.writerow(row)

class LoggerProcessor:
    def log(self, data: tuple,i: int):
        """
        Add row to ith logger
        """    
        self.loggers[i].add_row(data)
    
    def log_multiple(self, data_list: list):
        for i in range(len(data_list)):
            self.log(data_list[i],i)
    
    def process_header(self, vars):
        for i in range(len(vars)):
            self.add_logger(vars[i])   
            self.log((vars[i], "column"), i)
    
    def process_data(self,vars):
        for i in range(len(vars)):
            self.log((vars[i],1), i)

class LoggerManager:
    def __init__(self):
        self.log_folder = 'log/'
        self.create_log_folder()
        self.loggers = []
        self.processor = LoggerProcessor()

    def create_log_folder(self):
        if not os.path.exists(self.log_folder):
            os.makedirs(self.log_folder)

    def get_logger(self, i: int) -> Logger:
        return self.loggers[i]

    def add_logger(self, name: str):
        self.loggers.append(Logger(self.log_folder, name))



