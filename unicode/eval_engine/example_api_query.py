import requests as r



 __name__ == '__main__':

    rev_string = 'return str[::-1]'
    tests = []  
    test_strings = ['hey', 'whats up?', 'nothing much', 'olive', 'majumder', 'wooster', 'Merry Christmas']

    wrapper_data = {
            'argument': 'str',
            'func_name': 'rev_string'
        }  

    for str in test_strings:
        elem = [str, str[::-1]]
        tests.append(elem)
    
    wrapper = 'def'
    
