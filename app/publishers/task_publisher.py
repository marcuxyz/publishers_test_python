from .publisher import Publisher


class TaskPublisher(Publisher):
    def call(self):
        self.publish_message()

    def queue(self):
        return {"name": "task"}

    def payload(self):
        return dict(
            title="Ligar para a amazon",
            body="ás 18:00 do sábado 01/04/2023",
        )
