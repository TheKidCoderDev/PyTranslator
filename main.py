from __future__ import print_function, unicode_literals
from PyInquirer import prompt, print_json
from pprint import pprint
import newlang
import translate
import sys

questions = [
    {
        'type': 'list',
        'name': 'action',
        'message': 'What would you like to do?',
        'choices': ['Translate a program', 'Create a language map', 'Exit'],
        'filter': lambda val: val.lower()
    },
]

answers = prompt(questions)

if answers["action"]=="translate a program":
    questions = [
        {
            'type': 'list',
            'name': 'from',
            'message': 'What language would you like to translate from?',
            'choices': ['English', 'Japanese (日本人)', 'French (Français)'],
            'filter': lambda val: val
        },
        {
            'type': 'list',
            'name': 'to',
            'message': 'What language would you like to translate to?',
            'choices': ['English', 'Japanese (日本人)', 'French (Français)'],
            'filter': lambda val: val
        },
        {
            'type': 'input',
            'name': 'filename',
            'message': 'What file should be translated?',
        }
    ]
    answers = prompt(questions)
    langcodes = {
        'English':0,
        'Japanese (日本人)':1,
        'French (Français)':2
    }
    translate.run(answers["filename"], langcodes[answers["from"]], langcodes[answers["to"]])

elif answers["action"]=="create a language map":
    newlang.run()

else:
    sys.exit()
