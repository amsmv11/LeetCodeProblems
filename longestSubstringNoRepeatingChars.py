class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
            res = ""
            con = ""
            for e in range(len(s)):
                if s[e] not in con:
                    con += s[e]
                else:
                    if len(con) > len(res):
                        res = con
                    for i in range(len(con)):
                        if con[i] == s[e]:
                            con = con[i+1:]
                            con += s[e]
                            break

            if len(con) > len(res):
                res = con
            return len(res)