class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        count1, count2 = Counter(nums1), Counter(nums2)
        ans = []
        for val in count1.keys():
            if val in count2:
                ans.extend([val]*min(count1[val], count2[val]))
        return ans        