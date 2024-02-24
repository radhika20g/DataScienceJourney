#Problem Statement - Analyzing User-Generated Text Data for Keyword Frequency
from collections import Counter
import re

def analyse_text(textData):
    combined_text = ' '.join(textData)

    combined_text = combined_text.lower()

    words = re.findall(r'\b\w+\b', combined_text)

    keywords = ['of', 'good', 'it']

    keyword_counts = Counter(words)
    
    for key in keywords:
        print(f'The frequency of "{key}" in text data is "{keyword_counts[key]}" times.')

textData = ['Hi today is a good day.',
            'I did video editing.',
            'I I learned first code of the data science.',  
            'Took a bath as well.',
            'Did prayer also.',
            'I also walked around 6k steps already.',
            'Indeed it is a productive day.',
            'Glad i sat to study inspite of not feeling like it.',
            'DISCIPLICE BITCHES !!!!',
            'Truly a good day'
]

analyse_text(textData)