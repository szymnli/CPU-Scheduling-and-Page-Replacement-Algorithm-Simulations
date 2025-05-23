from process import Process
from fcfs import FCFS
from sjf import SJF
import copy
import random
import matplotlib.pyplot as plt
import numpy as np

# Generowanie danych testowych
random.seed(44)
num_processes = 10000
test_data = [
    Process(pid=i+1, arrival_time=random.randint(0, 10), burst_time=random.randint(1, 8))
    for i in range(num_processes)
]

# Kopia danych do FCFS i SJF
fcfs_processes = copy.deepcopy(test_data)
sjf_processes = copy.deepcopy(test_data)

# FCFS
fcfs = FCFS(fcfs_processes)
fcfs.run()
fcfs_stats = fcfs.get_stats()

# SJF
sjf = SJF(sjf_processes)
sjf.run()
sjf_stats = sjf.get_stats()

# Statystyki
print("FCFS Stats:", fcfs_stats)
print("SJF Stats:", sjf_stats)

# Wykres słupkowy
labels = ['Avg Waiting', 'Avg Turnaround', 'Avg Response']
fcfs_values = [
    fcfs_stats['avg_waiting_time'],
    fcfs_stats['avg_turnaround_time'],
    fcfs_stats['avg_response_time']
]
sjf_values = [
    sjf_stats['avg_waiting_time'],
    sjf_stats['avg_turnaround_time'],
    sjf_stats['avg_response_time']
]

x = np.arange(len(labels))
width = 0.35

fig, ax = plt.subplots(figsize=(8, 5))
rects1 = ax.bar(x - width/2, fcfs_values, width, label='FCFS', color='tab:purple')
rects2 = ax.bar(x + width/2, sjf_values, width, label='SJF', color='tab:cyan')

ax.set_ylabel('Time')
ax.set_title('Average Times: FCFS vs SJF')
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.legend()

for rect in rects1 + rects2:
    height = rect.get_height()
    ax.annotate(f'{height:.2f}',
                xy=(rect.get_x() + rect.get_width() / 2, height),
                xytext=(0, 3),
                textcoords="offset points",
                ha='center', va='bottom')

plt.tight_layout()
plt.show()