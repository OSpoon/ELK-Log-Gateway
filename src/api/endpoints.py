import asyncio
from fastapi import APIRouter
from typing import Optional
from src.models.index_pattern import IndexPattern
from src.services.log_query import query_logs
from src.services.log_generator import generate_test_log

router = APIRouter()

@router.get("/logs")
async def get_logs(
    start_time: Optional[str] = None,
    end_time: Optional[str] = None,
    level: Optional[str] = None,
    content: Optional[str] = None,
    index_pattern: IndexPattern = IndexPattern.FASTAPI,
    page: int = 1,
    size: int = 10
):
    """
    获取日志列表
    
    参数说明：
    - start_time: 开始时间，ISO格式，例如：2023-12-20T14:30:00.000Z
    - end_time: 结束时间，ISO格式，例如：2023-12-20T15:30:00.000Z
    - level: 日志级别，可选值：INFO、WARNING、ERROR、DEBUG
    - content: 搜索内容，支持对消息内容、路径和方法的模糊搜索
    - index_pattern: 索引模式，可选值：FASTAPI、APPLICATION、SYSTEM
    - page: 页码，默认为1
    - size: 每页大小，默认为10
    """
    return await query_logs(
        start_time, end_time, level, content, 
        index_pattern, page, size
    )

async def background_task():
    while True:
        for index_type in [IndexPattern.FASTAPI, IndexPattern.APPLICATION, IndexPattern.SYSTEM]:
            await generate_test_log(index_type)
        await asyncio.sleep(5)