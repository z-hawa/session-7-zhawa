## Session 7 assignment
## Function that checks if a function's docstring meets certain criterias
check_function_docstring is a closure that returns a function that takes in a Callable type and checks if the Callable has a docstring with more than 50 characters .

## Fibonacci iteration function closure
next_fibonacci_number is a closure that returns a function which iterates to the next fibonacci number . The value iterates when the function is called .

## Function Call Counter
This is a closure that returns a function which counts how many times a function was called . This is done through a dictionary using the function's name as the key and increments the value every time the function is called .
The dictionary is a global dictionary and hence there's no need to initialise a local dictionary to the closure .

## Updated Function Call Counter
This is a closure that returns a function which does the same job as the previous function call counter except that the dictionary is not stored globally and the user provides a dictionary instead . Raises a TypeError if the user provided dictionary isn't a dict instance.