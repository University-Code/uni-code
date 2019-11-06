import requests
from eval_engine.settings import url
from editor.models import UserSubmission
from problems.models import Problem
from problems.models import ProblemTestCase

# Judge0 assigns an integer to each supported language
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


# Makes the post request to the API and returns an object containing the API output
def eval_engine(source, lang, test_in, test_out):
    params = {
        'source_code': source,
        'language_id': lang,
        'stdin': test_in,
        'expected_output': test_out
    }
    return requests.post(url, params=params).json()   # Sends the post request to the api


# Function called by view.py in the editor. Submission_id is the primary key of the UserSubmission table
def eval_setup(submission_id):
    sub = UserSubmission.objects.get(id = submission_id)    # Gets an objects of all the attributes of the submission_id in UserSubmission
    source = sub.submission
    language = sub.language
    # user = sub.submitter
    test_cases = ProblemTestCase.objects.filter(problem = sub.problem)

    for case in test_cases:
        eval_object = eval_engine(source, lang[language], case.test_input, case.test_output)

        if 'Error' in eval_object['status']['description']:
            print('Compile Failed')
        else:
            print(eval_object['status']['description'])
