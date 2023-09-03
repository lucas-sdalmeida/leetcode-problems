class Solution:
    def __init__(self):
        self._memo_ = {}

    def unique_paths(self, m, n):
        if m == n == 1:
            return 0
        if m == 1 or n == 1:
            return 1
        if (m, n) not in self._memo_.keys():
            self._memo_[m, n] = self.unique_paths(m - 1, n) + self.unique_paths(m, n - 1)
        return self._memo_[m, n]
