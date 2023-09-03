class Solution:
    def min_taps(self, n, ranges):
        return self.calculate_min_taps(ranges, 0, n)

    def calculate_min_taps(self, ranges, begin_at, end_at):
        
        max_covering, backward_limit, frontward_limit = self.find_max_covering(ranges, begin_at, end_at)

        if max_covering == 0:
            return -1

        number_of_taps = [1]

        if backward_limit > begin_at:
            number_of_taps.append(self.calculate_min_taps(ranges, begin_at, backward_limit))
        if frontward_limit < end_at:
            number_of_taps.append(self.calculate_min_taps(ranges, frontward_limit, end_at))

        if -1 in number_of_taps:
            return -1

        return sum(number_of_taps)

    def find_max_covering(self, ranges, begin_at, end_at):
        max_covering = 0
        backward_covering_limit = 0
        frontward_covering_limit = 0

        for i in range(begin_at, end_at + 1):
            if ranges[i] == 0:
                continue

            range_indexes = i - ranges[i], i + ranges[i]
            covering = min(range_indexes[1], end_at) - max(range_indexes[0], begin_at) + 1

            if covering < max_covering:
                continue

            max_covering = covering
            backward_covering_limit = max(range_indexes[0], begin_at)
            frontward_covering_limit = min(range_indexes[1], end_at)

        return max_covering, backward_covering_limit, frontward_covering_limit
