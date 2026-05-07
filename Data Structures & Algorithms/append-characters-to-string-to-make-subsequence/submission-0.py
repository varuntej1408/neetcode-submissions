class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        i = 0   # pointer for s
        j = 0   # pointer for t

        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                j += 1      # match found, move t pointer
            i += 1          # always move s pointer

        return len(t) - j  # remaining unmatched characters


        