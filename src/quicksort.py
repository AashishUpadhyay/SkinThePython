class QuickSort:
    def __init__(self) -> None:
        pass

    def sort(self, nums):
        self.sort_internal(nums, 0, len(nums)-1)
        return nums

    def sort_internal(self, nums, si, ei):
        if si > ei:
            return

        pivot = nums[ei]
        i = si
        j = si

        while j < ei:
            if nums[j] < pivot:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
            j += 1

        if nums[i] > nums[j]:
            nums[i], nums[j] = nums[j], nums[i]

        self.sort_internal(nums, si, i-1)
        self.sort_internal(nums, i+1, ei)
