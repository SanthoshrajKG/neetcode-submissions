from collections import defaultdict
class Solution:
    def convertStr(self, str):
        lst = [0] * 26
        for s in str:
            pos = ord(s) - ord('a')
            lst[pos] += 1 
        return lst
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = defaultdict(list)
        for str in strs:
            num_lst = tuple(self.convertStr(str))
            seen[num_lst].append(str)
        result = []
        for key in seen:
            result.append(seen[key])
        return result
        


            

        