class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        hair, tortoise = nums[0], nums[0]
        while True:
            hair = nums[hair]
            tortoise = nums[nums[tortoise]]
            if hair == tortoise:
                break
        hair = nums[0]
        while hair != tortoise:
            hair = nums[hair]
            tortoise = nums[tortoise]
        return hair
        