class Solution:
    def maxArea(self, height: List[int]) -> int:
        max = 0
        i = 0
        j = len(height) - 1
        while i != j:
            if height[i] > height[j]:
                area = height[j] * (j-i)
                j -= 1
            elif height[i] <= height[j]:
                area = height[i] * (j-i)
                i += 1                
            if max < area:
                max = area
        
        return max

                            