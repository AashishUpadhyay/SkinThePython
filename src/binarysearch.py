class BinarySearch:
    def __init__(self) -> None:
        pass

    def search(self, nums, target):
        si = 0
        ei = len(nums) - 1

        while si <= ei:
            mid = si + (ei-si)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                si = mid+1
            else:
                ei = mid-1
        return -1
