# def func():
#     local_var=10
#     print(local_var)
#
# func()

global_var=20
def func():
    local_var=10
    print(local_var)

print(global_var)
func()

#Example 2
xy=100 #global

def cool():
    global xy #global is keyword
    xy=200
    print(xy)

# cool()
print(xy)
cool()


