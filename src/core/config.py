from pathlib import Path

# ES配置
ELASTICSEARCH_URL = "http://elasticsearch:9200"

# 日志配置
LOG_DIR = Path("logs")
LOG_FILE = LOG_DIR / "app.log"