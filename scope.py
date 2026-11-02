# scope of varieble
x=4   # ---> global func it is accessible throught out the program
def r():
    global x
    x=3  # local varieble it is only accessible in this fun r() out of func it is not accessible
    return x
print(f"before calling the func x value is {x}")
r()
print(f"now after calling func the value of x is {x}")