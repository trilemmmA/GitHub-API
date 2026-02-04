import logging
import time
from functools import wraps

# LOGGING

logger = logging.getLogger("actions.log")
logger.setLevel(logging.INFO)

if logger.handlers:
    logger.handlers.clear()
    
formatter = logging.Formatter(
    fmt="[%(asctime)s] [%(levelname)s] %(message)s",
    datefmt="%Y:%m:%d %H:%M:%S"
)

file_handler = logging.FileHandler("actions.log", mode="a", encoding='utf-8')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

def call_log(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
               
        logger.info(f"call '{func.__name__}' started")
        
        try:
            result = func(*args, **kwargs)
            
            end_time = time.time()
            duration = end_time - start_time
            
            logger.info(f"'{func.__name__}' Completed in {duration:.4f}s")
            return result
        
        except Exception as e:
            end_time = time.time()
            duration = end_time - start_time
            
            logger.error(f"'{func.__name__}' Failed with: {e} duration: {duration:.4f}s")
            raise
        
    return wrapper
