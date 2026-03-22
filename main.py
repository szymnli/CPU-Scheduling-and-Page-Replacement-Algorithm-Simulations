import copy
import csv
import random

import matplotlib.pyplot as plt
import numpy as np

from fcfs import FCFS
from fifo import FIFO
from lru import LRU
from process import Process
from sjf import SJF

# Generowanie danych testowych dla FCFS i SJF
random.seed(42)
num_processes = 10
test_data = [
    Process(
        pid=i + 1, arrival_time=random.randint(0, 10), burst_time=random.randint(1, 8)
    )
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


# Wykres słupkowy dla FCFS i SJF
labels = ["Avg Waiting", "Avg Turnaround", "Avg Response"]
fcfs_values = [
    fcfs_stats["avg_waiting_time"],
    fcfs_stats["avg_turnaround_time"],
    fcfs_stats["avg_response_time"],
]
sjf_values = [
    sjf_stats["avg_waiting_time"],
    sjf_stats["avg_turnaround_time"],
    sjf_stats["avg_response_time"],
]

x = np.arange(len(labels))
width = 0.35

fig, ax = plt.subplots(figsize=(8, 5))
rects1 = ax.bar(x - width / 2, fcfs_values, width, label="FCFS", color="tab:purple")
rects2 = ax.bar(x + width / 2, sjf_values, width, label="SJF", color="tab:cyan")

ax.set_ylabel("Time")
ax.set_title("Average Times: FCFS vs SJF")
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.legend()

for rect in rects1 + rects2:
    height = rect.get_height()
    ax.annotate(
        f"{height:.2f}",
        xy=(rect.get_x() + rect.get_width() / 2, height),
        xytext=(0, 3),
        textcoords="offset points",
        ha="center",
        va="bottom",
    )

plt.tight_layout()
plt.show()

# Zapis wyników FCFS i SJF do pliku CSV
with open("results/fcfs_sjf_results_1.csv", "w", newline="") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(
        [
            "PID",
            "ArrivalTime",
            "BurstTime",
            "FCFS_Start",
            "FCFS_Completion",
            "FCFS_Waiting",
            "FCFS_Turnaround",
            "FCFS_Response",
            "SJF_Start",
            "SJF_Completion",
            "SJF_Waiting",
            "SJF_Turnaround",
            "SJF_Response",
        ]
    )
    for fcfs_proc, sjf_proc in zip(fcfs.processes, sjf.processes):
        writer.writerow(
            [
                fcfs_proc.pid,
                fcfs_proc.arrival_time,
                fcfs_proc.burst_time,
                fcfs_proc.start_time,
                fcfs_proc.completion_time,
                fcfs_proc.waiting_time,
                fcfs_proc.turnaround_time,
                fcfs_proc.response_time,
                sjf_proc.start_time,
                sjf_proc.completion_time,
                sjf_proc.waiting_time,
                sjf_proc.turnaround_time,
                sjf_proc.response_time,
            ]
        )

# Parametry dane do FIFO i LRU
num_seeds = 10
num_frames = 3
reference_length = 30

fifo_faults_list = []
lru_faults_list = []
seed_labels = []

# Generowanie danych testowych oraz uruchamianie algorytmów FIFO i LRU
for seed in range(num_seeds):
    random.seed(seed)
    reference_string = [random.randint(0, 9) for _ in range(reference_length)]
    # reference_string = [1, 2, 1, 3, 1, 4, 1, 5, 1, 6, 1, 2, 1, 3, 1, 4, 1, 5, 1, 6]
    fifo = FIFO(num_frames)
    lru = LRU(num_frames)
    fifo_faults = fifo.run(reference_string)
    lru_faults = lru.run(reference_string)
    fifo_faults_list.append(fifo_faults)
    lru_faults_list.append(lru_faults)
    seed_labels.append(f"Seed {seed}")

# Wykres słupkowy dla FIFO i LRU
x = np.arange(num_seeds)
width = 0.35

fig, ax = plt.subplots(figsize=(12, 6))
rects1 = ax.bar(x - width / 2, fifo_faults_list, width, label="FIFO", color="tab:pink")
rects2 = ax.bar(x + width / 2, lru_faults_list, width, label="LRU", color="tab:blue")

ax.set_ylabel("Page Faults")
ax.set_title("Page Faults: FIFO vs LRU")
ax.set_xticks(x)
ax.set_xticklabels(seed_labels, rotation=45)
ax.legend()

for rect in rects1 + rects2:
    height = rect.get_height()
    ax.annotate(
        f"{height}",
        xy=(rect.get_x() + rect.get_width() / 2, height),
        xytext=(0, 3),
        textcoords="offset points",
        ha="center",
        va="bottom",
    )

plt.tight_layout()
plt.show()

# Zapis wyników FIFO i LRU do pliku CSV
with open("results/fifo_lru_results_1.csv", "w", newline="") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Seed", "FIFO_PageFaults", "LRU_PageFaults"])
    for seed, fifo_faults, lru_faults in zip(
        seed_labels, fifo_faults_list, lru_faults_list
    ):
        writer.writerow([seed, fifo_faults, lru_faults])
