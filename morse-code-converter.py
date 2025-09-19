morse_code_dict: dict[str, str] = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
    'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
    'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..',
    '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...',
    '8': '---..', '9': '----.', '0': '-----',
    '.': '.-.-.-', ',': '--..--', '..--..': '?', '!': '-.-.--', '-.--.': '(', '-.--.-': ')',
    '.-...': '&', ':': '---...', ';': '-.-.-.', '=': '-...-', '_': '..--.-', '...-..-': '$', '.--.-.': '@',
    ' ': '/'
}

reverse_morse_dict = {v: k for k, v in morse_code_dict.items()}
# Reverse the dictionary to convert morse code back to words

def convert_to_text(morse: str) -> str:
    return ''.join(reverse_morse_dict.get(code, '') for code in morse.split(' '))

def convert_to_morse(text: str) -> str:
    return ' '.join(morse_code_dict.get(char.upper(), '') for char in text)

TYPE = ['text', 'morse code']

def main() -> None:
    while True:
        try:
            convert_from = str(input('Convert from (text/morse code) or type (exit) to exit: '))

        except ValueError:
            print('Invalid input, please input text or morse code..')
            continue

        if convert_from.lower() == 'exit':
            break

        if convert_from.lower() not in TYPE:
            print('Invalid input, please input text or morse code. \n')
            continue


        if convert_from.lower() == ('morse code' or 'morse'):
            morse: str = input('Enter morse code: ')
            output: str = convert_to_text(morse)
            print(output)

        elif convert_from.lower() == ('text' or 'txt') :
            text: str = input('Enter text: ')
            output: str = convert_to_morse(text)
            print(output)


if __name__ == '__main__':
    main()
