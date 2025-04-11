import logging

from datetime import datetime
from pythonjsonlogger import jsonlogger
from .config import LOG_DIR, LOG_FILE

# 创建logs目录
LOG_DIR.mkdir(exist_ok=True)

class CustomJsonFormatter(jsonlogger.JsonFormatter):
    def add_fields(self, log_record, record, message_dict):
        super(CustomJsonFormatter, self).add_fields(log_record, record, message_dict)
        log_record['timestamp'] = datetime.now().isoformat()
        log_record['level'] = record.levelname

def setup_logger():
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)
    
    file_handler = logging.FileHandler(LOG_FILE)
    file_handler.setLevel(logging.INFO)
    
    formatter = CustomJsonFormatter('%(timestamp)s %(level)s %(name)s %(message)s')
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)
    
    return logger

logger = setup_logger()