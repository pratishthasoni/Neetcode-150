class Solution:
    def threeSum(self, nums1: List[int]) -> List[List[int]]:
        
        nums = sorted(nums1)
        l = []
        #print(nums)
        for i in range(len(nums)):

            if i > 0 and  nums[i] == nums[i-1]:
                continue
            j = i+1
            k = len(nums)-1
            tot = 0

            while(j<k):
                tot = nums[i]+nums[j]+nums[k]  
                if tot > 0:
                    k-=1
                elif tot < 0:
                    j+=1
                else:
                    l.append([nums[i],nums[j],nums[k]])
                    j+=1
                    while nums[j]==nums[j-1] and j<k:
                        j=j+1

    
        return(l)
                

