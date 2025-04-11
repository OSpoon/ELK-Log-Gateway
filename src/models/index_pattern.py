from enum import Enum

class IndexPattern(str, Enum):
    FASTAPI = "fastapi-logs-*"
    APPLICATION = "application-logs-*"
    SYSTEM = "system-logs-*"
    ALL = "*"