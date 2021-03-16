#iterative

def factorial1(num):
    fac = num

    if num == 1 or num == 0:
        return 1
    else:
        for i in range(1,num):
            fac *= i
            i-=1
        return fac

#recursive

def factorial(num):
    if num == 1 or num == 0:
        return 1
    else:
        return num*factorial(num-1)
    

print(factorial1(5))
#returns 120
print(factorial(20))
# returns 2432902008176640000
