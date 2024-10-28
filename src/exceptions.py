import sys
from src.logger import logging

def error_message_detail(error, error_detail:sys):
    '''
    In this function, the goal is to use sys.exc_info() (a function from the sys module) to get 
    details about an error, like the line number and file name where the error happened. By passing 
    sys as error_detail, you can call error_detail.exc_info() to grab those details.
    '''
    _,_,exc_tb=error_detail.exc_info()
    file_name=exc_tb.tb_frame.f_code.co_filename
    error_message="Error occured in python script name [{0}] line number [{1}] error message [{2}]".format(
    file_name,exc_tb.tb_lineno,str(error)
    )
    return error_message

class CustomException(Exception):
    def __init__(self,error_message,error_detail:sys):
        # Call the base class (Exception) initializer to set the basic error message
        super().__init__(error_message)
        '''
        Generate a detailed error message with file name, line number, and error message
        'error_message_detail' is a function that formats these details for easier debugging
        The 'error_detail' parameter (expected to be the sys module) provides extra error info
        '''
        self.error_message=error_message_detail(error_message,error_detail=error_detail)
        
    def __str__(self):
        return self.error_message
    
        