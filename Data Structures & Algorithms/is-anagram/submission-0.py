class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_seen = {}
        t_seen = {}
        for char in s:
            if char not in s_seen:
                s_seen[char] = 0
            s_seen[char] += 1
        
        for char in t:
            if char not in t_seen:
                t_seen[char] = 0
            t_seen[char] += 1
        
        s_len = len(s_seen)
        t_len = len(t_seen)

        if s_len != t_len:
            return False
        
        for char in s_seen:
            if(char not in t_seen or s_seen[char] != t_seen[char]):
                return False
        
        return True


            


        