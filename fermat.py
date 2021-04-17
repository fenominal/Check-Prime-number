import random
 
#power funtion for x ^ p-1
def power(a, n, p):
     
    # Initialize result
    res = 1
     
  
    a = a % p 
     
    while n > 0:
         
       
        if n % 2:
            res = (res * a) % p
            n = n - 1
        else:
            a = (a ** 2) % p
             
            # n must be even now
            n = n // 2
             
    return res % p
     
#Fermet Therom logic
def isPrime(n, k):
     
   
    if n == 1 or n == 4:
        return False
    elif n == 2 or n == 3:
        return True
     
    # Try k times
    else:
        for i in range(k):    
            a = random.randint(2, n - 2)             
            # Fermat's little theorem
            if power(a, n - 1, n) != 1:
                return False
                 
    return True
             
# Driver code
k = int(input('enter number x :- '))
m=  int(input('enter number p :- '))
  
#chek number is prime or not  
if isPrime(m, k):
  print("true")
else:
  print("false")