class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        charcount = {}

        for ch in s:
            charcount[ch] = charcount.get(ch,0) +1

        for ch in t:
            charcount[ch] = charcount.get(ch,0) -1

        for values in charcount.values():
            if values != 0: 
                return False    

        return True