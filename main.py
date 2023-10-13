import argparse

from src import solve_sudoku


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('filename', help='Path to sudoku text file.')
    args = parser.parse_args()
    solve_sudoku(path=args.filename)


if __name__ == "__main__":
    main()


