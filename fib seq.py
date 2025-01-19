def fibonacci():
    #num will stores number of terms  
 num = int(input("How many terms: "))
 #here a and b is fibonacci numbers
 a, b = 0, 1

 if num <= 0:
     print("Please enter a positive integer")
 elif num == 1:
     print("Fibonacci sequence up to 1:", a)
 else:
     print("Fibonacci sequence:")
 for _ in range(num):
     print(a,end=" ")
     a,b = b, a+b
fibonacci()
