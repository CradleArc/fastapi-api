# 配置文件：MongoConfig
from app.utils.mongo import MongoConfig

mongo_config = MongoConfig()
mongo_config.host = '127.0.0.1'
mongo_config.port = '27017'
# mongo_config.username = 'root'
# mongo_config.password = '1q2w3e4R'
mongo_config.database = 'fastapi_demo'
