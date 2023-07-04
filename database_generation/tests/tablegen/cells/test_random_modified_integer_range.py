from random import Random
from typing import Callable, List, Tuple

from databasegen.tablegen.cells.random_modified_integer_range import \
    RandomModifiedIntegerRangeCell


class TestRandomModifiedIntegerRangeCell:
    def test_can_supply_all_arguments_when_instantiating(self):
        """
        We expect to be able to supply the range, a random number generator and
        a modifying function
        """
        LOWER_BOUND: int = 0
        UPPER_BOUND: int = 10
        random: Random = Random()
        modifier: Callable[[int], int] = lambda x: x
        assert RandomModifiedIntegerRangeCell(
            LOWER_BOUND, UPPER_BOUND, random, modifier
        )

    def test_generate_returns_integers_within_range_with_no_modification(self):
        TEST_REPEATS: int = 10
        cell_ranges: List[Tuple[int, int]] = [(0, 10), (4, 4), (-10, 10)]

        lower_bound: int
        upper_bound: int
        random: Random = Random()
        modifier: Callable[[int], int] = lambda x: x
        for lower_bound, upper_bound in cell_ranges:
            cell: RandomModifiedIntegerRangeCell = RandomModifiedIntegerRangeCell(
                lower_bound, upper_bound, random, modifier
            )
            for _ in range(TEST_REPEATS):
                value = int(cell.generate())
                assert value >= lower_bound
                assert value <= upper_bound

    def test_generate_produces_different_integers_with_no_modifier(self):
        # This test has a 1 in 2^1000 chance of failing assuming a uniform
        # distribution
        ATTEMPTS: int = 1000
        LOWER_BOUND: int = 0
        UPPER_BOUND: int = 1
        random: Random = Random()
        modifier: Callable[[int], int] = lambda x: x
        cell: RandomModifiedIntegerRangeCell = RandomModifiedIntegerRangeCell(
            LOWER_BOUND, UPPER_BOUND, random, modifier
        )

        last: str = ""
        curr: str = cell.generate()
        i: int = 0
        while i < ATTEMPTS and (last == "" or last == curr):
            last = curr
            curr = cell.generate()
            i += 1

        assert i < ATTEMPTS

    def test_generate_produces_result_in_modified_range(self):
        TEST_REPEATS: int = 10
        LOWER_BOUND: int = 5
        UPPER_BOUND: int = 8
        random: Random = Random()
        modifier: Callable[[int], int] = lambda x: 2 * x
        cell: RandomModifiedIntegerRangeCell = RandomModifiedIntegerRangeCell(
            LOWER_BOUND, UPPER_BOUND, random, modifier
        )
        for _ in range(TEST_REPEATS):
            value = int(cell.generate())
            assert value >= 2 * LOWER_BOUND
            assert value <= 2 * UPPER_BOUND
