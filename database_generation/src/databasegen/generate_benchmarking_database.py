from random import Random
from typing import List

from databasegen.tablegen.cells.cell import Cell
from databasegen.tablegen.cells.counter_cell import CounterCell
from databasegen.tablegen.cells.even_integer_cell import EvenIntegerCell
from databasegen.tablegen.cells.odd_integer_cell import OddIntegerCell
from databasegen.tablegen.cells.random_modular_integer_cell import \
    RandomModularIntegerCell
from databasegen.tablegen.record_generator import RecordGenerator


def main():
    random: Random = Random()
    record_generator: RecordGenerator = construct_record_generator(random)


def construct_record_generator(random: Random) -> RecordGenerator:
    id: Cell = CounterCell()
    one_percent: Cell = RandomModularIntegerCell(100, random)
    twenty_percent: Cell = RandomModularIntegerCell(5, random)
    twenty_five_percent: Cell = RandomModularIntegerCell(4, random)
    fifty_percent: Cell = RandomModularIntegerCell(2, random)
    even_one_percent: Cell = EvenIntegerCell(100, random)
    odd_one_percent: Cell = OddIntegerCell(100, random)

    cells: List[Cell] = [
        id,
        one_percent,
        twenty_percent,
        twenty_five_percent,
        fifty_percent,
        even_one_percent,
    ]

    return RecordGenerator(cells)


if __name__ == "__main__":
    main()
