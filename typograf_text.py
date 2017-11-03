from re import sub


EM_DASH = '\u2014'
EN_DASH = '\u2013'
QUOTATION_FUR_TREE = {'left': '\u00AB', 'right': '\u00BB'}
WHITE_SPACE_NO_BREAKING = '\u00A0'


REGEX_LIST = [
    (r'("|\')(.*)\1', r'{left}\2{right}'.format(**QUOTATION_FUR_TREE)),
    (r'\s+', r' '),
    (r'\s+-\s+', EM_DASH),
    (r'(8|\+7)\s*\(\s*(\d{1,3})\s*\)\s*(\d{3})\s*-\s*(\d{2})\s*-\s*(\d{2})',
     r'\1 (\2) \3{0}\4{0}\5'.format(EN_DASH)),
    (r'(\b[а-яА-Яa-zA-Z]{1,2}\b)(\s+)(\b[а-яА-Яa-zA-Z]+\b)',
     r'\1{0}\3'.format(WHITE_SPACE_NO_BREAKING)),
    (r'(\b\d+\b)(\s+)(\b[а-яА-Яa-zA-Z]+\b)',
     r'\1{0}\3'.format(WHITE_SPACE_NO_BREAKING))
]


def typograf_text(text):
    for pattern, replace in REGEX_LIST:
        text = sub(pattern, replace, text)
    return text