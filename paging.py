import csv
import random

import matplotlib.pyplot as plt
import numpy as np

from fifo import FIFO
from lru import LRU


def run_paging(num_seeds=10, num_frames=3, reference_length=30):
    fifo_faults_list = []
    lru_faults_list = []
    seed_labels = []

    for seed in range(num_seeds):
        random.seed(seed)
        reference_string = [random.randint(0, 9) for _ in range(reference_length)]
        # Uncomment to test with a structured string that has clear temporal locality:
        # reference_string = [1, 2, 1, 3, 1, 4, 1, 5, 1, 6, 1, 2, 1, 3, 1, 4, 1, 5, 1, 6]

        fifo = FIFO(num_frames)
        lru = LRU(num_frames)

        fifo_faults_list.append(fifo.run(reference_string))
        lru_faults_list.append(lru.run(reference_string))
        seed_labels.append(f"Seed {seed}")

    _plot_paging(fifo_faults_list, lru_faults_list, seed_labels, num_seeds)
    _save_paging_csv(seed_labels, fifo_faults_list, lru_faults_list, num_frames)


def _plot_paging(fifo_faults_list, lru_faults_list, seed_labels, num_seeds):
    x = np.arange(num_seeds)
    width = 0.35

    fig, ax = plt.subplots(figsize=(12, 6))
    rects1 = ax.bar(
        x - width / 2, fifo_faults_list, width, label="FIFO", color="tab:pink"
    )
    rects2 = ax.bar(
        x + width / 2, lru_faults_list, width, label="LRU", color="tab:blue"
    )

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


def _save_paging_csv(seed_labels, fifo_faults_list, lru_faults_list, num_frames):
    path = f"results/fifo_lru_results_{num_frames}frames.csv"
    with open(path, "w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Seed", "FIFO_PageFaults", "LRU_PageFaults"])
        for seed, fifo_faults, lru_faults in zip(
            seed_labels, fifo_faults_list, lru_faults_list
        ):
            writer.writerow([seed, fifo_faults, lru_faults])
