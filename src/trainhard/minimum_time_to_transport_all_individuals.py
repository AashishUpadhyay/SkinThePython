# You are given n individuals at a base camp who need to cross a river to reach a destination using a single boat. The boat can carry at most k people at a time. The trip is affected by environmental conditions that vary cyclically over m stages.

# Each stage j has a speed multiplier mul[j]:

# If mul[j] > 1, the trip slows down.
# If mul[j] < 1, the trip speeds up.
# Each individual i has a rowing strength represented by time[i], the time (in minutes) it takes them to cross alone in neutral conditions.

# Rules:

# A group g departing at stage j takes time equal to the maximum time[i] among its members, multiplied by mul[j] minutes to reach the destination.
# After the group crosses the river in time d, the stage advances by floor(d) % m steps.
# If individuals are left behind, one person must return with the boat. Let r be the index of the returning person, the return takes time[r] × mul[current_stage], defined as return_time, and the stage advances by floor(return_time) % m.
# Return the minimum total time required to transport all individuals. If it is not possible to transport all individuals to the destination, return -1.

# Example 1:

# Input: n = 1, k = 1, m = 2, time = [5], mul = [1.0,1.3]

# Output: 5.00000

# Explanation:

# Individual 0 departs from stage 0, so crossing time = 5 × 1.00 = 5.00 minutes.
# All team members are now at the destination. Thus, the total time taken is 5.00 minutes.
# Example 2:

# Input: n = 3, k = 2, m = 3, time = [2,5,8], mul = [1.0,1.5,0.75]

# Output: 14.50000

# Explanation:

# The optimal strategy is:

# Send individuals 0 and 2 from the base camp to the destination from stage 0. The crossing time is max(2, 8) × mul[0] = 8 × 1.00 = 8.00 minutes. The stage advances by floor(8.00) % 3 = 2, so the next stage is (0 + 2) % 3 = 2.
# Individual 0 returns alone from the destination to the base camp from stage 2. The return time is 2 × mul[2] = 2 × 0.75 = 1.50 minutes. The stage advances by floor(1.50) % 3 = 1, so the next stage is (2 + 1) % 3 = 0.
# Send individuals 0 and 1 from the base camp to the destination from stage 0. The crossing time is max(2, 5) × mul[0] = 5 × 1.00 = 5.00 minutes. The stage advances by floor(5.00) % 3 = 2, so the final stage is (0 + 2) % 3 = 2.
# All team members are now at the destination. The total time taken is 8.00 + 1.50 + 5.00 = 14.50 minutes.
# Example 3:

# Input: n = 2, k = 1, m = 2, time = [10,10], mul = [2.0,2.0]

# Output: -1.00000

# Explanation:

# Since the boat can only carry one person at a time, it is impossible to transport both individuals as one must always return. Thus, the answer is -1.00.


from typing import List, Dict, Set
from collections import defaultdict
from functools import cache
from itertools import combinations


class Solution:
    def minTime(self, n: int, k: int, m: int, time: List[int], mul: List[float]) -> float:
        if k == 1 and n > 1:  # If boat can only carry 1 person, impossible for n > 1
            return -1

        @cache
        def dp(people_at_dest: int, stage: int, boat_at_dest: bool) -> float:
            if people_at_dest == (1 << n) - 1:  # All people at destination
                return 0

            if boat_at_dest:  # Boat is at destination, someone needs to return
                min_time = float('inf')
                people_at_dest_indices = [
                    i for i in range(n) if (people_at_dest & (1 << i))]

                # Try each person at destination to return with boat
                for person in people_at_dest_indices:
                    return_time = time[person] * mul[stage]
                    next_stage = (stage + int(return_time)) % m
                    remaining_time = dp(people_at_dest, next_stage, False)

                    if remaining_time != float('inf'):
                        min_time = min(min_time, return_time + remaining_time)

                return min_time
            else:  # Boat is at source, send group to destination
                min_time = float('inf')
                people_at_source = [(1 << i) for i in range(
                    n) if not (people_at_dest & (1 << i))]

                # Try all possible combinations of people to send (up to k people)
                for group_size in range(1, min(k + 1, len(people_at_source) + 1)):
                    for group in combinations(people_at_source, group_size):
                        group_mask = sum(group)  # Combine masks
                        group_indices = [i for i in range(
                            n) if (group_mask & (1 << i))]

                        # Calculate crossing time for this group
                        crossing_time = max(time[i]
                                            for i in group_indices) * mul[stage]
                        next_stage = (stage + int(crossing_time)) % m
                        new_dest = people_at_dest | group_mask

                        remaining_time = dp(new_dest, next_stage, True)
                        if remaining_time != float('inf'):
                            min_time = min(
                                min_time, crossing_time + remaining_time)

                return min_time

        # Start with everyone at source (people_at_dest = 0), stage 0, and boat at source
        result = dp(0, 0, False)
        return result if result != float('inf') else -1.0
