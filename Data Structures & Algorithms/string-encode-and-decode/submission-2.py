class Solution:

    def encode(self, strs: List[str]) -> str:
        chars = []
        for strg in strs:
            chars.append(str(len(strg)))
            chars.append('#')
            chars.append(strg)
        return "".join(chars)

    def decode(self, s: str) -> List[str]:
        result = []
        len_lst = []
        str_length = -300
        for i,char in enumerate(s):
            if(i<str_length):
                continue
            if(char != '#'):
                len_lst.append(str(char))
            else:
                if(len(len_lst) <= 0):
                    return ""
                str_length = i+1+int("".join(len_lst))
                result.append(s[i+1:str_length])
                len_lst.clear()
        return result

