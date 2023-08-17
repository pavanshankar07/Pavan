def checkIfPalindrome(s): 
     return s == s[::-1] 
  
 s = input() 
 #the input is taken in the form of string so it is easy to compare with the reversed string 
 ans = checkIfPalindrome(s) 
  
 if ans: 
     print("Yes") 
 else: 
     print("No")
