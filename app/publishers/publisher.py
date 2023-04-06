from abc import abstractmethod

from rq import Queue

from config.redis import RedisConnection


class Publisher:
    def __init__(self):
        queue = Queue(connection=self.redis(), **self.queue_params())
        queue.enqueue(self.perform)

        self.queue_ids = queue.get_job_ids()

    @abstractmethod
    def perform(self):
        raise NotImplementedError

    @abstractmethod
    def queue_params(self):
        raise NotImplementedError

    def redis(self):
        redis = RedisConnection()

        return redis.connect()
