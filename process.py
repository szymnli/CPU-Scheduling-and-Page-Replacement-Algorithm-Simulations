class Process:
    def __init__(self, pid, arrival_time, burst_time):
        self.pid = pid
        self.arrival_time = arrival_time
        self.burst_time = burst_time
        
        self.start_time = None
        self.completion_time = None
        self.waiting_time = None
        self.turnaround_time = None
        self.response_time = None

    def calculate_times(self, current_time):
        self.turnaround_time = self.completion_time - self.arrival_time
        self.waiting_time = self.turnaround_time - self.burst_time
        self.response_time = self.start_time - self.arrival_time

    def __repr__(self):
        return f"Process({self.pid}, {self.arrival_time}, {self.burst_time})"