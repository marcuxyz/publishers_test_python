import json

from abc import abstractmethod

from rq import Queue

from config.redis import RedisConnection


class Publisher:
    @abstractmethod
    def publish_message(self):
        queue = Queue(connection=self.redis(), **self.queue())
        queue.enqueue(json.dumps(self.payload()))

    @abstractmethod
    def queue(self):
        raise NotImplementedError

    @abstractmethod
    def payload(self):
        raise NotImplementedError

    def redis(self):
        return RedisConnection().connect()
