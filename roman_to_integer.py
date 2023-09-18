'''
Example 1:

Input: s = "III"
Output: 3
Explanation: III = 3.

'''

s="III"
# s = "LVIII"
# s = "MCMXCIV"


FACE_VAL={
"I":1,
"V":5,
"X":10,
"L":50,
"C":100,
"D":500,
"M":1000
}
MANI_VAL={
    ("I","V"):3,
    ("I","X"):8,
    ("X","L"):30,
    ("X","C"):80,
    ("C","D"):300,
    ("C","M"):800,
}

def romanToInt( s: str) -> int:
    
    '''
    
    1. Naive approach
    
    '''
    
    # num=0
    # prev=None
    # for x in s:
    #     if (prev,x) in MANI_VAL:
    #         num+=MANI_VAL[(prev,x)]
    #         prev=x
    #     elif x in FACE_VAL:
    #         num+=FACE_VAL[x]
    #         prev=x
    #     else:
    #         assert False
    # return num
    
    '''
    2. With try-exception
    
    '''

    num=0
    prev=None
    for x in s:
        try:
            num+=MANI_VAL[(prev,x)]
            prev=x
        except KeyError:
            num+=FACE_VAL[x]
            prev=x
        except Exception as e:
            assert False
    return num




if __name__ == '__main__':
    print(romanToInt(s))