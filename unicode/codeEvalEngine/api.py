#!/usr/bin/python
# -*- coding: utf-8 -*-

from parameters import SupportedLanguages
from parameters import RunAPIParameters

from api_handlers import HackerEarthAPI

client_secret = ''

source =
lang = SupportedLanguages.PYTHON
compressed = 1
html = 0
params = RunAPIParameters(
        client_secret=client_secret, source=source,
        lang=lang, compressed=compressed, html=html)

api = HackerEarthAPI(params)

print('Compiling code..')
r = api.compile()
# print(r.__dict__) If something breaks, uncomment this

print('\nRunning code...')
r = api.run()
# print(r.__dict__) If something breaks, uncomment this
output = r.__dict__.get('output')

print('\nRun Output:')
print(output)
# print('Process Complete!')
