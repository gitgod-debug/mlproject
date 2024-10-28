import logging
import os
from datetime import datetime

# Generate a log file name with the current date and time, e.g., "08_27_2024_14_35_22.log"
LOG_FILE=f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

# Create a directory path for logs, placing the log file in a "logs" folder within the current directory
logs_path=os.path.join(os.getcwd(),"logs",LOG_FILE)

# Create the logs directory if it doesn't already exist
os.makedirs(logs_path,exist_ok=True)

# Define the full path for the log file including the directory and file name
LOG_FILE_PATH=os.path.join(logs_path,LOG_FILE)

logging.basicConfig(
    filename=LOG_FILE_PATH, # Set the log file location
    format="[%(asctime)s] %(lineno)d %(name)s -%(levelname)s - %(message)s", # Log format including time, line number, module name, log level, and message
    level=logging.DEBUG, # Set the log level to DEBUG to capture all types of log messages
)

if __name__=="__main__":
    logging.info("logging has started")