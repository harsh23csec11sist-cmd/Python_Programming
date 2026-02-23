from typing import List

class Solution:
    """
    Given an array of intervals where intervals[i] = [start_i, end_i], merge all overlapping intervals.
    """
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []
        # Sort by start time
        intervals.sort(key=lambda x: x[0])
        merged = [intervals[0]]
        for current in intervals[1:]:
            last = merged[-1]
            if current[0] <= last[1]:  # Overlap
                last[1] = max(last[1], current[1])
            else:
                merged.append(current)
        return merged

# Test
if __name__ == "__main__":
    sol = Solution()
    print(sol.merge([[1,3],[2,6],[8,10],[15,18]]))  # 
    print(sol.merge([[1,4],[4,5]]))                  # 
    