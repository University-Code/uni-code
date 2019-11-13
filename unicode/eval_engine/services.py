import requests
from unicode import settings

lang = {
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

def eval_engine(source, lang, test_in, test_out):
    url = settings.CODE_EVAL_API_URL
    route = '/submissions/?base64_encoded=false&wait=true'   # wait=true makes the API call synchronous, halving the number of requests needed
    params = {
        'source_code': source,
        'language_id': lang,
        'stdin': test_in,
        'expected_output': test_out
    }
    r = requests.post(url+route, params=params)
    eval_output = r.json()
    return eval_output


def eval_setup(submission):
    submission_info = submission['user_submission']
    test_cases = submission['test_cases']

    source_code = submission_info.submission
    language = submission_info.language
    
    '''
    Collects all test case statuses in one object
    '''
    
    test_results = {}
    index = 0

    for case in test_cases:
        eval_object = eval_engine(source_code, lang[language], case.test_input, case.test_output)
        print(eval_object)

        #Checks for error
        if 'Error' in eval_object['status']['description']:
            error = eval_object['status']['description']
            return {'error': error}
        elif eval_object['status']['description'] == "Wrong Answer":
            status = 'fail'
        else:
            status = 'pass'
        
        #Adds test case object to result every iteration
        test_results[index] = {
                    "test_input": case.test_input,
                    "test_output": case.test_output,
                    "status": status
                }
        index += 1
        
    return test_results


