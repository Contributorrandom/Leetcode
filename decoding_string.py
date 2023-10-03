'''

Input: s = "226"
Output: 3
Explanation: "226" could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6).
Example 3:

Input: s = "06"
Output: 0
Explanation: "06" cannot be mapped to "F" because of the leading zero ("6" is different from "06").

'''
# s = "226"
# s = "06"
s="12"
s="111111111111111111111111111111111111111111111"
CONST=[str(x) for x in range(1,27,1)]
DP={
    
}

def numDecodings(s: str) -> int:
    if len(s) ==0:
        return 1
    elif len(s) ==1:
        if s in CONST: return 1
    else:
        if s in DP:
            return DP[s]
        DP[s]=int(s[:2] in CONST)*numDecodings(s[2:])+int(s[:1] in CONST)*numDecodings(s[1:])
        return DP[s]
    

if __name__=='__main__':
    print(numDecodings(s))