'''
Example 1:

Input: s = "()"
Output: true
Example 2:

Input: s = "()[]{}"
Output: true
Example 3:

Input: s = "(]"
Output: false



'''

# s = "()"
# s = "()[]{}"
s = "(]"


CONST={
    "(":")",
    "[":"]",
    "{":"}"
        }

def isValid(s: str) -> bool:
    i=0
    stack=[]
    while i<len(s):
        if s[i] in CONST:
            stack.append(s[i])
        else:
            try:
                if s[i]!=CONST[stack.pop()]:
                    return False
            except IndexError:
                return False
        i+=1
    if len(stack)>0:
        return False
    return True
        

if __name__=='__main__':
    # print(isValid(s))
    s=[1,4,2,1]
    print(s.sort())
    print(s)