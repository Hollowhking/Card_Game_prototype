from utils.config import Config
import string

class Logger():
    def __init__(self, config):
        self.config = config
    
    def output(self, data:string, level:string):
        log_level     = {"NONE": 0 , "INFO": 1 , "DEBUG": 2 , "ERROR": 3}.get(level, 0)
        logging_level = {"NONE": 0 , "INFO": 1 , "DEBUG": 2 , "ERROR": 3}.get(self.config.logging_level, 0)
        if (logging_level >= log_level):
            print(data)