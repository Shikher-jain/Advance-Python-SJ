import logging
def logFunctcionCall(func):
    def decorted(*args, **kwargs):
        print(logging.info(f"Calling {func.__name__} with args={args}, kwarg={kwargs}"))
        result=func(*args, **kwargs)
        logging.info(f"{func,__name__} returned {result}")
        return result
    return decorted
@logFunctcionCall
def my_function(a,b):
    return (a+b)
# print(my_function(45,87))
my_function(5,5)
print(logFunctcionCall)