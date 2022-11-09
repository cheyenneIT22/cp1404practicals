"""Project classes."""
import datetime


class project:
    def __init__(self, start_date, priority, cost_estimate, percent_complete):
        self.start_date = start_date
        self.priority = priority
        self.cost_estimate = cost_estimate
        self.percent_complete = percent_complete

    def __repr__(self):
        return f"{self.name}, start: {self.start_date}, priority: {self.priority}, cost: {self.cost_estimate}, percentage: {self.percent_complete}"

    def __it__(self,other):
        return self.priority <other.priority>
    def is_complete(self):
        return self.percent_complete == 100

