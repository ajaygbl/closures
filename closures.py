def outer_func(msg):
    message = msg

    def inner_func():
        print(message)

    return inner_func

hi_func = outer_func('Hi')
Hello_func = outer_func('Hello')

hi_func()
Hello_func()

#print(my_func)          # output --> <function outer_func.<locals>.inner_func at 0x108539080>
#print(my_func.__name__) # output -->  inner_func
#my_func()        # output --> Hi

# accessing message variable in inner_func which is defined in outer_func
# message variable is called free variable


