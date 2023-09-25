'''
Example 1:

Input: haystack = "sadbutsad", needle = "sad"
Output: 0
Explanation: "sad" occurs at index 0 and 6.
The first occurrence is at index 0, so we return 0.

Example 2:

Input: haystack = "leetcode", needle = "leeto"
Output: -1
Explanation: "leeto" did not occur in "leetcode", so we return -1.


'''
import math


haystack = "sadbutsad"
needle = "sad"

haystack="mississippi"
needle="pi"

# haystack = "leetcode"
# needle = "leeto"

def LPS_non_overlapping(S : str)->int:
    
    '''
    1. Naive: 
    '''
    
    isEven=not(len(S)%2)
    mid=math.ceil(len(S)/2)
    i=0
    while i<mid:
        flag= S[0:mid-i]==S[mid+i:] if isEven else S[0:mid-i-1]==S[mid+i:]
        if flag:
            return len(S[mid+i:])
        i+=1
    return 0


def strStr(haystack: str, needle: str) -> int:
    
    '''
    1. Naive approach
    '''
    
    # i=0
    # while i<len(haystack)-len(needle)+1:
    #     if haystack[i:i+len(needle)]==needle:
    #         return i
    #     i+=1
    # return -1

    '''
    2. KMP- Algorithm- O(m+n)
    
    '''
    
    i,j=0,-1
    lps=computeLPSArray(needle)
    while i<len(haystack) and j<len(needle)-1:
        if haystack[i]==needle[j+1]:
            j+=1
            i+=1
        else:
            if j==-1:
                i+=1 
            else:
                j=lps[j]

    
    if j==len(needle)-1:
        return i-len(needle)
    return -1
    

def computeLPSArray( S: str)->list[int]:
    i,length=1,0
    lps=[0]*len(S)
    while i<len(S):
        if S[i]==S[length]:
            length+=1
            lps[i]=length
            i+=1
        else:
            if length!=0:
                length=lps[length-1]
            else:
                lps[i]=0
                i+=1
    return [x-1 for x in lps] # For 0-indexed arrays 

        

        

if __name__ == '__main__':
    S="issip"
    print(computeLPSArray("ababa"))
    # print(strStr(haystack,needle)) 
    