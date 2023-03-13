import redis
import json

class RedisDB:
    def __init__(self, host, port, db, username, password) -> None:
        self.host = host
        self.port = port
        self.db = db
        self.username = username
        self.password = password
        self.pool = redis.ConnectionPool(host=self.host, port=self.port, db=self.db, username=self.username, password=self.password)
        
    def set(self, key, value) -> None:
        r = redis.Redis(connection_pool=self.pool)
        r.set(key, value)

    def get(self, key) -> str:
        r = redis.Redis(connection_pool=self.pool)
        return r.get(key)
    
    def delete(self, key) -> None:
        r = redis.Redis(connection_pool=self.pool)
        r.delete(key)

    def exists(self, key) -> bool:
        r = redis.Redis(connection_pool=self.pool)
        return r.exists(key)
    
    def keys(self) -> list:
        r = redis.Redis(connection_pool=self.pool)
        return r.keys()
    
    def flush(self) -> None:
        r = redis.Redis(connection_pool=self.pool)
        r.flushdb()

    def get_all(self) -> dict:
        return {key.decode("utf-8"): self.get(key).decode("utf-8") for key in self.keys()}
    
    def get_all_json(self) -> str:
        return json.dumps(self.get_all())
    
    
if __name__ == "__main__":
    # redis-17710.c16.us-east-1-2.ec2.cloud.redislabs.com:17710
    # ITESM-free-db
    #print(db.keys())