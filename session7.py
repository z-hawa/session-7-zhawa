from typing import Callable


def check_function_docstring():
    '''Closure that has a function which checks if the function provided has a docstring with more than 50 characters'''
    def fn_docstring(fn)->bool:
        """Takes in a function and returns a boolean depending on the docstring 
        fn:function"""
        if not isinstance(fn,Callable):
            raise TypeError("A function has not been provided!")
        if len(fn.__doc__) > 50:
            return True
        else:
            return False

    return fn_docstring



def next_fibonacci_number(*args,**kwargs):
    '''Closure which has a function that iterates over to the next fibonacci number'''
    if args or kwargs:
        raise ValueError("There are no values needed to be sent!")
    fibo_number_1 = 1
    fibo_number_2 = 1
    count = 0

    def next_fibo_number():
        '''Returns the next fibonacci number'''
        nonlocal fibo_number_1, fibo_number_2, count
        count+=1
        if count<=2:
            return fibo_number_2
        fibo_number_1,fibo_number_2=fibo_number_2,fibo_number_2+fibo_number_1
        return fibo_number_2

    return next_fibo_number



global function_dictionary
function_dictionary = {}


def function_call_counter():
    '''Closure which has a function that counts the number of times a function is called'''
    def counter(fn,*args,**kwargs):
        '''Function which has one dictionary that count the number of times a function is called
        fn: function
        *args: arguments to be passed
        **kwargs: keyword-arguments to be passed
        Raises TypeError if fn is not a function
        returns the provided function's output'''
        if not isinstance(fn,Callable):
            raise TypeError("A function has not been provided!")
        function_dictionary[fn.__name__]=function_dictionary.get(fn.__name__,0)+1
        return fn(*args,**kwargs)
    return counter


def updated_function(funcdict:dict):
    '''Closure which has a function that counts the number of times a function is called'''
    if not isinstance(funcdict,dict):
        raise TypeError("The provided variable is not a dictionary!")
    def count_functions(fn,*args,**kwargs):
        '''Function which has two dictionaries that count the number of times a function is called
        fn: function
        *args: arguments to be passed
        **kwargs: keyword-arguments to be passed
        Raises TypeError if fn is not a function
        returns the provided function's output'''
        if not isinstance(fn,Callable):
            raise TypeError("Please provide a function!")
        nonlocal funcdict
        funcdict[fn.__name__]=funcdict.get(fn.__name__,0)+1
        return fn(*args,**kwargs)
    return count_functions