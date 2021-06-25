import inspect
import os
import re
from typing import Counter, Type

import pytest

import session7
import test_session7

README_CONTENT_CHECK_FOR = [
    'iteration',
    'fibonacci',
    'docstring',
    '50',
    'dictionary',
    'global',
    'count',
    'TypeError',
]


def test_readme_exists():
    assert os.path.isfile(
        "README.md"), "README.md file missing!"


def test_readme_contents():
    readme = open("README.md","r", encoding="utf8")
    readme_words = readme.read().split()
    readme.close()
    assert len(readme_words) >= 150, "Make your README.md file interesting! Add atleast 500 words"


def test_readme_proper_description():
    READMELOOKSGOOD = True
    f = open("README.md", "r", encoding="utf8")
    content = f.read()
    f.close()
    for c in README_CONTENT_CHECK_FOR:
        if c not in content:
            print(c)
            READMELOOKSGOOD = False
            pass
    assert READMELOOKSGOOD == True, "You have not described all the functions/class well in your README.md file"


def test_readme_file_for_formatting():
    f = open("README.md", "r", encoding="utf8")
    content = f.read()
    f.close()
    assert content.count("#") >= 10


def test_indentations():
    ''' Returns pass if used four spaces for each level of syntactically \
    significant indenting.'''
    lines = inspect.getsource(session7)
    spaces = re.findall('\n +.', lines)
    for space in spaces:
        assert len(space) % 4 == 2, "Your script contains misplaced indentations"
        assert len(re.sub(
            r'[^ ]', '', space)) % 4 == 0, "Your code indentation does not follow PEP8 guidelines"


def test_function_name_had_cap_letter():
    functions = inspect.getmembers(session7, inspect.isfunction)
    for function in functions:
        assert len(re.findall(
            '([A-Z])', function[0])) == 0, "You have used Capital letter(s) in your function names"


def test_function_count():
    functions = inspect.getmembers(test_session7, inspect.isfunction)
    assert len(functions) > 20, 'Test cases seems to be low. Work harder man...'


def test_function_repeatations():
    functions = inspect.getmembers(test_session7, inspect.isfunction)
    names = []
    for function in functions:
        names.append(function)
    assert len(names) == len(set(names)), 'Test cases seems to be repeating...'


def test_function_doc_string():
    functions = inspect.getmembers(session7, inspect.isfunction)
    for function in functions:
        assert function[1].__doc__


def test_docstring_function_for_more_than_50():
    def check(x): return x
    check.__doc__ = "1"*51
    fn = session7.check_function_docstring()
    assert fn(check) == True, 'Something is wrong here, I can feel it...'


def test_docstring_function_for_less_than_50():
    def check(x): return x
    check.__doc__ = "1"*49
    fn = session7.check_function_docstring()
    assert fn(check) == False, 'Something is wrong here, I can feel it...'

def test_docstring_function_for_equal_to_50():
    def check(x): return x
    check.__doc__ = "1"*50
    fn = session7.check_function_docstring()
    assert fn(check) == False, 'Something is wrong here, I can feel it...'

def test_docstring_function_for_wrong_type():
    with pytest.raises(TypeError):
        test = 1
        fn = session7.check_function_docstring()
        fn(test)


def test_fibonacci_iteration():
    fibo = session7.next_fibonacci_number()
    assert fibo() == 1, "Something is wrong here,I can feel it"
    assert fibo() == 1, "Something is wrong here,I can feel it"
    assert fibo() == 2, "Something is wrong here,I can feel it"
    assert fibo() == 3, "Something is wrong here,I can feel it"
    for i in range(5):
        fibo()
    fibo() == 55


def test_fibonacci_for_unwanted():
    with pytest.raises(ValueError):
        fibo = session7.next_fibonacci_number('hmm let\'s see what happens')


add=lambda *args:sum(args)
mul=lambda x,y:x*y
def div(x,y):
    if y==0:
        raise ValueError("Can't divide by zero")
    return x/y
def test_normal_counter_function_with_add():
    counterfunction=session7.function_call_counter()
    for i in range(10):
        counterfunction(add,1,2,3,4,5,6)
    assert session7.function_dictionary[add.__name__]==10,'Hmm seems like the function can\'t count'

def test_normal_counter_function_with_mul():
    counterfunction=session7.function_call_counter()
    for i in range(5):
        counterfunction(mul,1,6)
    assert session7.function_dictionary[mul.__name__]==5,'Hmm seems like the function can\'t count'

def test_normal_counter_function_with_div():
    counterfunction=session7.function_call_counter()
    for i in range(14):
        counterfunction(div,1,3)
    assert session7.function_dictionary[div.__name__]==14,'Hmm seems like the function can\'t count'

def test_normal_counter_function_with_illegal_data():
    counterfunction=session7.function_call_counter()
    with pytest.raises(ValueError):
        counterfunction(div,1,0)

def test_normal_counter_function_with_non_function():
    counterfunction=session7.function_call_counter()
    with pytest.raises(TypeError):
        counterfunction('what is this idk')

def test_output_of_counter_function():
    counterfunction=session7.function_call_counter()
    assert 2==counterfunction(add,1,1),"Arey bhai function ko call kaun karega?"


def test_updated_counter_function_with_add():
    mydict={}
    counterfunction=session7.updated_function(mydict)
    for i in range(10):
        counterfunction(add,1,2,3,4,5,6)
    assert mydict[add.__name__]==10,'Hmm seems like the function can\'t count'

def test_updated_counter_function_with_mul():
    mydict={}
    counterfunction=session7.updated_function(mydict)
    for i in range(4):
        counterfunction(mul,1,5)
    assert mydict[mul.__name__]==4,'Hmm seems like the function can\'t count'

def test_updated_counter_function_with_div():
    mydict={}
    counterfunction=session7.updated_function(mydict)
    for i in range(14):
        counterfunction(div,6,3)
    assert mydict[div.__name__]==14,'Hmm seems like the function can\'t count'

def test_updated_counter_function_with_illegal_data():
    mydict={}
    counterfunction=session7.updated_function(mydict)
    with pytest.raises(ValueError):
        counterfunction(div,1,0)

def test_updated_counter_function_with_non_function():
    mydict={}
    counterfunction=session7.updated_function(mydict)
    with pytest.raises(TypeError):
        counterfunction('what is this idk')

def test_output_of_counter_function():
    mydict={}
    counterfunction=session7.updated_function(mydict)
    assert 2==counterfunction(add,1,1),"Arey bhai function ko call kaun karega?"
