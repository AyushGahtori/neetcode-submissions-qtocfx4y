class Solution:

    def encode(self, strs: List[str]) -> str:
        a = ""
        for s in strs:
            a += str(len(s)) + "#" + s
        return a    


    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != "#":
                j+=1
            length = int(s[i:j])
            res.append(s[j+1 : j + length + 1])
            i = j + 1 + length   
        return res    

