import csv
from typing import Type

class LoggerModel:
    def __init__(self):
        self.rows = []

    def set_folder(self, folder):
        self.log_folder = folder
        return self

    def set_name(self, name):
        self.name = name
        return self

    def __del__(self):
        """
        Upon destruction of object, log the data to a csv
        """
        with open(self.log_folder + self.name + '.csv', 'w', encoding='utf-8', newline='') as f:
            writer = csv.writer(f)
            for row in self.rows:
                writer.writerow(row)


