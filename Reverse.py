def reverse(s):
    if len(s) == 0:
        return s
    else:
        return reverse(s[1:]) + s[0]
  
s = "Anandhi"
  
print ("The original string  is : ","")
print (s)
  
print ("The reversed string(using recursion) is : ","")
print (reverse(s))
print ("Successfully reversed a string")

####### .........Here Palindrome Program ........ ######

def isPalindrome(s):
    return s == s[::-1]
 
 
# Driver code
s = "malayalam"
ans = isPalindrome(s)
 
if ans:
    print("Yes....It is palindrome")
else:
    print("No .......It is not a palindrome")