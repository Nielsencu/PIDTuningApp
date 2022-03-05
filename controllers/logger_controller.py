import os
from typing import List

class LoggerController:
    def __init__(self, model):
        self.model = model
    
    def handle_data(self,row : tuple):
        """
        Function to write rows by taking in tuple 
        """
        self.model.rows.append(tuple((str(i) for i in row)))

class LoggerFactory:
    def __init__(self):
        self.loggers = []

    def create_log_folder(self, folder):
        if not os.path.exists(folder):
            os.makedirs(folder)

    def create_logger_controllers(self,loggers) -> List[LoggerController]:
        for logger_model in loggers:
            self.loggers.append(LoggerController(logger_model))
        return self

    def set_motors(self, names):
        for i in range(len(names)):
            self.loggers[i].model.set_name(names[i])
        return self

    def set_folders(self, folder):
        for i in range(len(self.loggers)):
            self.loggers[i].model.set_folder(folder)
        self.create_log_folder(folder)
        return self

    def build(self):
        return self.loggers

class LoggerManager:
    def setup(self, logger_controllers):
        self.logger_controllers = logger_controllers

    def get_logger_controller(self, i: int) -> LoggerController:
        return self.logger_controllers[i]

    def handle_data(self, data):
        for i in range(len(self.logger_controllers)):
            self.get_logger_controller(i).handle_data(data)  



