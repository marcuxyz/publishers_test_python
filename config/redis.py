from redis import Redis


class RedisConnection:
    def __init__(
        self, host: str = "localhost", port: int = 6379, db=0
    ) -> None:
        self.host = host
        self.port = port
        self.db = db

    def connect(self):
        return Redis(host=self.host, port=self.port, db=self.db)
