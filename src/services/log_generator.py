import httpx

from datetime import datetime
from src.core.config import ELASTICSEARCH_URL
from src.core.logger import logger
from src.models.index_pattern import IndexPattern

INDEX_LOG_TEMPLATES = {
    IndexPattern.FASTAPI: {
        "message": "API请求处理",
        "path": "/api/process",
        "method": "POST",
        "level": "INFO"
    },
    IndexPattern.APPLICATION: {
        "message": "应用状态更新",
        "path": "/app/status",
        "method": "PUT",
        "level": "WARNING"
    },
    IndexPattern.SYSTEM: {
        "message": "系统资源监控",
        "path": "/system/monitor",
        "method": "GET",
        "level": "ERROR"
    }
}

async def generate_test_log(index_type: IndexPattern):
    try:
        async with httpx.AsyncClient() as client:
            template = INDEX_LOG_TEMPLATES[index_type]
            
            test_log = {
                "timestamp": datetime.now().isoformat(),
                "level": template["level"],
                "message": template["message"],
                "path": template["path"],
                "method": template["method"]
            }
            
            index_name = index_type.value.replace("*", datetime.now().strftime("%Y.%m.%d"))
            
            await client.post(
                f"{ELASTICSEARCH_URL}/{index_name}/_doc",
                json=test_log
            )
            
    except Exception as e:
        logger.error(f"生成测试日志失败: {str(e)}")