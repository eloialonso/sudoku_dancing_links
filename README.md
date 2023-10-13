# Sudoku solver - Algorithm X with Dancing Links (DLX)

Sudoku solver based on Knuth's Algorithm X implemented with [Dancing Links](https://arxiv.org/pdf/cs/0011047.pdf) (DLX).

<div align='center'>
     <img alt="Sudoku solver" src="sudoku_solver.gif">
</div>

## Installation and usage

```sh
git clone https://github.com/eloialonso/sudoku_dancing_links.git
cd sudoku_dancing_links
```

Then

```sh
python3 main.py <filename>
```

Example grids are provided in `grids/`:

- `python3 main.py grids/grid_1.txt` (1 solution)
- `python3 main.py grids/grid_2.txt` (2560 solutions)
- `python3 main.py grids/grid_3.txt` (no solution)

For instance, `python3 main.py grids/grid_1.txt` prints

```
*** Solution #1 ***

-------------------------
| 4 5 3 | 1 8 9 | 6 2 7 |
| 6 1 7 | 2 5 3 | 9 4 8 |
| 9 8 2 | 4 7 6 | 3 1 5 |
-------------------------
| 5 3 1 | 8 4 7 | 2 9 6 |
| 7 2 9 | 6 3 1 | 5 8 4 |
| 8 6 4 | 9 2 5 | 1 7 3 |
-------------------------
| 2 7 5 | 3 9 8 | 4 6 1 |
| 3 9 6 | 7 1 4 | 8 5 2 |
| 1 4 8 | 5 6 2 | 7 3 9 |
-------------------------

Found 1 solution.
```

## Other problems

Note that the DLX implementation can be used to solve any [Exact Cover](https://en.wikipedia.org/wiki/Exact_cover) problem, not only Sudoku. For instance:

```python
from src import dlx

a = [[1,0,0,1,0,0,1],
     [1,0,0,1,0,0,0],
     [0,0,0,1,1,0,1],
     [0,0,1,0,1,1,0],
     [0,1,1,0,0,1,1],
     [0,1,0,0,0,0,1]]

for solution in dlx(a):
    print(solution)

# prints (1, 3, 5)
```

## Content

- `src/dancing_links.py` and `src/sparse_matrix.py`: Python implementation of Knuth's Algorithm X with Dancing Links (DLX).
- `src/solve_sudoku.py`: sudoku solver based on DLX.
