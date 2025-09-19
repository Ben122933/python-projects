from collections import Counter
import re

def open_file(path: str) -> str:
    with open(path, 'r') as file:
        text: str = file.read()
        return text

def analyze(text: str) -> dict[str, int]:
    print(f'"{text}"')

    words = re.findall(r'\b\w+\b', text.lower())
    most_common_words: list = Counter(words).most_common(5)
    result: dict[str, int] = {
        'total_chars_include_spaces': len(text),
        'total_chars_exclude_spaces': len(text.replace(' ', '')),
        'total_spaces': text.count(' '),
        'total_words': len(text.split(' ')),
        'most_common_words': most_common_words

    }

    return result

def main() -> None:
    text: str = open_file('note.txt')
    analysis: dict[str, int] = analyze(text)
    data: list = ['Total characters including spaces: ', 'Total characters excluding spaces: ',
                  'Total spaces: ', 'Total words:', 'Most common words:']

    i = 0
    for key, value in analysis.items():
        print(f'{data[i]} {value}')
        i += 1

if __name__ == '__main__':
    main()
