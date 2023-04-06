import json

from .publisher import Publisher


class TaskPublisher(Publisher):
    def __init__(self, title, content):
        self.title = title
        self.content = content

        super().__init__()

    def perform(self):
        return self.count_words()

    def queue_params(self):
        return {"name": "default"}

    def count_words(self):
        return len(self.payload())

    def payload(self):
        return json.dumps(
            {
                "title": self.title,
                "content": self.content,
            }
        )
