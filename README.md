# CPU Scheduling & Page Replacement Simulations

Python simulations benchmarking **FCFS vs SJF** (CPU scheduling) and **FIFO vs LRU** (page replacement) across varied workloads, with matplotlib visualizations and CSV export.

## Project Structure
```
.
├── main.py          # Entry point
├── scheduling.py    # FCFS vs SJF simulation and plotting
├── paging.py        # FIFO vs LRU simulation and plotting
├── fcfs.py          # FCFS algorithm
├── sjf.py           # SJF algorithm
├── fifo.py          # FIFO page replacement
├── lru.py           # LRU page replacement
├── process.py       # Process data class
└── results/         # CSV output (git-ignored)
```

## Usage
```bash
pip install -r requirements.txt
python main.py
```

Charts are displayed inline. CSV results are saved to `results/`.

To run with custom parameters, call the simulation functions directly:
```python
from scheduling import run_scheduling
from paging import run_paging

run_scheduling(num_processes=100, seed=43)
run_paging(num_seeds=10, num_frames=5, reference_length=100)
```

## Algorithms

### CPU Scheduling

| Algorithm | Strategy | Preemptive |
|-----------|----------|------------|
| FCFS | Execute in arrival order | No |
| SJF | Execute shortest burst time first | No |

### Page Replacement

| Algorithm | Strategy |
|-----------|----------|
| FIFO | Evict the oldest loaded page |
| LRU | Evict the least recently used page |

## Results

### FCFS vs SJF

SJF consistently outperforms FCFS across all dataset sizes. The convoy effect in FCFS — short processes blocked behind long ones — is the primary driver of the gap.

| Processes | Waiting / Response improvement | Turnaround improvement |
|-----------|-------------------------------|------------------------|
| 10        | −38.4%                        | −29.9%                 |
| 100       | −36.6%                        | −35.9%                 |
| 10,000    | −29.4%                        | −29.4%                 |

![10 processes](img/fcfs_sjf_10.png)
![100 processes](img/fcfs_sjf_100.png)
![10,000 processes](img/fcfs_sjf_10000.png)

### FIFO vs LRU

On random reference strings, both algorithms perform similarly. FIFO edges ahead slightly — random data has no temporal locality for LRU to exploit.

On structured strings with a frequently-accessed page, LRU significantly reduces page faults by keeping hot pages in memory. FIFO evicts based purely on load order and misses them repeatedly.

![Random, 3 frames, length 30](img/fifo_lru_1.png)
![Random, 5 frames, length 100](img/fifo_lru_2.png)
![Random, 10 frames, length 500](img/fifo_lru_3.png)
![Structured string with temporal locality](img/fifo_lru_4.png)

## Key Takeaways

- SJF's advantage over FCFS shrinks as process count grows but never disappears
- LRU's advantage over FIFO is invisible on random data — workload shape is what matters
- Benchmarking OS algorithms requires realistic access patterns to surface meaningful differences

## Tech Stack

- Python 3
- `matplotlib` — visualizations  
- `numpy` — bar chart positioning
- `csv` — result export
