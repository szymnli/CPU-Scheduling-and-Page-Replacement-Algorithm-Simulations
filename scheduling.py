import copy
import csv
import random

import matplotlib.pyplot as plt
import numpy as np

from fcfs import FCFS
from process import Process
from sjf import SJF


def run_scheduling(num_processes=10, seed=42):
    # Generate test data for FCFS and SJF
    random.seed(seed)
    test_data = [
        Process(
            pid=i + 1,
            arrival_time=random.randint(0, 10),
            burst_time=random.randint(1, 8),
        )
        for i in range(num_processes)
    ]

    # Deep copy so both algorithms get identical, independent input
    fcfs_processes = copy.deepcopy(test_data)
    sjf_processes = copy.deepcopy(test_data)

    # Run FCFS
    fcfs = FCFS(fcfs_processes)
    fcfs.run()
    fcfs_stats = fcfs.get_stats()

    # Run SJF
    sjf = SJF(sjf_processes)
    sjf.run()
    sjf_stats = sjf.get_stats()

    _plot_scheduling(fcfs_stats, sjf_stats)
    _save_scheduling_csv(fcfs, sjf, seed)


def _plot_scheduling(fcfs_stats, sjf_stats):
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


def _save_scheduling_csv(fcfs, sjf, seed):
    path = f"results/fcfs_sjf_results_{seed}.csv"
    with open(path, "w", newline="") as csvfile:
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
