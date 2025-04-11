# ELK-Log-Gateway

ELK-Log-Gateway 是一个基于 FastAPI 和 ELK Stack 构建的日志管理原型演示系统，在提供统一的日志收集、查询和管理功能之外，支持通过API的方式直接访问 Elasticsearch 获取日志便于编程处理。

## 功能特点

- 支持多种日志格式和索引模式
- 提供统一的 REST API 接口
- 实时日志收集和查询
- 支持多维度日志搜索
- 自动生成测试日志数据

## 技术栈

- FastAPI
- Elasticsearch
- Logstash
- Kibana
- Docker & Docker Compose

## 快速开始

### 环境要求

- Docker
- Docker Compose
- Python 3.10+

### 安装部署

1. 克隆项目
```bash
git clone https://github.com/OSpoon/ELK-Log-Gateway.git
cd elk-log-gateway
```

2. 启动服务
```bash
# 首次部署或代码更新后使用
docker-compose up --build

# 日常启动服务使用
docker-compose up -d
```

3. 访问服务
- API 服务：http://localhost:8000
- Kibana：http://localhost:5601

## API 接口

### 日志查询

```bash
GET /logs

参数：
- start_time: 开始时间（ISO格式，例如：2023-12-20T14:30:00.000Z）
- end_time: 结束时间（ISO格式，例如：2023-12-20T14:30:00.000Z）
- level: 日志级别
- content: 搜索内容
- index_pattern: 索引模式（FASTAPI/APPLICATION/SYSTEM）
- page: 页码
- size: 每页大小
```

## 索引模式

支持以下索引模式：
- FASTAPI: API服务日志
- APPLICATION: 应用服务日志
- SYSTEM: 系统监控日志

## 项目结构

```
.
├── src/
│   ├── api/          # API 路由
│   ├── core/         # 核心配置
│   ├── models/       # 数据模型
│   └── services/     # 业务逻辑
├── logstash/         # Logstash 配置
├── logs/             # 日志文件
├── docker-compose.yml
└── Dockerfile
```

## 开发说明

项目使用 FastAPI 框架开发，采用模块化设计，便于扩展和维护。主要模块：

- 日志收集：通过 Logstash 收集应用日志
- 日志存储：使用 Elasticsearch 存储和索引日志
- 日志查询：提供统一的 REST API 接口
- 可视化：通过 Kibana 进行日志可视化

## License

MIT
