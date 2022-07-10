def get_text(what_text, locale):
    messages = {'rightclick-delete': {
                    'en': 'Remove securely',
                    'pl': 'Bezpiecznie usuń'
                    },
                'rightclick-move': {
                    'en': 'Move to secured directory',
                    'pl': 'Przenieś do zabezpieczonego katalogu'
                    }
    }
    return messages[what_text][locale]