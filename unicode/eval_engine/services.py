import requests
from . import settings
import sys 
from termcolor import colored, cprint 
import re
from ast import literal_eval



language_id = {
    'C': 4,
    'C++': 10,
    'C#': 16,
    'Clojure': 18,
    'Java': 26,
    'JavaScript': 29,
    'Octave': 32,
    'Python': 34,
    'Ruby': 38
}
def eval_engine(source, language_id, test_in, test_out):
    #Replaces escape string with new line 
    source= source.replace('\\n', '\n') 
    api_test= format_source_code(language_id, source, test_in)
    print(colored(api_test,"red"))
    
    url = settings.CODE_EVAL_REQUEST_ENDPOINT   # wait=true makes the API call synchronous, halving the number of requests needed
    params = {
        'source_code': api_test,
        'language_id': language_id,
        'stdin': test_in,
        'expected_output': test_out
    }
    r = requests.post(url, params=params)
    eval_output = r.json()
    return eval_output
    

def eval_setup(submission):
    submission_info= submission['user_submission']
    test_cases= submission['test_cases']

    source_code= submission_info.submission
    language= submission_info.language
    
    '''
    Collects all test case statuses in one object
    '''
    
    result={}
    index=0
    for case in test_cases:
        status=""
        test_input=case.test_input
        test_output= case.test_output
        eval_object = eval_engine(source_code, language_id[language], test_input, test_output)
        print(eval_object)

        #Checks for error
        if 'Error' in eval_object['status']['description']:
            error= eval_object['status']['description']
            return {'error': error}
        elif eval_object['status']['description']=="Wrong Answer":
            status='fail'
        else:
            status='pass'
        
        #Adds test case object to result every iteration
        result[index]=({"test_input":test_input,"test_output":test_output,"status":status})
        index+=1
    return result

def format_source_code(language_id, code, test_input):
    
     #Alogrithm: 
     #Finds function name
     #Adds print statement to test function
     #Concats function and print statement in one string 
 
    if language_id == 34: #Python
        result = re.search('def (.*):', code)
        temp= result.group(1)
        test_function="print("+re.sub(r'\([^)]*\)', '', temp) + "('"+ test_input+"'))"
        test_function=test_function.replace("\\","")
        api_test= code+ "\n"+ test_function
        return api_test
    else:
        return code
