import unittest
from python_solutions.leetcodedaily.uniquepaths.solution import Solution


class SolutionTest(unittest.TestCase):
    def __init__(self, methodName: str = ...) -> None:
        super().__init__(methodName)
        self._solution = Solution()

    def test_if_there_is_a_single_path_for_one_dimensional_grids(self):
        result = self._solution.unique_paths(1, 1)
        self.assertEqual(0, result)

    def test_if_there_is_three_paths(self):
        result = self._solution.unique_paths(3, 2)
        self.assertEqual(3, result)

    def test_if_there_is_28_paths(self):
        result = self._solution.unique_paths(3, 7)
        self.assertEqual(28, result)


if __name__ == '__main__':
    unittest.main()
