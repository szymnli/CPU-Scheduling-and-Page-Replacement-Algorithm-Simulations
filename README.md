# CPU Scheduling and Page Replacement Algorithm Simulations

## Introduction
The goal of this report is to analyze and compare selected CPU scheduling and page replacement algorithms. The algorithms chosen for simulation are FCFS and SJF for CPU scheduling, and FIFO and LRU for page replacement. The algorithms were implemented in Python, with visualizations generated using the matplotlib library.

## CPU Scheduling Algorithm Simulations
When a process in memory enters a waiting state, the operating system reclaims CPU resources and assigns them to another process. CPU scheduling is one of the fundamental functions of any operating system.

The main goals of scheduling algorithms include minimizing process waiting and execution times, and maintaining a balance between system performance and responsiveness. In practice, various scheduling algorithms are implemented, each with distinct advantages and limitations, tailored to specific system requirements.

FCFS and SJF were selected for simulation due to their clear operational differences and straightforward implementation, which allows for a transparent comparison of results.

### FCFS (First-Come, First-Served)
FCFS is the simplest CPU scheduling algorithm, which executes processes from start to finish in the order they arrive. FCFS is a non-preemptive strategy (it does not interrupt a running process).

#### Advantages
- Waiting time can be estimated based on the queue
- No process starvation (every process will eventually be served)
- Simple to implement and understand

#### Disadvantages
- Potentially long waiting times for short processes
- Poor average performance
- No priority support

### SJF (Shortest Job First)
SJF is a non-preemptive process scheduling method that optimizes CPU utilization by prioritizing tasks with the shortest execution time. Its goal is to minimize the average task processing time.

#### Advantages
- Minimizes average waiting time
- Increases system throughput (executes more short tasks, increasing the number of completed processes)

#### Disadvantages
- Can lead to starvation of long processes
- Predicting execution time is complex

### Test Data
Simulations were run on three randomly generated datasets of varying sizes. The code below generates a list of processes used as input for both algorithms. `num_processes` defines the number of processes to generate; `burst_time` and `arrival_time` are randomly selected values representing process duration and arrival time respectively.
```python
random.seed(42)
num_processes = 10
test_data = [
    Process(pid=i+1, arrival_time=random.randint(0, 10), burst_time=random.randint(1, 8))
    for i in range(num_processes)
]
```

### Results
1. 10 processes, seed 42
![10 processes](img/fcfs_sjf_10.png)
2. 100 processes, seed 43
![100 processes](img/fcfs_sjf_100.png)
3. 10,000 processes, seed 44
![10,000 processes](img/fcfs_sjf_10000.png)

### Conclusions
For small, medium, and large process counts with varied execution times, SJF clearly outperforms FCFS. Average waiting time, response time, and turnaround time are significantly lower than in FCFS. Waiting time equals response time in both algorithms, since processes wait their turn without interruption.

- For a small number of processes (10), SJF provides on average 38.4% shorter waiting and response times, and 29.9% shorter turnaround compared to FCFS — the largest difference across all tested cases.
- With 100 processes, the differences narrow slightly but remain significant: on average 36.6% shorter waiting and response times, and 35.9% shorter turnaround.
- For a large number of processes (10,000), SJF still performs better, offering 29.4% shorter waiting, response, and turnaround times compared to FCFS.

FCFS, despite its simplicity, proves inefficient in practice. The convoy effect forces shorter processes to wait unnecessarily for longer ones to finish, significantly degrading performance — especially with a small number of tasks. As the number of processes increases, FCFS efficiency improves slightly, but it remains less effective than SJF.

## Page Replacement Algorithm Simulations
Memory paging in operating systems is a memory management approach in which the computer stores and retrieves data from secondary storage for use in primary memory. The operating system moves data in standardized fixed-size blocks (pages), enabling efficient organization of the address space.

The assumption that only a subset of each process's pages needs to be in memory can lead to over-allocation — too many processes in memory and no free frames remaining. To avoid blocking a process that requires another frame, page replacement is used.

FIFO and LRU were selected for simulation due to their fundamental differences in memory management.

### FIFO (First In, First Out)
FIFO is the simplest page replacement algorithm. It maintains all pages in a queue, with the oldest page at the front. When all frames are occupied, FIFO evicts the first page in the queue.

#### Advantages
- Simple to implement
- Low computational overhead
- Predictable behavior (the oldest page is always evicted)

#### Disadvantages
- Does not account for page usage frequency (may evict pages that are still needed)

### LRU (Least Recently Used)
LRU is an algorithm that evicts the page that has not been used for the longest period of time. It is based on the assumption that pages used furthest in the past are less likely to be needed than recently used ones.

#### Advantages
- Reduces the risk of evicting needed pages
- Minimizes page faults (better exploits temporal locality)

#### Disadvantages
- More complex to implement than FIFO
- Rarely used but critical pages may still be evicted

### Test Data
Test data consists of randomly generated page reference strings with varying parameters, enabling comparison of algorithm behavior across different scenarios. `num_seeds` defines the number of seeds to compare, `num_frames` specifies how many pages can reside in memory simultaneously, and `reference_length` sets the length of generated reference strings. One simulation also uses a static page reference string with a clearly dominant frequently-used page.
```python
num_seeds = 10
num_frames = 3
reference_length = 30

for seed in range(num_seeds):
    random.seed(seed)
    reference_string = [random.randint(0, 9) for _ in range(reference_length)]
    # reference_string = [1, 2, 1, 3, 1, 4, 1, 5, 1, 6, 1, 2, 1, 3, 1, 4, 1, 5, 1, 6]
```

### Results
1. Frames: 3, string length: 30, page count: 10, seeds: 0–9
![First comparison](img/fifo_lru_1.png)
2. Frames: 5, string length: 100, page count: 20, seeds: 0–9
![Second comparison](img/fifo_lru_2.png)
3. Frames: 10, string length: 500, page count: 50, seeds: 0–9
![Third comparison](img/fifo_lru_3.png)
4. Frames: 3, static string with a visible frequently-used page trend
![Fourth comparison](img/fifo_lru_4.png)

### Conclusions
Based on the simulations, for randomly generated page reference strings, FIFO and LRU produce very similar results — FIFO performs marginally better, likely as a result of the random nature of the test data.

For data with clear locality patterns — where certain pages are accessed frequently and in short intervals — LRU significantly outperforms FIFO in terms of page fault count. This is because FIFO operates purely on the order in which pages were loaded into memory, ignoring how often they are reused. As a result, it may evict frequently accessed pages, leading to a higher page fault rate.

LRU achieves better results in environments characterized by temporal locality, since its strategy of evicting the least recently used page keeps the most likely-to-be-reused pages in memory. This makes it more effective, especially in conditions that reflect realistic operating system workloads.

## Sources
- Dr inż. Marek Wilkus, [Systemy operacyjne Wykład 04](https://home.agh.edu.pl/~mwilkus/os/2024_W04_ITc.pdf)
- Dr inż. Marek Wilkus, [Systemy operacyjne Wykład 03N](https://home.agh.edu.pl/~mwilkus/os/2024_W03N_ITc.pdf)
- prof. dr hab. inż. Jerzy Brzeziński, dr inż. Dariusz Wawrzyniak, [Planowanie przydziału procesora](https://www.cs.put.poznan.pl/dwawrzyniak/SysOp2017/szereg1_1s.pdf)
- dr inż. Witold Paluszyński, [Szeregowanie: podstawowe pojęcia i algorytmy szeregowania, szeregowanie zadań obliczeniowych i interakcyjnych, strategie złożone](https://kcir.pwr.edu.pl/~witold/opsys/os_sched_s.pdf)
