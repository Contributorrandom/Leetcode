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
haystack = "sadbutsad"
needle = "sad"

# haystack = "leetcode"
# needle = "leeto"

def strStr(haystack: str, needle: str) -> int:
    
    '''
    1. Naive approach
    '''
    
    i=0
    while i<len(haystack)-len(needle)+1:
        if haystack[i:i+len(needle)]==needle:
            return i
        i+=1
    return -1

    
        

if __name__ == '__main__':
    print(strStr(haystack,needle))
    