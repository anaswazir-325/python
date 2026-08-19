def prime_number(x):
    print(x)
    if x < 2:
        print("The number is not prime number")
        return
    for i in range(2, x):
     if x % i == 0:
        print("The number is not prime number")
        return
     
    print("The number is prime number")
        
prime_number(5)        