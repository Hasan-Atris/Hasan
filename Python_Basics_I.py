# %%
a = 56
b = 11
# 1) Basic Operations
# Addition +
# Subtraction -
# Multiplication *
# Division /
# Integer Division
ans = a//b
print('Integer Division: ', ans)

# Modulo
ans =a%b
print('Modulo: ', ans)

# Exponentiation 
# square one of the variables
''' 
Note that a ^ b  will run but give you the wrong results. 
In python the ^ operator does not exponentiate like a normal person would expect it to, instead it does a bitwise XOR (if you do not know what that means its not very important and you will probably never use it in this course... neither in the rest of your life)
'''
ans = a**b
print('Exponentiation: ', ans)
# %%
# 2) Loops

''' 
a) Using only one for loop, draw the following shape:

size = 5
*
**
***
****
*****


b) Using two for loops, draw the following shape:
(if you'r feeling adventurous try doing it with 1 for loop)

size = 5
*********
 *******
  *****
   ***
    *
   ***
  *****
 *******
*********


c) Using a while loop brute force trying to find the square root of a perfect square and print it. If the number is not a perfect square, print 'square root not found'.
num=int(input())
div=1
while(div**2!=num):
    div=div+1
    if(div>num):
        div=-1
        break
print(div)
    '''

# a)
size = 5
# Fill in the code here
s1="*"
l=[1,2,3,4,5]
for i in l:
    print(s1*i)
print()
# b)
size = 5
# Fill in the code here
m="*"
sp=" "
list1=[9,7,5,3,1,3,5,7,9]
list2=[0,1,2,3,4,3,2,1,0]
for i in range(0,len(list1)):
    s=(sp*list2[i])+(m*list1[i])
    print(s)

print()

# c)
input_Value = 592240896
# Fill in the code here
num=592240896
div=1
while(div**2!=num):
    div=div+1
    if(div>num):
        div=-1
        break
print(div)



# %%

# 3) Functions 
#  Write a function that takes a String and checks if it is a palindrome or 
# not. (a palindrome is a word that is read the same left to right and right to left i.e.: 'civic', 'anna' and '1001001' are palindromes but 'car' is not ) 

# Fill in the code here
def IsPalindrome(s):

    sI=s[::-1]
    if(s==sI):
        return True
    else:
        return False
print(IsPalindrome("CIVIC"))




# %%
