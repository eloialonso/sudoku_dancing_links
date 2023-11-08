from typing import List, Tuple


Matrix2D = List[List[int]]


class Cell:
    def __init__(self, name, l=None, r=None, u=None, d=None, c=None) -> None:
        self.name, self.l, self.r, self.u, self.d, self.c = name, l, r, u, d, c

    def __repr__(self) -> str:
        return f"Cell({self.name}, l={self.l}, r={self.r}, u={self.u}, d={self.d}, c={self.c})"

    def __str__(self) -> str:
        return self.name


class Column(Cell):
    def __init__(self, name, size=0, *args, **kwargs) -> None:
        super().__init__(name, *args, **kwargs)
        self.size = size


class Root(Column):
    def __init__(self) -> None:
        super().__init__(name="root")


class SparseMatrix:
    def __init__(self, a: Matrix2D) -> None:
        self._a = a
        self._h = Root()
        self._create_linked_lists()

    @property
    def a(self) -> Matrix2D:
        return self._a

    @property
    def h(self) -> Root:
        return self._h

    @property
    def shape(self) -> Tuple[int, int]:
        return len(self._a), len(self._a[0])

    def _create_linked_lists(self) -> None:
        self._create_columns()
        self._connect_rows()

    def _create_columns(self) -> None:
        prev_col = self.h
        for j in range(self.shape[1]):
            # Create column headers
            col = Column(f"C{j}")
            col.l, prev_col.r = prev_col, col
            prev_col = col
            # Create cells and connect ones inside columns
            prev_row = col
            for i in range(self.shape[0]):
                if self.a[i][j] == 0:
                    continue
                row = Cell(name=f"R{i}C{j}", c=col)
                col.size += 1
                row.u, prev_row.d = prev_row, row
                prev_row = row
            col.u, prev_row.d = prev_row, col
        self.h.l, prev_col.r = prev_col, self.h

    def _connect_rows(self) -> None:
        for i in range(self.shape[0]):
            ones = [j for j in range(self.shape[1]) if self.a[i][j] == 1]
            if len(ones) == 0:
                continue
            first_cell = self._get_cell(i, ones[0])
            prev_cell = first_cell
            for j in ones[1:]:
                cell = self._get_cell(i, j)
                cell.l, prev_cell.r = prev_cell, cell
                prev_cell = cell
            first_cell.l, prev_cell.r = prev_cell, first_cell

    def _get_cell(self, i: int, j: int) -> Cell:
        if self.a[i][j] == 0:
            return None
        col = self.h
        while col.name != f"C{j}":
            col = col.r
        cell = col
        while cell.name != f"R{i}C{j}":
            cell = cell.d
        return cell
