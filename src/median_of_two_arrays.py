class MedianOfTwoArrays:
    def findMedianSortedArrays(self, nums1, nums2) -> float:
        self.total = len(nums1) + len(nums2)
        if len(nums1) > len(nums2):
            return self.findmedian(nums2, nums1, 0, len(nums2))
        return self.findmedian(nums1, nums2, 0, len(nums1))

    def findmedian(self, arrX, arrY, si, ei):
        par_idx = si + (ei - si) // 2

        arrX1 = arrX[0:par_idx]
        arrX2 = arrX[par_idx:]

        left_side_rem_len = (self.total) // 2 - len(arrX1)
        if left_side_rem_len > 0:
            arrY1 = arrY[0:left_side_rem_len]
        else:
            arrY1 = []

        arrY2 = arrY[len(arrY1) :]

        left_side_len = len(arrX1) + len(arrY1)
        right_side_len = len(arrX2) + len(arrY2)

        X1 = arrX1[-1] if arrX1 else -1000000
        X2 = arrX2[0] if arrX2 else 1000000

        Y1 = arrY1[-1] if arrY1 else -1000000
        Y2 = arrY2[0] if arrY2 else 1000000

        if X1 <= Y2 and Y1 <= X2:
            if left_side_len == right_side_len:
                return (max(X1, Y1) + min(X2, Y2)) / 2
            elif left_side_len > right_side_len:
                return max(X1, Y1)
            else:
                return min(X2, Y2)
        elif X1 < Y2:
            return self.findmedian(arrX, arrY, par_idx + 1, ei)
        else:
            return self.findmedian(arrX, arrY, si, par_idx - 1)
