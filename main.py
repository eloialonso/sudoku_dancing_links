import argparse
from pathlib import Path

from src import solve_sudoku


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('filename', type=Path, help='Path to sudoku text file.')

    args = parser.parse_args()

    with args.filename.open('r') as f:
        grid = [list(map(int, x.strip().split(' '))) for x in f.readlines()]

    solve_sudoku(grid)


if __name__ == "__main__":
    main()


