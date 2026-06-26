th1, lang1, dbg1 = input().split()
th2, lang2, dbg2 = input().split()

settings = {
    'theme': th1,
    'lang': lang1,
    'debug': True if dbg1 == '1' else False,
    'override': {
        'theme': th2,
        'lang': lang2,
        'debug': None if dbg2 == '-' else (True if dbg2 == '1' else False)
    }
}

final_theme = settings['override']['theme'] if settings['override']['theme'] != '-' else settings['theme']
final_lang = settings['override']['lang'] if settings['override']['lang'] != '-' else settings['lang']
final_debug = settings['override']['debug'] if settings['override']['debug'] is not None else settings['debug'] 

print(final_theme, final_lang, 1 if final_debug else 0)