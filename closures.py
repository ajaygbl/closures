def outer_func():
    message ='Hi'

    def inner_func():
        print(message)

    return inner_func()

outer_func()

# accessing message variable in inner_func which is defined in outer_func
#message variable is called free variable