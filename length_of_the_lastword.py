'''

Example 1:

Input: s = "Hello World"
Output: 5
Explanation: The last word is "World" with length 5.
Example 2:

Input: s = "   fly me   to   the moon  "
Output: 4
Explanation: The last word is "moon" with length 4.
Example 3:

Input: s = "luffy is still joyboy"
Output: 6
Explanation: The last word is "joyboy" with length 6.


'''

s = "Hello World"
s = "   fly me   to   the moon  "
s = "luffy is still joyboy"

def lengthOfLastWord( s: str) -> int:
    
    '''
    1. Naive
    
    '''
    
    i=len(s)-1
    count=0
    flag=False
    while i>-1:
        if s[i]==" ":
            if flag:
                return count
            i-=1
        else:
            count+=1
            flag=True
            i-=1
    # return count
    
    '''
    2. Using strip()
    '''


    s=s.strip()
    i,count=len(s)-1,0
    while i>-1:
        if s[i]==" ":
            return count
        else:
            count+=1
            i-=1
    # return count
    '''
    3. Using split()
    '''
    
    return len(s.split()[-1])
    
    



if __name__ == "__main__":
    print(lengthOfLastWord(s))