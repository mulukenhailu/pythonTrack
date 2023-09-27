class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        nums.sort()
        left=0
        right=len(nums)-1
        total=0
        while left<right:
            if nums[left]+nums[right]>upper:
                right=right-1
            else:
                
                total+=(right-left)
                left=left+1
        left=0
        right=len(nums)-1
        while left<right:
            if nums[left]+nums[right]>lower-1:
                right=right-1
            else:
                total-=(right-left)
                left=left+1
        return total
                
            
            
            
                
            
        