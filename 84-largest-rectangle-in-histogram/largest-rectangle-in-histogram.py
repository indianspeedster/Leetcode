class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0
        st = []
        left = []
        for i,h in enumerate(heights):
            ind = i
            while st and st[-1][1] > h:
                index, height = st.pop()
                maxArea = max(maxArea, height*(i - index))
                ind = index
            st.append((ind, h))
        for i,h in st:
            maxArea = max(maxArea, h * (len(heights)-i))
        return maxArea
            
            

        