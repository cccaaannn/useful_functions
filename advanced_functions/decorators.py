
# we need decorators to add additional functionally to a function without changing it
# we need a structure like this because there should be a function that returns wrapper function 
# since wrapper function can't return itself outer decorator function does that


# general structure
def outer_function(msg):
    def inner_function(name):
        print(msg, name) # can access msg
    
    return inner_function
    # return inner_function()  this executes when outer_function called
    
hi = outer_function("hi")
# hi("can")


# ways of writing
def decorator_funcion(func): 
    def function(*args, **kwargs): 
        return func()
    return function 

# 1
def hello():
    print("hello")

decorated = decorator_funcion(hello)
# decorated()

# 2
@decorator_funcion
def hello2():
    print("hello")

# hello2()


# class decorator
class decorator_class(object):
    def __init__(self, func):
        self.func = func
    def __call__(self, *args, **kwargs):
        print("add functionality here")
        return self.func(*args, **kwargs)
        




# ---------------------------usefull stuff----------------------------

from functools import wraps
# @wraps(func) if used for preserve original function name while using stacked decorators
# without @wraps stacking decorators can behave abnormally 


# using decarators for timing execution
def calc_exec_time(func):
    import time

    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        func_instance = func(*args, **kwargs)
        exec_time = time.time() - start
        print("\n\nfunction: {0} execution time is: {1} sec\n".format(func.__name__, exec_time))
        return func_instance

    return wrapper

import time



# use decorators for logging
def __set_logger(logger_name):
    import logging

    logger = logging.getLogger(logger_name)  
    
    logger.setLevel(20)
    formatter = logging.Formatter("[%(levelname)s] %(asctime)s %(message)s", datefmt="%Y-%m-%d %H:%M:%S")

    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(formatter)
    logger.addHandler(stream_handler)

    return logger

# passing a parameter to a decorated function is looks like this
def log_func(logger):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            logger.info("Function: {0} Ran with args: {1}, and kwargs: {2}".format(func.__name__, args, kwargs))
            return func(*args, **kwargs)
        return wrapper
    return decorator



logger = __set_logger("my_logger")

@log_func(logger)
@calc_exec_time
def display_info(name, age):
    time.sleep(1)
    print(name, age)

display_info("can", 23)






