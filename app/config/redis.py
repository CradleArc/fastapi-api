# 配置文件：RedisConfig
from app.utils.redis import RedisConfig

redis_config = RedisConfig()
redis_config.host = '127.0.0.1'
redis_config.port = '6379'
redis_config.username = 'root'
redis_config.password = '123456'
redis_config.database = 1
