
'''

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.

'''
strs = ["flower","flow","flight"]
# strs = ["dog","racecar","car"]


def longestCommonPrefix(strs: list[str]) -> str:
    '''
    
    1. Brute force approach -Naive
    
    '''
    
    # i=0
    # common=""
    # while i<len(strs[0]):
    #     char=strs[0][i]
    #     for s in strs[1:]:
    #         try:
    #             if char!=s[i]:
    #                 return common
    #         except IndexError:
    #             return common
    #     common+=char
    #     i+=1
    # return common
    
    '''
    2.  Using sorting 
    
    '''
    i=0
    strs=sorted(strs)
    common=""
    while i<len(strs[0]):
        if i<len(strs[-1]) and strs[0][i]==strs[-1][i]:
            common+=strs[0][i]
            i+=1
        else:
            return common
    return common
    
    
if __name__ == '__main__':
    # print(longestCommonPrefix(strs))
    # pass
    print("aa"<"ab")