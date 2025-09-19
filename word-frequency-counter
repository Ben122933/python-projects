from collections import Counter
import re
import os
import platform


def get_frequency(text: str) -> list[tuple[str, int]]:
    lowered_text:str = text.lower()
    words: list[str] = re.findall(r'\b\w+\b', lowered_text)
    word_counts: Counter = Counter(words)
    return word_counts.most_common()


def main() -> None:
    text: str = input('Enter your text: ').strip()
    word_frequencies: list[tuple[str, int]] = get_frequency(text)

    f = open('file.txt', 'w')
    for word, count in word_frequencies:
        f.write(f'{word}: {count}' + "\n")

    f.close()

system = platform.system()
filename = 'file.txt'

if system == 'Windows':
    os.startfile(filename)
elif system == 'Darwin':  # macOS
    os.system(f'open "{filename}"')
else:  # Linux or others
    os.system(f'xdg-open "{filename}"')


if __name__ == '__main__':
    main()
