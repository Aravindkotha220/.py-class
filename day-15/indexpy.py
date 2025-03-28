#  recurtion as factorial
# printing N natural numbers in  given number

def fact(input_num):
    if input_num==0:
     return
    print(input_num)
    fact(input_num-1)
    fact(6)
    
    # factorial
    
def fact (input_num):
    if input_num in [1,0]:
        return 1
        res = fact ( input_num-1)
        return input_num *res
        final_res = fact(5)
        print(final_res)
        
# reversing a given string

def rev(str):
    if len(str)<=1:
        return str
        return str[-1]+rev (str[0:-1])
        print(rev('given a string'))
        
        
# exponents using recursion (a**b)

def exponent (a,b):
    if b==0:
        return 1
        return a * exponent(a,b-1)
        print (exponent(a,b))
        
#  if have negative exponents using recursion (a**b)
        
a=10
b=-2

def exponent(a,b):
  if b<0:
        print(1/exponent(a,-1*b))
    # else:
    #     print(exponent(a,b))

        
        
# check if a string is palindrome
def palindrome(str):
     if len (str)<=1:
         return True
         return  str[0] == str[-1] and palindrome (str[0:-1])
         
         print(palindrome('malayalam'))
         print(palindrome('madam'))
         