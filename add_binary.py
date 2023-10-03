'''
Example 1:

Input: a = "11", b = "1"
Output: "100"
Example 2:

Input: 
Output: "10101"

'''

a = "11"
b = "1"

# a = "1010"
# b = "1011"



def bin_to_dec(s : str)-> int :
    return sum([int(s[(len(s)-1)-i])*pow(2,i) for i in range(len(s)-1,-1,-1)])
def dec_to_bin(x : int)->str:
    if x==0:
        return "0"
    s=""
    while x!=0:
        s=str(x%2)+s
        x=x//2
    return s

def addBinary(a: str, b: str) -> str:
    '''
    1. Naive 
    '''
    # return dec_to_bin(bin_to_dec(a)+bin_to_dec(b))
    '''
    
    2. using Primitives
    
    '''
    return bin(int(a,2)+int(b,2))[2:]



if __name__ == "__main__":
    print(addBinary(a,b))  