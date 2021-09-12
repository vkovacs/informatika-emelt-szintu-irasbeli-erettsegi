class Entry:
    def __init__(self, hour, minute, actor_id, direction):
        self.hour = hour
        self.minute = minute
        self.actor_id = actor_id
        self.direction = direction

    def __str__(self):
        return self.hour + " " + self.minute + " " + self.actor_id + " " + self.direction
