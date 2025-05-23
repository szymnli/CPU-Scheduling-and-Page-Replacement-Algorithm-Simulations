# Sprawozdanie
...
## Symulacje algorytmów planowania czasu procesora
Do przeprowadzenia symulacji zostały wybrane algorytmy FCFS oraz SJF, ze względu na ich wyraźne różnice w działaniu, a także prostotę implementacji, która umożliwia klarowne porównanie wyników. Symulacje zostały wykonane w języku Python, do porównania oraz wizualizacji wyników zostały wykorzystane biblioteki matplotlib oraz numpy. 
### FCFS (First-Come, First-Served)
Algorytn FCFS jest znany z jego prostoty, tak jak nazwa wskazuje procesy są obsługiwane w kolejności w której pojawiły się w kolejce.
#### Zalety
- Można oszacować czas oczekiwania na podstawie kolejki
- Procesy nie są głodzone, każdy zostanie obsłużony
- Łatwa implementacja oraz zrozumienie
#### Wady
- Możliwy długi czas oczekiwania dla krótkich procesów
- Słaba średnia wydajność 
- Brak priorytetów
### SJF (Shortest Job First)
Algorytm SJF to metoda planowania procesów, która optymalizuje wykorzystanie procesora poprzez priorytetowe wykonywanie zadań o najkrótszym czasie wykonania.
#### Zalety
- Minimalizacja średniego czasu oczekiwania
- Zwiększa przepustowość systemu, częściej wykonuje krótkie zadania, zwiększając liczbę okończonych procesów
#### Wady
- Może prowadzić do głodzenia długich procesów
- Skompliwany proces przewidywania czasu wykonania
### Dane testowe
Symulacje zostały wykonane na trzech losowo wygenerowanych zbiorach danych o różnej wielkości. Poniższy kod generuje listę procesów o podanej liczbię elementów, która jest następnie wykorzystywana jako dane wejściowe dla obu algorytmów.
```
random.seed(42)
num_processes = 10
test_data = [
    Process(pid=i+1, arrival_time=random.randint(0, 10), burst_time=random.randint(1, 8))
    for i in range(num_processes)
]
```
### Wyniki
1. 10 procesów
![10 procesów](img/fcfs_sjf_10.png)
SJF jest wyraźnie lepszy, średni czas oczekiwania oraz turnaround są znacząco niższe niż w FCFS. Czas oczekiwania jest równy czasowi odpowiedzi, ponieważ w obu algorytmach procesy czekają na swoją kolej bez przerw.
2. 100 procesów
![100 procesów](img/fcfs_sjf_100.png)
SJF nadal przeważa chociaż różnice stają się mniej dramatyczne.
3. 10000 procesów
![10000 procesów](img/fcfs_sjf_10000.png)
FCFS dalej widocznie gorzej sobie radzi niż SJF ale różnice ciągle maleją.
### Wnioski
SJF jest optymalny dla małej, średniej oraz dużej liczby procesów przy zróżnicowanych czasach wykonania. FCFS jest prostszym algorytmem ale nawet przy małym obciążeniu ma problemy z wydajnością ze względu na "efekt konwoju", blokowanie kolejki jednym długim procesem do momentu jego zakończenia.
## Symulacje algorytmów zastępowania stron
### FIFO (First In, First Out)
...
### LRU (Least Recently Used)
...
