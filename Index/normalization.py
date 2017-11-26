from string import digits


def normalize(term):
    term = remove_digits(term)
    term = term.lower()
    term = remove_punctuation(term)
    term = remove_stopwords(term)
    return term


def remove_punctuation(term):
    symbols = ['.', ',', '!', '?', '\'s', ';', '>', '(', ')', '#', '\'', '&', '$', '*', '+', '/'
               , '@', '=', '[', ']', ':', '`', '{', '}', '\\', '-', '|']
    for sym in symbols:
        term = term.replace(sym, '').strip()

    return term


def remove_stopwords(term):
    stop_words = ['a', 'an', 'and', 'are', 'as', 'at', 'be', 'by', 'can', 'do',  'for', 'from', 'has', 'he', 'i', 'in',
                  'is', 'it', 'its', 'my', 'of', 'on', 'she', 'that', 'the', 'to', 'was', 'were', 'will', 'with']
    for word in stop_words:
        if word == term:
            return ''

    return term


def remove_digits(term):
    term = ''.join([i for i in term if not i.isdigit()])
    return term.strip()
