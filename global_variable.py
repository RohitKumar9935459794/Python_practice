# declaring the global variable
f=101
print(f)

#globle vs local variable
def someFunction():
    #global f
    f='i am learing python'
    print(f)

someFunction()
print(f)