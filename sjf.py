from process import Process

class SJF:
    def __init__(self, processes):
        self.processes = processes

    def run(self):
        n = len(self.processes)
        completed = 0
        current_time = 0
        is_completed = [False] * n
        processes = self.processes[:]
        while completed < n:
            # Znajdowanie procesów, które przybyły i nie zostały jeszcze zakończone
            available = [p for i, p in enumerate(processes) if p.arrival_time <= current_time and not is_completed[i]]
            if available:
                # Wybieranie procesu o najkrótszym czasie przybycia
                shortest = min(available, key=lambda p: p.burst_time)
                idx = processes.index(shortest)
                shortest.start_time = current_time
                shortest.completion_time = current_time + shortest.burst_time
                shortest.calculate_times(current_time)
                current_time = shortest.completion_time
                is_completed[idx] = True
                completed += 1
            else:
                # Przesunięcie czasu, jeśli nie ma dostępnych procesów
                current_time += 1

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
