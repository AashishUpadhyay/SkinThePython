# Skin The Python

A repository containing solutions for complex computer science problems using Python.

## Problem Solutions

| Problem Name | Link |
|-------------|------|
| **Graph Algorithms** |
| A* Search (8x8 puzzle) | [astarsearch.py](src/astarsearch.py) |
| Bellman Ford | [bellmanford.py](src/bellmanford.py) |
| Floyd Warshall | [floyd_warshall.py](src/floyd_warshall.py) |
| Kruskal's Algorithm (Disjoint Set) | [kruskalsalgorithm.py](src/kruskalsalgorithm.py) |
| Traveling Salesman Problem | [tsp.py](src/tsp.py) |
| **Dynamic Programming** |
| Knapsack | [knapsack.py](src/knapsack.py) |
| Longest Common Subsequence | [longest_common_subsequence.py](src/longest_common_subsequence.py) |
| Longest Palindrome Subsequence | [longest_palindrome_subsequence.py](src/longest_palindrome_subsequence.py) |
| **String Algorithms** |
| Rabin Karp Search | [rabinkarp.py](src/rabinkarp.py) |
| Hierholzer's Algorithm (Debrujin Sequence) | [hierholzersalgorithm.py](src/hierholzersalgorithm.py) |
| Alien Dictionary | [aliendictionary.py](src/aliendictionary.py) |
| **Data Structures** |
| Fixed Size Queue | [fixedsizequeue.py](src/fixedsizequeue.py) |
| Arbitrary Queue Using Fixed Arrays | [arbitraryqueueusingfixedlengtharray.py](src/arbitraryqueueusingfixedlengtharray.py) |
| LRU Cache | [lrucache.py](src/lrucache.py) |
| Fenwick Tree Application | [count_smaller_than_self.py](src/count_smaller_than_self.py) |
| Time Key Dictionary | [timekeydictionary.py](src/timekeydictionary.py) |
| Quack | [quack.py](src/quack.py) |
| **Probability & Sampling** |
| Markov Chain | [markovchain.py](src/markovchain.py) |
| Reservoir Sampling | [reservoirsampling.py](src/reservoirsampling.py) |
| Fisher Yates | [fisheryates.py](src/fisheryates.py) |
| **Games & Puzzles** |
| Ghost Game | [ghost.py](src/ghost.py) |
| Count4 Game | [count4.py](src/count4.py) |
| Cryptarithmetic Game | [cryptarithmetic.py](src/cryptarithmetic.py) |
| American Crossword Puzzle | [americancrosswordpuzzle.py](src/americancrosswordpuzzle.py) |
| **Miscellaneous** |
| Cheapest Itinerary | [cheapestitinerary.py](src/cheapestitinerary.py) |
| Prime Generator | [primegenerator.py](src/primegenerator.py) |
| Set Cover | [setcover.py](src/setcover.py) |

## Development

1. Install `uv` ([Installation Guide](https://docs.astral.sh/uv/getting-started/installation/))

2. Create a virtual environment:
```bash
uv venv
```

3. Install dependencies:
```bash
uv sync
```

4. Run tests:
```bash
pytest tests/*.py
```
