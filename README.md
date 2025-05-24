# Symulacje algorytmów planowania procesora i zastępowania stron
## Wstęp
Celem tego sprawozdania jest analiza i porównanie wybranych algorytmów planowania czasu procesora oraz zastępowania stron w pamięci operacyjnej. Do symulacji zostały wybrane algorytmy FCFS i SJF oraz FIFO i LRU. Implementacja algorytmów została wykonana w języku Python, a wizualizacja za pomocą biblioteki matplotlib.
## Symulacje algorytmów planowania czasu procesora
Kiedy proces w pamięci operacyjnej przechodzi w stan oczekiwania, system operacyjny odbiera mu zasoby procesora i przekazuje do dyspozycji innego procesu. Planowanie przydziału procesora jest jedną z fundamentalnych funkcji każdego systemu operacyjnego.<br><br>
Główne cele algorytmów planowania to między innymi minimalizacja czasu oczekiwania i wykonania procesów oraz utrzymanie równowagi między wydajnością a responsywnością systemu. W praktyce implementowane są różne algorytmy planowania, każdy z charakterystycznymi zaletami oraz ograniczeniami, dostosowane do konkretnych wymagań systemowych. <br><br>
Do przeprowadzenia symulacji zostały wybrane algorytmy FCFS oraz SJF, ze względu na ich wyraźne różnice w działaniu, a także prostotę implementacji, która umożliwia porównanie wyników w przejrzysty sposób.
### FCFS (First-Come, First-Served)
FCFS to najprostszy algorytm planowania procesora, który wykonuje procesy od początku do końca w takiej kolejności, w jakiej się pojawiły. FCFS jest strategią bez wywłaszczania (przerywania trwającego procesu).
#### Zalety
- Można oszacować czas oczekiwania na podstawie kolejki
- Procesy nie są głodzone (każdy zostanie obsłużony)
- Łatwa implementacja oraz zrozumienie
#### Wady
- Możliwy długi czas oczekiwania dla krótkich procesów
- Słaba średnia wydajność 
- Brak priorytetów
### SJF (Shortest Job First)
Algorytm SJF to metoda planowania procesów bez wywłaszczania, która optymalizuje wykorzystanie procesora poprzez priorytetowe wykonywanie zadań o najkrótszym czasie wykonania. Jego celem jest minimalizacja średniego czasu przetwarzania zadania.
#### Zalety
- Minimalizacja średniego czasu oczekiwania
- Zwiększa przepustowość systemu (częściej wykonuje krótkie zadania, zwiększając liczbę ukończonych procesów)
#### Wady
- Może prowadzić do głodzenia długich procesów
- Skompliwany proces przewidywania czasu wykonania
### Dane testowe
Symulacje zostały wykonane na trzech losowo wygenerowanych zbiorach danych o różnej wielkości. Poniższy kod generuje listę procesów, która jest następnie wykorzystywana jako dane wejściowe dla obu algorytmów. Num_processes określa liczbę procesów do wygenerowania, burst_time oraz arrival_time są losowo wybieranymi wartościami odpowiednio czasu trwania procesu i czasu jego przybycia.
```
random.seed(42)
num_processes = 10
test_data = [
    Process(pid=i+1, arrival_time=random.randint(0, 10), burst_time=random.randint(1, 8))
    for i in range(num_processes)
]
```
### Wyniki
1. 10 procesów, ziarno 42 <br>
![10 procesów](img/fcfs_sjf_10.png)
2. 100 procesów, ziarno 43 <br>
![100 procesów](img/fcfs_sjf_100.png)
3. 10000 procesów, ziarno 44 <br>
![10000 procesów](img/fcfs_sjf_10000.png)
### Wnioski
Dla małej, średniej jak i dużej ilości procesów, przy zróżnicowanych czasach wykonania, algorytm SJF jest wyraźnie lepszy. Średni czas oczekiwania (waiting), odpowiedzi (response) oraz cyklu przetwarzania (turnaround) są znacząco niższe niż w FCFS. Czas oczekiwania jest równy czasowi odpowiedzi, ponieważ w obu algorytmach procesy czekają na swoją kolej bez przerw. 
- Dla małej liczby procesów (10), SJF zapewnia średnio o 38,4% krótszy czas oczekiwania i odpowiedzi, oraz o 29,9% krótszy turnaround w porównaniu do FCFS. To największa różnica spośród wszystkich testowanych przypadków.
- Przy 100 procesach, różnice nieco się zmniejszają, ale nadal są znaczące: średnio 36,6% krótszy czas oczekiwania i odpowiedzi, oraz 35,9% krótszy turnaround.
- Dla dużej liczby procesów (10 000), SJF nadal wypada lepiej, oferując 29,4% krótszy czas oczekiwania, odpowiedzi i turnaround w porównaniu do FCFS. <br>
FCFS, mimo swojej prostoty, okazuje się mało efektywny w praktyce. Efekt konwoju powoduje, że krótsze procesy muszą niepotrzebnie czekać na zakończenie dłuższych, co znacznie pogarsza wydajność, zwłaszcza przy małej liczbie zadań. Wraz ze wzrostem liczby procesów efektywność FCFS nieco się poprawia, jednak nadal pozostaje mniej efektywny od SJF.
## Symulacje algorytmów zastępowania stron
Stronicowanie pamięci w systemach operacyjnych to sposób zarządzania pamięcią, w którym komputer zapisuje i pobiera dane z pamięci dodatkowej do wykorzystania w pamięci podstawowej. System operacyjny przenosi dane w postaci ustandaryzowanych bloków (stron) o stałym rozmiarze, co umożliwia efektywną organizację przestrzeni adresowej. <br><br>
Założenie, że tylko część stron każdego procesu jest potrzebna w pamięci może doprowadzić do nadprzydziału, czyli nadmiaru procesów w pamięci i całkowitego braku wolnych ramek. Aby nie blokować procesu wymagającego kolejnej ramki, stosuje się zastępowanie stron. <br><br>
Do przeprowadzenia symulacji zostały wybrane algorytmy FIFO oraz LRU. Wybrano te metody ze względu na ich fundamentalne różnice w zarządzaniu pamięcią.
### FIFO (First In, First Out)
Algorytm FIFO jest najprostszym algorytmem zastępowania stron. Jego działanie polega na trzymaniu wszystkich stron w kolejce, a najstarsza znajduje się na początku. Kiedy wszystkie ramki są zajęte, FIFO usuwa pierwszą w kolejce.
#### Zalety
- Prostota implementacji
- Niskie wymagania obliczeniowe
- Przewidywalność (zawsze zostanie usunięta najstarsza strona)
#### Wady
- Nie bierze pod uwagę użycia stron (może usuwać te które są nadal potrzebne)
### LRU (Least Recently Used)
LRU to algorytm, który usuwa z pamięci stronę, która jest od najdłuższego czasu nieużywana. Jest oparty o założenie, że strony używane dawniej są mniej potrzebne niż te, który były używane później.
#### Zalety
- Ogranicza ryzyko usunięcia potrzebnych stron
- Minimalizuje błędy strony (lepiej wykorzystuje lokalność czasową)
#### Wady
- Trudniejsza implementacja od FIFO
- Rzadko używane, ale kluczowe strony mogą być usuwane
### Dane testowe
Dane testowe składają się z losowo wygenerowanych ciągów numerów stron o zmiennych parametrach, tak aby można było porównać ze sobą działania algorytmów w różnych scenariuszach. Num_seeds odpowiada za ilość ziaren do porównania, num_frames określa, ile stron może być jednocześnie w pamięci, a reference_length wyznacza długość wygenerowanych ciągów liczbowych. Do jednej z symulacji użyto również statycznego ciągu numerów stron z widocznie najczęściej używaną stroną.
```
num_seeds = 10
num_frames = 3
reference_length = 30

for seed in range(num_seeds):
    random.seed(seed)
    reference_string = [random.randint(0, 9) for _ in range(reference_length)]
    # reference_string = [1, 2, 1, 3, 1, 4, 1, 5, 1, 6, 1, 2, 1, 3, 1, 4, 1, 5, 1, 6]
```
### Wyniki
1. Liczba ramek: 3, długość ciągów: 30, liczba stron: 10, ziarno: 0-9 <br>
![Pierwsze porównanie](img/fifo_lru_1.png) <br>
2. Liczba ramek: 5, długość ciągów: 100, liczba stron: 20, ziarno: 0-9 <br>
![Drugie porównanie](img/fifo_lru_2.png) <br>
3. Liczba ramek: 10, długość ciągów: 500, liczba stron: 50, ziarno: 0-9 <br>
![Trzecie porównanie](img/fifo_lru_3.png) <br>
4. Liczba ramek: 3, konkretny ciąg w kórym widoczny jest trend najczęściej używanej strony <br>
![Czwarte porównanie](img/fifo_lru_4.png) <br>
### Wnioski
Na podstawie przeprowadzonych symulacji można zauważyć, że w przypadku losowo generowanych ciągów odwołań do stron, algorytmy FIFO i LRU osiągają bardzo zbliżone wyniki, FIFO wypada minimalnie lepiej, co może być wynikiem losowości danych testowych. <br><br>
W przypadku danych o wyraźnych wzorcach lokalności, czyli gdy pewne strony są używane częściej i w krótkich odstępach czasu, FIFO znacząco przewyższa LRU pod względem liczby błędów stron. Wynika to z faktu, że FIFO działa wyłącznie na zasadzie kolejności wczytania stron do pamięci i nie bierze pod uwagę ich ponownego użycia. W konsekwencji może usuwać często używane strony, co prowadzi do większej liczby błędów strony. <br><br>
Algorytm LRU osiąga lepsze wyniki w środowiskach charakteryzujących się lokalnością czasową, ponieważ jego strategia polega na usuwaniu stron najdłużej niewykorzystywanych, co pozwala utrzymać w pamięci strony o największym prawdopodobieństwie ponownego użycia. To czyni go bardziej efektywnym, zwłaszcza w warunkach, które odzwierciedlają realistyczne scenariusze pracy systemu operacyjnego.
## Źródła
- Dr inż. Marek Wilkus, [Systemy operacyjne Wykład 04](https://home.agh.edu.pl/~mwilkus/os/2024_W04_ITc.pdf)
- Dr inż. Marek Wilkus, [Systemy operacyjne Wykład 03N](https://home.agh.edu.pl/~mwilkus/os/2024_W03N_ITc.pdf)
- prof. dr hab. inż. Jerzy Brzeziński, dr inż. Dariusz Wawrzyniak, [Planowanie przydziału procesora](https://www.cs.put.poznan.pl/dwawrzyniak/SysOp2017/szereg1_1s.pdf)
- dr inż. Witold Paluszyński, [Szeregowanie: podstawowe pojęcia i algorytmy szeregowania, szeregowanie zadań obliczeniowych i interakcyjnych, strategie złożone](https://kcir.pwr.edu.pl/~witold/opsys/os_sched_s.pdf)