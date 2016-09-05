"""
Definition of ArrayReader:
class ArrayReader:
    def get(self, index):
        # this would return the number on the given index
        # return -1 if index is less than zero.
"""


class Solution:
    def search_a_big_sorted_array(self, reader, target):
        index = 0
        while reader.get(index) < target:
            index = index * 2 + 1

        start, end = 0, index
        while start + 1 < end:
            mid = start + (end - start)/2
            num = reader.get(mid)
            if num >= target:
                end = mid
            else:
                start = mid

        if reader.get(start) == target:
            return start
        if reader.get(end) == target:
            return end

        return -1