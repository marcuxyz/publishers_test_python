from abc import abstractmethod

from rq import Queue
from rq.serializers import JSONSerializer

from config.redis import RedisConnection

class Publisher:
    @abstractmethod
    def publish_message(self):
        queue = Queue(connection=self.redis(), **self.queue_params())
        queue.enqueue(self.payload)

    @abstractmethod
    def queue_params(self):
        raise NotImplementedError

    @abstractmethod
    def payload(self):
        raise NotImplementedError

    def redis(self):
        return RedisConnection().connect()
