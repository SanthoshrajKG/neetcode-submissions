import math
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        seen = {}
        result = []
        for num in nums:
            if(num not in seen):
                seen[num] = 0
            seen[num] += 1
        
        sorted_seen = sorted(seen.items(), key=lambda item: item[1], reverse=True)

        for i in range(k):
            result.append(sorted_seen[i][0])
        
        return result


            

        