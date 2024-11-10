"""Project classes."""
from datetime import datetime


class Project:
    def __init__(self, name, start_date, priority, completion):
        self.name = name
        self.start_date = datetime.strptime(start_date, '%Y-%m-%d')
        self.priority = int(priority)
        self.completion = int(completion)

    def __str__(self):
        return f"{self.name}, start: {self.start_date.date()}, priority: {self.priority}, completion: {self.completion}%"

    def is_completed(self):
        return self.completion == 100

    # Custom sort by priority (lower number means higher priority)
    def __lt__(self, other):
        return self.priority < other.priority
