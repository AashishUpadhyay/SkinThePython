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

    def can_partition_dp(self, nums):
        total_sum = 0
        for num in nums:
            total_sum += num

        if (total_sum & 1) == 1:
            return False

        width = total_sum//2
        dp = [[False for _ in range(width+1)] for _ in range(len(nums))]

        for i, num in enumerate(nums):
            for j in range(1, width+1):
                if num == j:
                    dp[i][j] = True
                elif num > j:
                    dp[i][j] = dp[i-1][j]
                else:
                    dp[i][j] = dp[i-1][j-num]
        return dp[len(nums)-1][width]
