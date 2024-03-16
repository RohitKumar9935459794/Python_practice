f=101
print(f)

#global vs local variable in functions
def someFunction():
    global f
    print(f)
    f="chainging global variable"

someFunction()
print(f)