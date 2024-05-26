import sys

class CustomException(Exception):

    def __init__(self, error_message, sys_details:sys):
        self.error_message = error_message
        _, _, exe_tb = sys_details.exc_info()
        
        self.lineno = exe_tb.tb_lineno
        self.filename = exe_tb.tb_frame.f_code.co_filename

    def __str__(self):
        return f"Error occured in \n Python File: {self.filename} \n Line Number: {self.lineno} \n Error Message: {self.error_message}"



