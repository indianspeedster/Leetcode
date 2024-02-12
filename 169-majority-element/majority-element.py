class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        major, count = -1,0
        for num in nums:
            if num != major:
                if count == 0:
                    major = num
                    count += 1

                else:
                    count -= 1
            else:
                count += 1
        return major


        