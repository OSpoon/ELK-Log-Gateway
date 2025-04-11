import httpx

from datetime import datetime, timedelta
from fastapi import HTTPException
from src.core.config import ELASTICSEARCH_URL
from src.core.field_mappings import FIELD_MAPPINGS
from src.models.index_pattern import IndexPattern

async def query_logs(
    start_time: str = None,
    end_time: str = None,
    level: str = None,
    content: str = None,
    index_pattern: IndexPattern = IndexPattern.FASTAPI,
    page: int = 1,
    size: int = 10
):
    if not start_time:
        end_time = datetime.now().isoformat()
        start_time = (datetime.now() - timedelta(days=1)).isoformat()

    field_mapping = FIELD_MAPPINGS.get(index_pattern, FIELD_MAPPINGS[IndexPattern.FASTAPI])
    
    query = build_query(start_time, end_time, level, content, field_mapping, page, size)

    try:
        async with httpx.AsyncClient() as client:
            response = await client.post(
                f"{ELASTICSEARCH_URL}/{index_pattern.value}/_search",
                json=query
            )
            
            if response.status_code != 200:
                raise HTTPException(status_code=response.status_code, detail="查询失败")

            return process_response(response.json(), page, size)

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"获取日志失败: {str(e)}")

def build_query(start_time, end_time, level, content, field_mapping, page, size):
    query = {
        "query": {
            "bool": {
                "must": [
                    {"range": {field_mapping["timestamp"]: {"gte": start_time, "lte": end_time}}}
                ]
            }
        },
        "sort": [{field_mapping["timestamp"]: "desc"}],
        "from": (page - 1) * size,
        "size": size
    }

    if level:
        query["query"]["bool"]["must"].append(
            {"match": {field_mapping["level"]: level}}
        )
    
    if content:
        query["query"]["bool"]["must"].append({
            "multi_match": {
                "query": content,
                "fields": [
                    field_mapping["message"],
                    field_mapping["path"],
                    field_mapping["method"]
                ],
                "type": "phrase_prefix"
            }
        })
    
    return query

def process_response(data, page, size):
    hits = data.get("hits", {})
    return {
        "total": hits.get("total", {}).get("value", 0),
        "page": page,
        "size": size,
        "logs": [hit["_source"] for hit in hits.get("hits", [])]
    }