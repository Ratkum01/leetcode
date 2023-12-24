class Solution(object):
    def romanToInt(self, s):
        rim={
            "I":1,
            "V":5,
            "X":10,
            "L":50,
            "C":100,
            "D":500,
            "M":1000,
        }
        res=0
        for i in range(len(s)):
            if i+1 < len(s) and rim[s[i]] < rim[s[i+1]]:
                res -= rim[s[i]]
            else:
                res+= rim[s[i]]
        return res