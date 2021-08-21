class Knapsack:
    def __init__(self) -> None:
        pass

    def can_partition(self, nums):
        total_sum = 0
        for num in nums:
            total_sum += num

        if (total_sum & 1) == 1:
            return False

        self.memo = {}
        for i in range(len(nums)):
            index_set = set()
            if self.dfs(total_sum//2, i, 0, index_set, nums):
                return True

        return False

    def dfs(self, match_condition, index, running_sum, index_set, nums):
        if len(index_set) > len(nums)-1:
            return False

        if running_sum == match_condition:
            return True

        if index not in self.memo:
            self.memo[index] = {}

        if running_sum in self.memo[index]:
            return self.memo[index][running_sum]

        result = False
        for i, num in enumerate(nums):
            if i in index_set:
                continue

            index_set.add(i)
            result = self.dfs(
                match_condition, i, running_sum + num, index_set, nums)
            index_set.remove(i)
            if result:
                break

        self.memo[index][running_sum] = result
        return result
