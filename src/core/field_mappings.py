from src.models.index_pattern import IndexPattern

FIELD_MAPPINGS = {
    IndexPattern.FASTAPI: {
        "timestamp": "timestamp",
        "level": "level",
        "message": "message",
        "path": "path",
        "method": "method"
    },
    IndexPattern.APPLICATION: {
        "timestamp": "timestamp",
        "level": "log_level",
        "message": "content",
        "path": "api_path",
        "method": "http_method"
    },
    IndexPattern.SYSTEM: {
        "timestamp": "timestamp",
        "level": "severity",
        "message": "log_message",
        "path": "source_path",
        "method": "operation"
    }
}