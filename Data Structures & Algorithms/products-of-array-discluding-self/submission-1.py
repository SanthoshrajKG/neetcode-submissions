class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        curr_pre = 1
        curr_suf = 1 

        prefix = []
        suffix = [] 
        result = []  
        for i in nums:
            prefix.append(curr_pre)
            curr_pre *= i
        
        for i in nums[::-1]:
            suffix.append(curr_suf)
            curr_suf *= i

        leng = len(prefix)
        for i in range(leng):
            result.append(prefix[i] * suffix[leng-1-i])

        return result

            
            
        