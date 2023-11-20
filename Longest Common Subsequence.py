class Solution: 

    def longestConsecutive(self):

        nums_set = set(nums)
        
        longest =0 
        for n in nums:
            if n-1 not in nums_set:
                length = 0
                while(n+length) in nums_set:
                    length = length+1
                longest = max(length,longest)


        
        return(longest)
    
    

if __name__ == "__main__":

    nums = [100,4,200,1,3,2]

    obj1 = Solution()
    x = obj1.longestConsecutive()
    print(x)


