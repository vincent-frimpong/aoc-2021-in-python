from unittest import TestCase

from src.Day01 import part1, part2


class TestPart1(TestCase):
    def test_part_1_with_1_item(self):
        sample_input = [200]
        expected = {"increased": 0, "decreased": 0}
        self.assertEqual(part1(sample_input), expected)

    def test_part_1_with_2_items(self):
        sample_input = [199, 200]
        expected = {"increased": 1, "decreased": 0}
        self.assertEqual(part1(sample_input), expected)

    def test_part_1(self):
        sample_input = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]
        expected = {"increased": 7, "decreased": 2}
        self.assertEqual(part1(sample_input), expected)


class TestPart2(TestCase):
    def test_part2_with_3(self):
        sample_input = [199, 200, 208]
        expected = {"increased": 0, "decreased": 0}
        self.assertEqual(part2(sample_input), expected)

    def test_part2_with_4(self):
        sample_input = [199, 200, 208, 210]
        expected = {"increased": 1, "decreased": 0}
        self.assertEqual(part2(sample_input), expected)

    def test_part2(self):
        sample_input = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]
        expected = {"increased": 5, "decreased": 1}
        self.assertEqual(part2(sample_input), expected)
