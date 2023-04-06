from app.publishers.task_publisher import TaskPublisher
from rq import Queue
from rq.job import Job
from redis import Redis

publisher = TaskPublisher(
    title="Ligar para a amazon", content="content example"
)
jobs = Job.fetch_many(publisher.queue_ids, connection=Redis())
for job in jobs:
    print(job.result)
