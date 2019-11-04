import requests

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
    url = 'http://159.89.93.145:3000/submissions/?base64_encoded=false&wait=true'
    params = {
        'source_code': source,
        'language_id': lang,
        'stdin': test_in,
        'expected_output': test_out
    }
    r = requests.post(url, params=params)
    eval_output = r.json()
    return eval_output


def eval_setup(submission_id):

    language = 'Python'
    code = "print('yo')"
    sub_id = '12'
    submission = {
        'source': {
            'language': lang[language],
            'code': code
            },
        'submission_id': sub_id
        }

    for case in test_case:
        eval_object = eval_engine(submission['source']['code'], submission['source']['language'], [], 'yo')
    if 'Error' in eval_object['status']['description']:
        print('Compile Failed')
    else:
        print(eval_object['status']['description'])
