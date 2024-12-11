def factorial(n):
    if n == 0:    		# the base case 
        return 1
    else:		 		# the recursive case
        return n * factorial(n-1)

#print(factorial(10))
#print(factorial(100)) # grows very fast

def reverse_string(s):
    if len(s) <= 1:  
        return s
    else:
        return reverse_string(s[1:]) + s[0]

word = "Testing"
#word = "T"
#print(f"The word {word} reversed is {reverse_string(word)}")

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)
    
#print(gcd(9,6))
print("GCD:", gcd(112127, 26443))

