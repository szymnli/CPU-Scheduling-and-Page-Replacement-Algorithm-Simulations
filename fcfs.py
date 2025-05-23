from process import Process

class FCFS:
    def __init__(self, processes):
        # Sortowanie procesów według czasu przybycia
        self.processes = sorted(processes, key=lambda p: p.arrival_time)

    def run(self):
        current_time = 0
        for process in self.processes:
            # Zmiana czasu przybycia jeśli CPU czeka na proces
            if current_time < process.arrival_time:
                current_time = process.arrival_time
            process.start_time = current_time
            process.completion_time = current_time + process.burst_time
            process.calculate_times(current_time)
            current_time = process.completion_time

    def get_stats(self):
        n = len(self.processes)
        avg_waiting = sum(p.waiting_time for p in self.processes) / n
        avg_turnaround = sum(p.turnaround_time for p in self.processes) / n
        avg_response = sum(p.response_time for p in self.processes) / n
        return {
            "avg_waiting_time": avg_waiting,
            "avg_turnaround_time": avg_turnaround,
            "avg_response_time": avg_response
        }
