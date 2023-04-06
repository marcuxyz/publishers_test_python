from rq.worker import SimpleWorker

class TaskWorker(SimpleWorker):
    def work(self, *args, **kwargs):
        return super().work(*args, **kwargs)